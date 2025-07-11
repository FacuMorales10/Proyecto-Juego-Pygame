import pygame
import os
import assets as a

def play_music():
    pygame.mixer.init()

    ruta_musica = os.path.join(a.MUSICA_DIR, "InGameMeteoro.mp3")

    pygame.mixer.music.load(ruta_musica)
    pygame.mixer.music.play(loops=-1)