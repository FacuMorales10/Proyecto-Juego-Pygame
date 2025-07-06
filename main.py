import pygame
import random
import os

import settings as st
import assets as a
import player
import enemies
import projectiles

def main():
    # —— Inicialización de Pygame y ventana ——
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((st.ANCHO_VENTANA, st.ALTO_VENTANA))
    pygame.display.set_caption("Mach-Max")
    clock = pygame.time.Clock()
    font  = pygame.font.Font(None, 36)

    # —— Variables de juego ——
    puntuacion  = 0
    shoot_delay = 190
    last_shot   = 0

    # < ---- A CHEQUEAR ---->

    # Sistema de Vidas ***
    vida_inicial = 3
    pausa_invulnerable = 2000

    # Puntuación y vida  *****
    puntuacion = 0
    vidas = vida_inicial
    ultimo_toque = 0
    invulnerable = False
    font = pygame.font.Font(None, 36)   

    # Puntuación 
    puntuacion = 0
    font = pygame.font.Font(None, 36)  

    # Tiempo entre disparos
    shoot_delay = 190
    last_shot = 0

    # Reloj
    clock = pygame.time.Clock()

    
    # —— Bucle principal ——
    running = True
    while running:
        current_time = pygame.time.get_ticks() #Tiempo actual en ms

        # — Eventos —
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_SPACE and
                    current_time - last_shot > shoot_delay):
                    # Disparo
                    projectiles.crear(player.jugador.centerx,
                                      player.jugador.top)
                    last_shot = current_time

        # — Lógica —
        player.manejar_input()

        # Enemigos
        enemies.crear_competidor()
        enemies.mover_competidores(puntuacion)

        # Proyectiles
        projectiles.mover()

        # Colisiones
        for c in enemies.competidores[:]:
            # Choque jugador–enemigo
            if player.jugador.colliderect(c["rect"]) and not invulnerable:
                vidas -= 1
                ultimo_toque = current_time
                invulnerable = True
                enemies.competidores.remove(c)
                if vidas <= 0:
                    running = False

            # Choque proyectil–enemigo
            for p in projectiles.proyectiles[:]:
                if c["rect"].colliderect(p["rect"]):
                    enemies.competidores.remove(c)
                    projectiles.proyectiles.remove(p)
                    puntuacion += 5
                    break
    
        # Actualizando estado de invulneraBilidad
        if invulnerable:
            if current_time - ultimo_toque > pausa_invulnerable:
                invulnerable = False

        # — Dibujado —
        screen.fill(st.COLOR_01)

        # Efecto de invulnerabilidad (parpadeo de jugador)
        if not invulnerable or (current_time // 100) % 2 == 0:  # Parpadeo cada 200ms
            player.dibujar(screen)

        enemies.dibujar_competidores(screen)
        projectiles.dibujar(screen)
        
        # Mostrar puntuación 
        puntuacion_text = font.render(f"Puntuacion: {puntuacion}", True, st.COLOR_02)  #parámetros normales
        screen.blit(puntuacion_text, (10, 10))
        
        # Mostrar vidas restantes
        vida_text = font.render(f"Vidas: {vidas}", True, st.COLOR_02)  
        screen.blit(vida_text, (10, 30))
        
        pygame.display.flip()
        clock.tick(60)

    # Pantalla "GAME OVER"
    if vidas <= 0:
        game_over = True
        while game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = False
                    pygame.quit()
                    exit()  # Asegura que el juego se cierre correctamente
                if event.type == pygame.KEYDOWN:  
                    if event.key == pygame.K_RETURN:  # Detecta ENTER
                        game_over = False
            
            # Fondo semitransparente
            s = pygame.Surface((st.ANCHO_VENTANA, st.ALTO_VENTANA))
            s.set_alpha(128)
            s.fill(st.COLOR_01) 
            screen.blit(s, (0, 0))
            
            # Texto "GAME OVER"
            game_over_font = pygame.font.Font(None, 74)
            game_over_text = game_over_font.render("GAME OVER", True, st.COLOR_03)
            game_over_rect = game_over_text.get_rect(center=(st.ANCHO_VENTANA/2, st.ALTO_VENTANA/3))
            screen.blit(game_over_text, game_over_rect)
            
            # Estadísticas
            stats_font = pygame.font.Font(None, 36)
            puntuacion_final = stats_font.render(f"Puntuación Final: {puntuacion}", True, st.COLOR_03)  
            screen.blit(puntuacion_final, (st.ANCHO_VENTANA/2 - puntuacion_final.get_width()/2, st.ALTO_VENTANA/2))
            
            # Texto "Presione ENTER para SALIR"
            enter_text = stats_font.render("Presione ENTER para SALIR", True, st.COLOR_04)
            enter_rect = enter_text.get_rect(center=(st.ANCHO_VENTANA/2, st.ALTO_VENTANA - 100))
            screen.blit(enter_text, enter_rect)
            
            pygame.display.flip()  # Actualiza la pantalla dentro del bucle
            clock.tick(60)

        # HUD
        texto = font.render(f"Puntuacion: {puntuacion}", True, st.COLOR_02)
        screen.blit(texto, (10, 10))

        pygame.display.flip()
        clock.tick(60)
    pygame.quit()

if __name__ == "__main__":
    main()
