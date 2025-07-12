import pygame
import os
import assets as a

def play_music():
    pygame.mixer.init()

    ruta_musica = os.path.join(a.MUSICA_DIR, "InGameMeteoro.mp3")

    pygame.mixer.music.load(ruta_musica)
    pygame.mixer.music.play(loops=-1)


def play_music_menu():
    ruta_musica = os.path.join(a.MUSICA_DIR, "Opening_Meteoro.MP3")
    pygame.mixer.music.load(ruta_musica)
    pygame.mixer.music.play(loops=-1)
