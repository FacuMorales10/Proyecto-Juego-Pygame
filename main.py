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
from screens.pause import mostrar_pantalla_pausa
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
    enemies.competidores = []
    projectiles.proyectiles = []


    # imagen del proyectil (sierra)
    sierra_img = pygame.image.load(a.SIERRA_PATH).convert_alpha()
    sierra_img = pygame.transform.scale(sierra_img, (16, 16))

    #Sistema de Vidas
    vida_inicial = 3
    pausa_invulnerable = 2000

    # Puntuación y vida
    vidas = vida_inicial
    ultimo_toque = 0
    invulnerable = False  

    # Puntuación 
    puntuacion = 0 

    ##Tiempo entre disparos
    shoot_delay = 190
    last_shot = 0
    
    #Tiempo de inicio
    tiempo_inicial = pygame.time.get_ticks()
    
    # Reloj
    clock = pygame.time.Clock()
    # Variables de estado
    pausa = False
    running = True
    
    # Reiniciar posición del jugador
    player.jugador = player.a.coche_max_5.get_rect(
    centerx = st.ANCHO_VENTANA // 2,
    bottom  = st.ALTO_VENTANA  - 10
    )

    # Bucle principal
    while running:
        current_time = pygame.time.get_ticks() #Tiempo actual en ms

        # — Eventos —
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:  
                    pausa = not pausa
                if (event.key == pygame.K_SPACE and
                    current_time - last_shot > shoot_delay and not pausa):
                    # Disparo
                    projectiles.crear(player.jugador.centerx,
                                    player.jugador.top, sierra_img)
                    last_shot = current_time

        # — Lógica —
        player.manejar_input()

        # Enemigos (spawn cada spawn_delay ms)
        if current_time - last_spawn >= spawn_delay:
            enemies.crear_competidor()
            last_spawn = current_time
        puntuacion += enemies.mover_competidores()

        # Proyectiles
        projectiles.mover()

        # Colisiones
        estado = {
            "jugador": player.jugador,
            "competidores": enemies.competidores,
            "invulnerable": invulnerable,
            "ultimo_toque": ultimo_toque,
            "pausa_invulnerable": pausa_invulnerable,
            "current_time": current_time,
            "vidas": vidas
        }
        estado = colision_jugador_enemigo(estado)

        vidas = estado["vidas"]
        invulnerable = estado["invulnerable"]
        ultimo_toque = estado["ultimo_toque"]

        if vidas <= 0:
            running = False

        puntuacion += colision_proyectil_enemigo(
            projectiles.proyectiles, enemies.competidores
        )

        # En estado de PAUSA
        if pausa:
            mostrar_pantalla_pausa(screen, st, clock)
            pausa = False
    
        # Actualizando estado de invulnerabilidad
        if invulnerable:
            if current_time - ultimo_toque > pausa_invulnerable:
                invulnerable = False
                
        #Tiempo de juego 
        tiempo = (current_time - tiempo_inicial ) // 1000
        min = tiempo // 60
        seg = tiempo % 60

        # — Dibujado —
        screen.blit(background, (0, 0))

        # Efecto de invulnerabilidad (parpadeo de jugador)
        if not invulnerable or (current_time // 100) % 2 == 0:  # Parpadeo cada 200ms
            player.dibujar(screen)

        enemies.dibujar_competidores(screen)
        projectiles.dibujar(screen)
        
        # HUD puntuacion y vidas
        hud.dibujar_hud(screen, font, puntuacion, vidas, min, seg)

        pygame.display.flip()
        clock.tick(60)
        
        if vidas <= 0:
            pantalla_game_over(screen, font, puntuacion)
            return

    pygame.quit()

if __name__ == "__main__":
    main()
