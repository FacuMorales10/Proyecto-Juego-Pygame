import pygame
import settings as st
import assets as a

# Rect y sprite del jugador
jugador = a.coche_max_5.get_rect(
    centerx = st.ANCHO_VENTANA // 2,
    bottom  = st.ALTO_VENTANA  - 10
)

def manejar_input():
    """
    Lee teclas y mueve el rectángulo jugador.
    Llamar en cada iteración del loop.
    """
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]  and jugador.left  > 0: jugador.x -= 5
    if keys[pygame.K_RIGHT] and jugador.right < st.ANCHO_VENTANA: jugador.x += 5
    if keys[pygame.K_UP]    and jugador.top   > 0: jugador.y -= 5
    if keys[pygame.K_DOWN]  and jugador.bottom< st.ALTO_VENTANA: jugador.y += 5

def dibujar(screen):
    """Dibuja al jugador en pantalla."""
    screen.blit(a.coche_max_5, jugador)