import pygame

def mostrar_pantalla_pausa(screen, st, clock):
    pausa_font = pygame.font.Font(None, 35)
    pausa_text = pausa_font.render("PAUSA - Presiona (P) para continuar", True, st.COLOR_02)
    text_rect = pausa_text.get_rect(center=(st.ANCHO_VENTANA // 2, st.ALTO_VENTANA // 2))

    en_pausa = True
    while en_pausa:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                en_pausa = False

        screen.blit(pausa_text, text_rect)
        pygame.display.flip()
        clock.tick(10)