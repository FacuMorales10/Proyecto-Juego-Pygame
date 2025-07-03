#main

import pygame
import random
import json
import os

pygame.init()
pygame.mixer.init() # Inicializa el mezclador de sonido de Pygame

# Configurar la pantalla (ALTO/ANCHO)
ANCHO_VENTANA = 800  
ALTO_VENTANA = 600
screen = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("Mach-Max")

# Rutas a tus carpetas de assets
ASSETS_DIR = os.path.dirname(__file__) 
IMAGENES_DIR = os.path.join(ASSETS_DIR, "assets", "images")
SONIDOS_DIR = os.path.join(ASSETS_DIR, "assets", "sounds")
MUSICA_DIR = os.path.join(ASSETS_DIR, "assets", "music")

#imagen del coche del jugador
coche_max_5 = pygame.image.load(os.path.join(IMAGENES_DIR, "Max5.png")).convert_alpha()
coche_max_5 = pygame.transform.scale(coche_max_5, (65, 110 ))

#imagen del coche enemigo
autos_enemigos = [
    pygame.transform.scale(pygame.image.load(os.path.join(IMAGENES_DIR, "RacerX.png")).convert_alpha(), (30, 60)),
    pygame.transform.scale(pygame.image.load(os.path.join(IMAGENES_DIR, "Spider11.png")).convert_alpha(), (30, 60)),
    pygame.transform.scale(pygame.image.load(os.path.join(IMAGENES_DIR, "Mati21.png")).convert_alpha(), (30, 60)),
]


# Colores
COLOR_01 = (0, 0, 0) #NEGRO
COLOR_02 = (255, 255, 255) #BLANCO
COLOR_03 = (255, 0, 0) #ROJO
COLOR_04 = (255, 255, 0) #AMARILLO
COLOR_DEBUG = (0, 255, 0) # VERDE

# Jugador 
jugador = coche_max_5.get_rect()
# Posiciona el jugador:Add commentMore actions
jugador.centerx = ANCHO_VENTANA // 2 
jugador.bottom = ALTO_VENTANA - 10 

# Proyectiles 
proyectiles = []
def crear_proyectil(x, y):
    return {
        "rect": pygame.Rect(x - 2, y, 4, 10),
        "speed": 7
    }

def mover_proyectil(proyectil):
    proyectil["rect"].y -= proyectil["speed"]

def dibujar_proyectil(proyectil):
    pygame.draw.rect(screen, COLOR_04, proyectil["rect"])


# Competidores
competidor_ancho = 40 
competidor_alto = 20
# VELOCIDAD_ENEMIGOS = 3
competidores = []

# Sistema de Vidas ***
vida_inicial = 3
pausa_invulnerable = 2000

# Puntuación y vida  *****
puntuacion = 0
vidas = vida_inicial
ultimo_toque = 0
invulnerable = False
font = pygame.font.Font(None, 36)   

# Puntuación 
puntuacion = 0
font = pygame.font.Font(None, 36)  

# Tiempo entre disparos
shoot_delay = 190
last_shot = 0

# Reloj
clock = pygame.time.Clock()

