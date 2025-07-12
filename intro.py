import pygame
import settings as st

def mostrar_intro(screen):
    pygame.init()
    clock = pygame.time.Clock()

    # Cargar fondo de la intro
    fondo = pygame.image.load("assets/images/intro_fondo.png")
    fondo = pygame.transform.scale(fondo, (st.ANCHO_VENTANA, st.ALTO_VENTANA))

    fuente = pygame.font.Font("assets/fonts/arcade.ttf", 20)
    texto_intro = [
    "Speed Racer y su legendario Mach 5", 
    "vuelven a las pistas contra sus", 
    "rivales más peligrosos.",
    "¡Esquiva, destruye y sobrevive!"
    ]

    tiempo_entre_lineas = 500  # ms
    linea_actual = 0
    ultimo_tiempo = pygame.time.get_ticks()
    mostrar_todo = False

    esperando = False

    while not esperando:
        screen.blit(fondo, (0, 0))

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif evento.type == pygame.KEYDOWN or evento.type == pygame.MOUSEBUTTONDOWN:
                esperando = True

        # Mostrar líneas progresivamente
        if not mostrar_todo and linea_actual < len(texto_intro):
            if pygame.time.get_ticks() - ultimo_tiempo > tiempo_entre_lineas:
                linea_actual += 1
                ultimo_tiempo = pygame.time.get_ticks()
            if linea_actual == len(texto_intro):
                mostrar_todo = True

        for i in range(linea_actual):
            texto = fuente.render(texto_intro[i], True, (0, 0, 0))
            rect = texto.get_rect(center=(st.ANCHO_VENTANA // 2, 200 + i * 35))
            screen.blit(texto, rect)

        # Mostrar indicación para saltar
        if mostrar_todo:
            salto_texto = fuente.render("Presiona una tecla para continuar...", True, (255, 0, 0))
            salto_rect = salto_texto.get_rect(center=(st.ANCHO_VENTANA // 2, st.ALTO_VENTANA - 50))
            screen.blit(salto_texto, salto_rect)

        pygame.display.flip()
        clock.tick(st.FPS)