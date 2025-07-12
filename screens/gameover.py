import pygame
import settings as st
from utils import guardar_puntaje

def pantalla_game_over(screen, fuente, puntuacion):
    """
    Muestra pantalla de GAME OVER, permite ingresar nombre
    y guarda puntaje en archivo al presionar ENTER.
    """
    clock = pygame.time.Clock()
    nombre = ""
    input_activo = True
    max_caracteres = 10

    while input_activo:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and nombre.strip():
                    guardar_puntaje(nombre.strip(), puntuacion)
                    input_activo = False
                elif event.key == pygame.K_BACKSPACE:
                    nombre = nombre[:-1]
                elif len(nombre) < max_caracteres and event.unicode.isprintable():
                    nombre += event.unicode

        # Fondo semitransparente
        overlay = pygame.Surface((st.ANCHO_VENTANA, st.ALTO_VENTANA))
        overlay.set_alpha(180)
        overlay.fill(st.COLOR_01)
        screen.blit(overlay, (0, 0))

        # Título "GAME OVER"
        font_grande = pygame.font.Font("assets/fonts/arcade.ttf", 64)
        texto_go = font_grande.render("GAME OVER", True, st.COLOR_03)
        rect_go = texto_go.get_rect(center=(st.ANCHO_VENTANA // 2, st.ALTO_VENTANA // 3))
        screen.blit(texto_go, rect_go)

        # Puntuación final
        stats_font = fuente
        texto_score = stats_font.render(f"Puntuación Final: {puntuacion}", True, st.COLOR_02)
        rect_score = texto_score.get_rect(center=(st.ANCHO_VENTANA // 2, st.ALTO_VENTANA // 2))
        screen.blit(texto_score, rect_score)

        # Instrucciones
        texto_ingreso = stats_font.render("Ingresá tu nombre y presioná ENTER", True, st.COLOR_04)
        rect_ingreso = texto_ingreso.get_rect(center=(st.ANCHO_VENTANA // 2, st.ALTO_VENTANA - 140))
        screen.blit(texto_ingreso, rect_ingreso)

        # Caja de entrada de texto
        caja_rect = pygame.Rect(st.ANCHO_VENTANA // 2 - 100, st.ALTO_VENTANA - 100, 200, 40)
        pygame.draw.rect(screen, st.COLOR_02, caja_rect, 2)

        texto_nombre = stats_font.render(nombre, True, st.COLOR_02)
        rect_nombre = texto_nombre.get_rect(center=caja_rect.center)
        screen.blit(texto_nombre, rect_nombre)

        pygame.display.flip()
        clock.tick(st.FPS)