# Bucle principal
running = True
while running:
    current_time = pygame.time.get_ticks()#Tiempo actual en ms
    
    # Soltar proyectil
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and current_time - last_shot > shoot_delay:
                proyectiles.append(crear_proyectil(jugador.centerx, jugador.top))
                last_shot = current_time

    # Mover jugador
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and jugador.left > 0: 
        jugador.x -= 5 
    if keys[pygame.K_RIGHT] and jugador.right < ANCHO_VENTANA:
        jugador.x += 5  
    if keys[pygame.K_UP] and jugador.top > 0:
        jugador.y -= 5  
    if keys[pygame.K_DOWN] and jugador.bottom < ALTO_VENTANA:  
        jugador.y += 5  
        
    # Rivales 
    if len(competidores) < 5:    
        nuevo_competidor = {     
            "rect": pygame.Rect(
                random.randint(0, ANCHO_VENTANA - 30),
                -30,
                30,
                60
            ),
            "imagen": random.choice(autos_enemigos),
            "velocidad": random.randint(2, 5)
        }
        competidores.append(nuevo_competidor)  

    # Mover competidores
    for competidor in competidores[:]:
        competidor["rect"].y += competidor["velocidad"]
        if competidor["rect"].top > ALTO_VENTANA:
            competidores.remove(competidor)
            puntuacion += 1
            
    # Mover y dibujar proyectiles
    for proyectil in proyectiles[:]:
        mover_proyectil(proyectil)
        if proyectil["rect"].bottom < 0:
            proyectiles.remove(proyectil)

    # Colisiones
    for competidor in competidores[:]:
        if jugador.colliderect(competidor["rect"]) and not invulnerable:
            vidas -= 1
            ultimo_toque = current_time
            invulnerable = True
            competidores.remove(competidor)
            if vidas <= 0:
                running = False
                
        # Colisión con proyectiles
        for proyectil in proyectiles[:]:
            if competidor["rect"].colliderect(proyectil["rect"]):
                competidores.remove(competidor)
                proyectiles.remove(proyectil)
                puntuacion += 5  # Puntos por eliminar
                break
            
    # Actualizando estado de invulneraBilidad
    if invulnerable:
        if current_time - ultimo_toque > pausa_invulnerable:
            invulnerable = False
    
    # Dibujar 
    screen.fill(COLOR_01)
    
    # Efecto de invulnerabilidad (parpadeo de jugador)
    if not invulnerable or (current_time // 100) % 2 == 0:  # Parpadeo cada 200ms
        screen.blit(coche_max_5, jugador)  # Dibuja la imagen del coche
    pygame.draw.rect(screen, COLOR_DEBUG, jugador, 2)#rectángulo de debug
    
    # Dibujar competidores
    for competidor in competidores:
        screen.blit(competidor["imagen"], competidor["rect"])
        pygame.draw.rect(screen, (0, 255, 255), competidor["rect"], 1)
        
    # Dibujar proyectiles
    for proyectil in proyectiles:
        dibujar_proyectil(proyectil)
    
    # Mostrar puntuación 
    puntuacion_text = font.render(f"Puntuacion: {puntuacion}", True, COLOR_02)  #parámetros normales
    screen.blit(puntuacion_text, (10, 10))
    
    # Mostrar vidas restantes
    vida_text = font.render(f"Vidas: {vidas}", True, COLOR_02)  
    screen.blit(vida_text, (10, 30))
    
    pygame.display.flip()
    clock.tick(60)
    
# Pantalla "GAME OVER"
if vidas <= 0:
    game_over = True
    while game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = False
                pygame.quit()
                exit()  # Asegura que el juego se cierre correctamente
            if event.type == pygame.KEYDOWN:  
                if event.key == pygame.K_RETURN:  # Detecta ENTER
                    game_over = False
        
        # Fondo semitransparente
        s = pygame.Surface((ANCHO_VENTANA, ALTO_VENTANA))
        s.set_alpha(128)
        s.fill(COLOR_01) 
        screen.blit(s, (0, 0))
        
        # Texto "GAME OVER"
        game_over_font = pygame.font.Font(None, 74)
        game_over_text = game_over_font.render("GAME OVER", True, COLOR_03)
        game_over_rect = game_over_text.get_rect(center=(ANCHO_VENTANA/2, ALTO_VENTANA/3))
        screen.blit(game_over_text, game_over_rect)
        
        # Estadísticas
        stats_font = pygame.font.Font(None, 36)
        puntuacion_final = stats_font.render(f"Puntuación Final: {puntuacion}", True, COLOR_03)  
        screen.blit(puntuacion_final, (ANCHO_VENTANA/2 - puntuacion_final.get_width()/2, ALTO_VENTANA/2))
        
        # Texto "Presione ENTER para SALIR"
        enter_text = stats_font.render("Presione ENTER para SALIR", True, COLOR_04)
        enter_rect = enter_text.get_rect(center=(ANCHO_VENTANA/2, ALTO_VENTANA - 100))
        screen.blit(enter_text, enter_rect)
        
        pygame.display.flip()  # Actualiza la pantalla dentro del bucle
        clock.tick(60)

pygame.quit()
#probando