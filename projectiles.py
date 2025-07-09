
import pygame, settings as st

proyectiles = []

def crear(x, y, imagen):
    """
    Crea un proyectil con una imagen en la posición (x, y).
    """
    rect = pygame.Rect(
        x - imagen.get_width() // 2,
        y,
        imagen.get_width(),
        imagen.get_height()
    )
    proyectiles.append({"rect": rect, "speed": 7, "img": imagen})

def mover():
    for p in proyectiles[:]:
        p["rect"].y -= p["speed"]
        if p["rect"].bottom < 0:
            proyectiles.remove(p)

def dibujar(screen):
    for p in proyectiles:
        screen.blit(p["img"], p["rect"])


        
