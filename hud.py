
import pygame
import settings as st

def dibujar_hud(screen, font, puntuacion, vidas, min, seg):
    """
    Dibuja en pantalla la puntuación y las vidas restantes.
    """
    #Mostrar Tiempo
    tiempo_text = font.render(f"Tiempo {min:02d}:{seg:02d}", True, st.COLOR_02)
    screen.blit(tiempo_text, (10, 10))
    
    # Mostrar puntuación
    puntuacion_text = font.render(f"Puntuación: {puntuacion}", True, st.COLOR_02)
    screen.blit(puntuacion_text, (10, 30))
    
    # VIDAS
    vida_text = font.render(f"Vidas: {vidas}", True, st.COLOR_02)
    screen.blit(vida_text, (10, 50))
    
    
