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
            random.randint(0, st.ANCHO_VENTANA - 30),
            -30,
            30,
            60
        )
        competidores.append({
            "rect": rect,
            "imagen": random.choice(a.autos_enemigos),
            "velocidad": random.randint(2, 5)
        })

def mover_competidores():
    """
    Recorre la lista, desplaza cada competidor según su velocidad
    y lo elimina (sumando punto) si sale por abajo de la ventana.
    """
    for c in competidores[:]:
        c["rect"].y += c["velocidad"]
        if c["rect"].top > st.ALTO_VENTANA:
            competidores.remove(c)

def dibujar_competidores(screen):
    """
    Dibuja en pantalla cada competidor con su imagen en su rect.
    """
    for c in competidores:
        screen.blit(c["imagen"], c["rect"])
