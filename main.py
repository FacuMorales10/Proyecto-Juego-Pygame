import pygame
from screens.menu import mostrar_menu_principal
from intro import mostrar_intro
import settings as st

if __name__ == "__main__":
    pygame.init()

    pantalla = pygame.display.set_mode((st.ANCHO_VENTANA, st.ALTO_VENTANA))
    pygame.display.set_caption("Mach-Max")

    mostrar_intro(pantalla)
    mostrar_menu_principal(pantalla)