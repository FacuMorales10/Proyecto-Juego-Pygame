import pygame

def mostrar_pantalla_pausa(screen, st, clock):
    """
    Pausa hasta que el jugador presione 'CTRL' (una vez para pausar, otra para continuar).
    """
    font = pygame.font.Font(None, 48)
    pausado = True
    pygame.mixer.music.pause()  # Pausar música

    while pausado:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL:
                    pausado = False
                    pygame.mixer.music.unpause()  # Reanudar música

        overlay = pygame.Surface((st.ANCHO_VENTANA, st.ALTO_VENTANA))
        overlay.set_alpha(180)
        overlay.fill(st.COLOR_01)
        screen.blit(overlay, (0, 0))

        texto = font.render("PAUSA", True, st.COLOR_03)
        subtexto = font.render("Presiona CTRL para continuar", True, st.COLOR_04)

        rect_texto = texto.get_rect(center=(st.ANCHO_VENTANA // 2, st.ALTO_VENTANA // 2 - 30))
        rect_sub = subtexto.get_rect(center=(st.ANCHO_VENTANA // 2, st.ALTO_VENTANA // 2 + 30))

        screen.blit(texto, rect_texto)
        screen.blit(subtexto, rect_sub)

        pygame.display.flip()
        clock.tick(st.FPS)
