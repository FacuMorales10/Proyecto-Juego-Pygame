import random
import pygame
import settings as st
import assets as a

# Lista de competidores en pantalla
competidores = []

def crear_competidor():
    """
    Si hay menos de 5 competidores, genera uno nuevo
    con posición aleatoria en X, Y = -30, sprite y velocidad.
    """
    if len(competidores) < 5:
        rect = pygame.Rect(
            random.randint(0, st.ANCHO_VENTANA - 30),-30, 30, 60)
        competidores.append({
            "rect": rect,
            "imagen": random.choice(a.autos_enemigos),
            "velocidad": random.randint(2, 5)
        })

def mover_competidores():
    """Mueve cada rival y lo elimina al salir de la ventana."""
    for rival in competidores[:]:
        rival["rect"].y += rival["velocidad"]
        if rival["rect"].top > st.ALTO_VENTANA:
            competidores.remove(rival)

def dibujar_competidores(screen):
    """Dibuja todos los rivales en pantalla."""
    for rival in competidores:
        screen.blit(rival["imagen"], rival["rect"])
