import pygame
import settings as st
import json
import os

RUTA_RANKING = "ranking_data.json"

def mostrar_ranking(screen, fuente, fondo=None):
    """
    Muestra una pantalla con el Top 5 de puntajes reales.
    """
    clock = pygame.time.Clock()

    # Cargar datos reales
    if os.path.exists(RUTA_RANKING):
        with open(RUTA_RANKING, "r", encoding="utf-8") as archivo:
            try:
                datos = json.load(archivo)
            except json.JSONDecodeError:
                datos = []
    else:
        datos = []

    esperando = True
    while esperando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif evento.type == pygame.KEYDOWN or evento.type == pygame.MOUSEBUTTONDOWN:
                esperando = False

        # Fondo
        if fondo:
            screen.blit(fondo, (0, 0))
        else:
            screen.fill(st.COLOR_01)

        # Título
        titulo = fuente.render("Ranking - Top 5", True, st.COLOR_04)
        screen.blit(titulo, titulo.get_rect(center=(st.ANCHO_VENTANA // 2, 100)))

        # Listado de puntajes
        for i, entrada in enumerate(datos):
            nombre = entrada["nombre"]
            puntaje = entrada["puntaje"]
            linea = fuente.render(f"{i+1}. {nombre} - {puntaje}", True, st.COLOR_02)
            screen.blit(linea, (st.ANCHO_VENTANA//2 - 100, 160 + i * 30))

        pygame.display.flip()
        clock.tick(st.FPS)