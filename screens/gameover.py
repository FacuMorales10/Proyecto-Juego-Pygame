import pygame
import settings as st

def pantalla_game_over(screen, font, puntuacion):
    """
    Muestra la pantalla de GAME OVER y cierra el juego
    cuando se presiona ENTER o ESC.
    """
    clock = pygame.time.Clock()
    mostrando = True

    while mostrando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_RETURN, pygame.K_ESCAPE):
                    mostrando = False

        # Fondo semitransparente
        overlay = pygame.Surface((st.ANCHO_VENTANA, st.ALTO_VENTANA))
        overlay.set_alpha(180)
        overlay.fill(st.COLOR_01)
        screen.blit(overlay, (0, 0))

        # Texto principal
        go_font = pygame.font.Font(None, 74)
        go_surf = go_font.render("GAME OVER", True, st.COLOR_03)
        go_rect = go_surf.get_rect(center=(st.ANCHO_VENTANA//2, st.ALTO_VENTANA//3))
        screen.blit(go_surf, go_rect)

        # Puntuación
        stats_font = pygame.font.Font(None, 36)
        score_surf = stats_font.render(f"Puntuación Final: {puntuacion}", True, st.COLOR_02)
        score_rect = score_surf.get_rect(center=(st.ANCHO_VENTANA//2, st.ALTO_VENTANA//2))
        screen.blit(score_surf, score_rect)

        # Instrucciones
        prompt_text = "Presiona ENTER para salir"
        prompt_surf = stats_font.render(prompt_text, True, st.COLOR_04)
        prompt_rect = prompt_surf.get_rect(center=(st.ANCHO_VENTANA//2, st.ALTO_VENTANA - 100))
        screen.blit(prompt_surf, prompt_rect)

        pygame.display.flip()
        clock.tick(st.FPS)
