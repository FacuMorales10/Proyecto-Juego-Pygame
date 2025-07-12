import pygame
import settings as st
import pygame.mixer
import json
import os

# -------- FUNCIONES DE BOTONES --------
def esta_sobre(mouse_pos, boton):
    """
    Verifica si el mouse está sobre un botón.
    """
    x, y = mouse_pos
    return (boton["x"] <= x <= boton["x"] + boton["w"] and
            boton["y"] <= y <= boton["y"] + boton["h"])

def cambio_color_boton(mouse_pos, boton, click, color_normal, color_hover, color_click):
    """
    Devuelve el color del botón según la interacción del mouse.
    """
    if esta_sobre(mouse_pos, boton):
        return color_click if click else color_hover
    return color_normal

# -------- SONIDO Y MÚSICA --------
def reproducir_musica(nombre_archivo, loop=False):
    """
    Carga y reproduce música de fondo.
    """
    ruta = f"assets/music/{nombre_archivo}"
    pygame.mixer.music.load(ruta)
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(-1 if loop else 0)

def reproducir_sonido_boton(mouse_pos, boton, click):
    """
    Reproduce un efecto de sonido si se hace clic sobre un botón.
    """
    if esta_sobre(mouse_pos, boton) and click:
        efecto = pygame.mixer.Sound("assets/sounds/click.wav")
        efecto.set_volume(0.5)
        efecto.play()

def actualizar_sonido(eventos, mouseX, mouseY, rect_icono, sonido_activado):
    """
    Activa o desactiva el sonido si se clickea sobre el icono.
    """
    for evento in eventos:
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if rect_icono.collidepoint(mouseX, mouseY):
                if sonido_activado:
                    pygame.mixer.music.set_volume(0)
                else:
                    pygame.mixer.music.set_volume(0.4)
                return not sonido_activado
    return sonido_activado

# -------- CRÉDITOS --------
def mostrar_creditos(screen, fuente, fondo=None):
    """
    Muestra una pantalla con créditos del juego.
    """
    clock = pygame.time.Clock()
    creditos = [
        "Créditos de Mach-Max",
        "Integrantes:",
        "Lucas, Dai, Alexis, Facu",
        "Materia: Programación I",
        "Universidad: UTN",
        "",
        "Presiona cualquier tecla para volver"
    ]

    esperando = True
    while esperando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif evento.type == pygame.KEYDOWN or evento.type == pygame.MOUSEBUTTONDOWN:
                esperando = False

        if fondo:
            screen.blit(fondo, (0, 0))
        else:
            screen.fill(st.COLOR_01)

        for i, linea in enumerate(creditos):
            texto = fuente.render(linea, True, (0, 0, 0))
            rect = texto.get_rect(center=(st.ANCHO_VENTANA//2, 150 + i * 40))
            screen.blit(texto, rect)

        pygame.display.flip()
        clock.tick(st.FPS)

# -------- RANKING --------
RUTA_RANKING = "ranking_data.json"

def guardar_puntaje(nombre, puntaje):
    """
    Guarda el puntaje con el nombre del jugador en un archivo JSON.
    Mantiene solo los 5 mejores puntajes.
    """
    datos = []

    if os.path.exists(RUTA_RANKING):
        with open(RUTA_RANKING, "r", encoding="utf-8") as archivo:
            try:
                datos = json.load(archivo)
            except json.JSONDecodeError:
                datos = []

    datos.append({"nombre": nombre, "puntaje": puntaje})
    datos = sorted(datos, key=lambda x: x["puntaje"], reverse=True)[:5]

    with open(RUTA_RANKING, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4)