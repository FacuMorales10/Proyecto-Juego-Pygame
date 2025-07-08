import pygame
import settings as st

def dibujar_hud(screen, font, puntuacion, vidas):
    """
    Dibuja en pantalla la puntuación y las vidas restantes.
    """
    # PUNTUACIÓN
    score_surf = font.render(f"Puntuación: {puntuacion}", True, st.COLOR_02)
    screen.blit(score_surf, (10, 10))
    # VIDAS
    lives_surf = font.render(f"Vidas: {vidas}", True, st.COLOR_02)
    screen.blit(lives_surf, (10, 30))