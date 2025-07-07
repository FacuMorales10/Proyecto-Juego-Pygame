import pygame
import settings as st

def pantalla_game_over(screen, font, puntuacion):
    """
    Muestra una pantalla de GAME OVER con la puntuación final
    y espera a que el jugador presione ENTER o cierre la ventana.
    """
    clock = pygame.time.Clock()
    mostrando = True

    while mostrando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                mostrando = False

        # Fondo semitransparente
        overlay = pygame.Surface((st.ANCHO_VENTANA, st.ALTO_VENTANA))
        overlay.set_alpha(180)
        overlay.fill(st.COLOR_01)
        screen.blit(overlay, (0, 0))

        # Texto principal “GAME OVER”
        go_font = pygame.font.Font(None, 74)
        go_surf = go_font.render("GAME OVER", True, st.COLOR_03)
        go_rect = go_surf.get_rect(center=(st.ANCHO_VENTANA//2, st.ALTO_VENTANA//3))
        screen.blit(go_surf, go_rect)

        # Puntuación final
        stats_font = pygame.font.Font(None, 36)
        score_surf = stats_font.render(f"Puntuación Final: {puntuacion}", True, st.COLOR_02)
        score_rect = score_surf.get_rect(center=(st.ANCHO_VENTANA//2, st.ALTO_VENTANA//2))
        screen.blit(score_surf, score_rect)

        # Prompt de reinicio
        prompt_surf = stats_font.render("Presiona ENTER para volver a jugar", True, st.COLOR_04)
        prompt_rect = prompt_surf.get_rect(center=(st.ANCHO_VENTANA//2, st.ALTO_VENTANA - 100))
        screen.blit(prompt_surf, prompt_rect)

        pygame.display.flip()
        clock.tick(st.FPS)
