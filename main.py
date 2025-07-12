import pygame
from screens.menu import mostrar_menu_principal
from intro import mostrar_intro
import settings as st
from music import play_music_menu 

if __name__ == "__main__":
    pygame.init()
    pygame.mixer.init()  
    pygame.mixer.music.set_volume(0.4)

    play_music_menu()  

    pantalla = pygame.display.set_mode((st.ANCHO_VENTANA, st.ALTO_VENTANA))
    pygame.display.set_caption("Mach-Max")

    mostrar_intro(pantalla)
    mostrar_menu_principal(pantalla)