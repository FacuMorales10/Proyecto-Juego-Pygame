
import pygame, settings as st

proyectiles = []

def crear(x, y):
    proyectiles.append({"rect": pygame.Rect(x-2, y, 4, 10), "speed": 7})

def mover():
    for p in proyectiles[:]:
        p["rect"].y -= p["speed"]
        if p["rect"].bottom < 0:
            proyectiles.remove(p)

def dibujar(screen):
    for p in proyectiles:
        pygame.draw.rect(screen, st.COLOR_04, p["rect"])
