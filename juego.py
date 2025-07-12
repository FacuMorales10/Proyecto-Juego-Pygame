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
from collisions import colision_jugador_enemigo, colision_proyectil_enemigo

def main():
    # —— Inicialización de Pygame y ventana ——
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((st.ANCHO_VENTANA, st.ALTO_VENTANA))
    pygame.display.set_caption("Mach-Max")
    font  = pygame.font.Font(None, 24)
    spawn_delay = 1000
    last_spawn = pygame.time.get_ticks()

    background = pygame.transform.scale(
        pygame.image.load(a.BACKGROUND_PATH).convert(),
        (st.ANCHO_VENTANA, st.ALTO_VENTANA)
    )

    # Imagen del proyectil (sierra)
    sierra_img = pygame.image.load(a.SIERRA_PATH).convert_alpha()
    sierra_img = pygame.transform.scale(sierra_img, (16, 16))

    # Sistema de Vidas
    vida_inicial = 3
    pausa_invulnerable = 2000

    vidas = vida_inicial
    ultimo_toque = 0
    invulnerable = False  
    puntuacion = 0 

    shoot_delay = 190
    last_shot = 0
    tiempo_inicial = pygame.time.get_ticks()
    clock = pygame.time.Clock()
    
    enemies.competidores = []
    projectiles.proyectiles = []

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
                    projectiles.crear(player.jugador.centerx,
                                      player.jugador.top, sierra_img)
                    last_shot = current_time

        # — Lógica —
        player.manejar_input()

        if current_time - last_spawn >= spawn_delay:
            enemies.crear_competidor()
            last_spawn = current_time
        puntuacion += enemies.mover_competidores()

        projectiles.mover()

        # Colisiones
        vidas, invulnerable, ultimo_toque = colision_jugador_enemigo(
            player.jugador,
            enemies.competidores,
            invulnerable,
            ultimo_toque,
            pausa_invulnerable,
            current_time,
            vidas
        )

        puntuacion += colision_proyectil_enemigo(
            projectiles.proyectiles,
            enemies.competidores
        )

        if vidas <= 0:
            pantalla_game_over(screen, font, puntuacion)
            return

        # Tiempo en minutos y segundos
        tiempo = (current_time - tiempo_inicial) // 1000
        min = tiempo // 60
        seg = tiempo % 60

        # — Dibujado —
        screen.blit(background, (0, 0))

        if not invulnerable or (current_time // 100) % 2 == 0:
            player.dibujar(screen)

        enemies.dibujar_competidores(screen)
        projectiles.dibujar(screen)
        hud.dibujar_hud(screen, font, puntuacion, vidas, min, seg)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()