import pygame
import random
import os

import settings as st
import assets as a
import player
import enemies
import projectiles
import hud
from screens.gameover import pantalla_game_over
from assets import BACKGROUND_PATH

def main():
    # —— Inicialización de Pygame y ventana ——
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((st.ANCHO_VENTANA, st.ALTO_VENTANA))
    pygame.display.set_caption("Mach-Max")
    clock = pygame.time.Clock()
    font  = pygame.font.Font(None, 36)
    spawn_delay = 1000
    last_spawn = pygame.time.get_ticks()

    background = pygame.transform.scale(
    pygame.image.load(a.BACKGROUND_PATH).convert(),
    (st.ANCHO_VENTANA, st.ALTO_VENTANA)
)


    # Sistema de Vidas ***
    vida_inicial = 3
    pausa_invulnerable = 2000

    # Puntuación y vida  *****
    vidas = vida_inicial
    ultimo_toque = 0
    invulnerable = False  

    # Puntuación 
    puntuacion = 0 

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

        # Enemigos (spawn cada spawn_delay ms)
        if current_time - last_spawn >= spawn_delay:
            enemies.crear_competidor()
            last_spawn = current_time
        enemies.mover_competidores()

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
        screen.blit(background, (0, 0))

        # Efecto de invulnerabilidad (parpadeo de jugador)
        if not invulnerable or (current_time // 100) % 2 == 0:  # Parpadeo cada 200ms
            player.dibujar(screen)

        enemies.dibujar_competidores(screen)
        projectiles.dibujar(screen)
        
        # Mostrar puntuación 
        puntuacion_text = font.render(f"Puntuacion: {puntuacion}", True, st.COLOR_02)  #parámetros normales
        screen.blit(puntuacion_text, (10, 10))
        
        # HUD puntuacion y vidas
        hud.dibujar_hud(screen, font, puntuacion, vidas)

        pygame.display.flip()
        clock.tick(60)
        
        if vidas <= 0:
            pantalla_game_over(screen, font, puntuacion)

    pygame.quit()

if __name__ == "__main__":
    main()
