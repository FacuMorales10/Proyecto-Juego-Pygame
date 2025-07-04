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
    pygame.display.set_caption("Os-Car")
    clock = pygame.time.Clock()
    font  = pygame.font.Font(None, 36)

    # —— Variables de juego ——
    puntuacion  = 0
    shoot_delay = 190
    last_shot   = 0
    
    # —— Bucle principal ——
    running = True
    while running:
        current_time = pygame.time.get_ticks()

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
        enemies.mover_competidores()

        # Proyectiles
        projectiles.mover()

        # Colisiones
        for c in enemies.competidores[:]:
            # Choque jugador–enemigo
            if player.jugador.colliderect(c["rect"]):
                running = False
                break
            # Choque proyectil–enemigo
            for p in projectiles.proyectiles[:]:
                if c["rect"].colliderect(p["rect"]):
                    enemies.competidores.remove(c)
                    projectiles.proyectiles.remove(p)
                    puntuacion += 5
                    break

        # — Dibujado —
        screen.fill(st.COLOR_01)
        player.dibujar(screen)
        enemies.dibujar_competidores(screen)
        projectiles.dibujar(screen)

        # HUD
        texto = font.render(f"Puntuacion: {puntuacion}", True, st.COLOR_02)
        screen.blit(texto, (10, 10))

        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
if __name__ == "__main__":
    main()