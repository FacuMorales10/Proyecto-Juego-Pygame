import pygame
import settings as st
import assets as a
from juego import main as jugar
from ranking import mostrar_ranking
from utils import (esta_sobre,
                   cambio_color_boton,
                   mostrar_creditos,
                   #reproducir_musica,
                   reproducir_sonido_boton,
                   actualizar_sonido)

def mostrar_menu_principal(screen):
    clock = pygame.time.Clock()

    #reproducir_musica("musica_menu.ogg", loop=True)

    fuente_grande = pygame.font.Font("assets/fonts/arcade.ttf", 36)
    fuente_chica = pygame.font.Font("assets/fonts/arcade.ttf", 22)
    #fuente_titulo = pygame.font.Font("assets/fonts/arcade.ttf", 64)


    fondo = pygame.image.load("assets/images/fondo.png")
    fondo = pygame.transform.scale(fondo, (st.ANCHO_VENTANA, st.ALTO_VENTANA))

    # Título en texto con fuente arcade
    fuente_titulo = pygame.font.Font("assets/fonts/arcade.ttf", 64)
    titulo_texto = fuente_titulo.render("MACH-MAX", True, st.COLOR_04)
    titulo_rect = titulo_texto.get_rect(center=(st.ANCHO_VENTANA // 2, 120))
    screen.blit(titulo_texto, titulo_rect)



    #sonido_on = pygame.image.load("assets/images/sonido_on.png")
    #sonido_off = pygame.image.load("assets/images/sonido_off.png")
    #sonido_on = pygame.transform.scale(sonido_on, (40, 40))
    #sonido_off = pygame.transform.scale(sonido_off, (40, 40))
    #icono_sonido = pygame.Rect(st.ANCHO_VENTANA - 50, st.ALTO_VENTANA - 50, 40, 40)

    botones = [
        {"texto": "Jugar", "x": 330, "y": 280, "w": 140, "h": 40},
        {"texto": "Ranking", "x": 315, "y": 340, "w": 170, "h": 40},
        {"texto": "Creditos", "x": 315, "y": 400, "w": 170, "h": 40},
        {"texto": "Salir", "x": 330, "y": 460, "w": 140, "h": 40}
    ]

    sonido_activado = True
    en_menu = True

    while en_menu:
        screen.blit(fondo, (0, 0))
        screen.blit(titulo_texto, (200, 100))

        eventos = pygame.event.get()
        mouseX, mouseY = pygame.mouse.get_pos()
        click = False

        for evento in eventos:
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                click = True

        #sonido_activado = actualizar_sonido(eventos, mouseX, mouseY, icono_sonido, sonido_activado)

        for boton in botones:
            mouse_pos = (mouseX, mouseY)
            reproducir_sonido_boton(mouse_pos, boton, click)
            color = cambio_color_boton(mouse_pos, boton, click, st.COLOR_02, st.COLOR_03, st.COLOR_04)
            if click and esta_sobre(mouse_pos, boton):
                if boton["texto"] == "Jugar":
                    jugar()
                elif boton["texto"] == "Ranking":
                    mostrar_ranking(screen, fuente_chica, fondo)
                elif boton["texto"] == "Creditos":
                    mostrar_creditos(screen, fuente_chica, fondo)
                elif boton["texto"] == "Salir":
                    pygame.quit()
                    exit()
            texto = fuente_grande.render(boton["texto"], True, color)
            screen.blit(texto, (boton["x"], boton["y"]))

        #screen.blit(sonido_on if sonido_activado else sonido_off, icono_sonido)
        pygame.display.flip()
        clock.tick(st.FPS)
