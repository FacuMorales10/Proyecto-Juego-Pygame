import os
import pygame
import settings as st 

ASSETS_DIR   = os.path.dirname(__file__)
IMAGENES_DIR = os.path.join(ASSETS_DIR, "assets", "images")
SONIDOS_DIR  = os.path.join(ASSETS_DIR, "assets", "sounds")
MUSICA_DIR   = os.path.join(ASSETS_DIR, "assets", "music")


coche_max_5 = pygame.transform.scale(
    pygame.image.load(os.path.join(IMAGENES_DIR, "Max5.png")),
    (65, 110)
)


autos_enemigos = [
    pygame.transform.scale(
        pygame.image.load(os.path.join(IMAGENES_DIR, "RacerX.png")),
        (30, 60)
    ),
    pygame.transform.scale(
        pygame.image.load(os.path.join(IMAGENES_DIR, "Spider11.png")),
        (30, 60)
    )
]