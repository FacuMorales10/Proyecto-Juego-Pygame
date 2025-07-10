# 🚗 Mach-Max - TP Programación 1 UTN FRA

## 🎮 Descripción

**Mach-Max** es un juego arcade de desplazamiento vertical desarrollado con **Python y Pygame**. El jugador controla un auto supersónico que esquiva y destruye competidores en una autopista infinita. Usando sierras giratorias como proyectiles, debe sobrevivir el mayor tiempo posible mientras suma puntos.

---

## 🧠 Equipo de Desarrollo

### 👨‍💻 Alumno 1 – Motor & Estados (Lead Programmer)
- **Tareas:**
  - Configuración del proyecto y estructura de carpetas
  - Bucle principal (`main.py`)
  - Control de estados (pausa, game over, menú)
  - Integración de módulos
- **Email:** [colocar email]
- **GitHub:** [colocar GitHub]

### 🎮 Alumno 2 – Jugabilidad & Balance (Gameplay Designer)
- **Tareas:**
  - Lógica del jugador (`player.py`), enemigos (`enemies.py`) y proyectiles (`projectiles.py`)
  - Sistema de dificultad y oleadas
  - Power-ups
  - Sistema de puntuación y balance de juego
- **Email:** [colocar email]
- **GitHub:** [colocar GitHub]

### 🎨 Alumno 3 – Arte, UI & Audio (UX Engineer)
- **Tareas:**
  - Organización y carga de assets (`assets/`)
  - Interfaces: menú, pausa, game over (`screens/`)
  - Efectos visuales y sonoros
  - Feedback visual (parpadeo, explosiones, textos)
- **Email:** [colocar email]
- **GitHub:** [colocar GitHub]

### 🧪 Alumno 4 – Persistencia & QA (Data Engineer)
- **Tareas:**
  - Guardado y carga de puntajes (`ranking.py`)
  - Validación de datos
  - Pruebas de funcionalidades (colisiones, puntuación, archivo)
  - Documentación y empaquetado final
- **Email:** [colocar email]
- **GitHub:** [colocar GitHub]

---

## 📁 Estructura del Proyecto

Proyecto-Juego-Pygame/
├── assets/ # Recursos visuales y de audio
│
├── screens/ # Pantallas del juego
│ ├── gameover.py # Pantalla de Game Over
│ ├── menu.py # Menú principal
│ ├── pause.py # Pantalla de pausa
│
├── collisions.py # Sistema de colisiones
├── enemies.py # Lógica de enemigos
├── hud.py # Heads-Up Display (vidas, puntos)
├── intro.py # Intro del juego
├── juego.py # Lógica de juego (si aplica)
├── main.py # Punto de entrada principal
├── player.py # Lógica del jugador
├── projectiles.py # Lógica de proyectiles
├── ranking.py # Guardado y carga de puntajes
├── settings.py # Configuraciones generales
├── utils.py # Funciones utilitarias
└── README.md # Este archivo

## 🕹️ Controles

- **← / → / ↑ / ↓** - Movimiento del auto
- **ESPACIO** - Disparar sierras
- **P** - Pausar / Reanudar juego
- **ESC** - Salir desde pantalla de Game Over
- **ENTER** - Salir desde pantalla de Game Over

---

## 📦 Requisitos

- Python 3.8 o superior
- pygame >= 2.0

---

## ⚙️ Instalación y Ejecución

```bash
git clone https://github.com/usuario/proyecto-juego-pygame.git
cd proyecto-juego-pygame
pip install pygame
python main.py

🎯 Características Implementadas
 Movimiento libre del jugador

 Sistema de enemigos con spawn progresivo

 Disparo de proyectiles

 Detección de colisiones

 Sistema de vidas e invulnerabilidad

 Sistema de puntuación

 Pantalla de pausa

 Pantalla de game over

 Guardado de puntajes

 Modularización completa

 Control por teclado

 Integración de imágenes y sonidos

📞 Información Académica
Universidad: UTN - Facultad Regional Avellaneda

Materia: Programación 1

Año: 2025

Profesores: Enzo Zotti / Lucas Ferrini

Comisión: 

Entrega: Trabajo Práctico Final - Juego Arcade

⚖️ Licencia
Este proyecto fue desarrollado con fines exclusivamente educativos para el curso de Programación 1 - UTN FRA.

🏁 Créditos Finales
Gracias a todo el equipo por la colaboración, compromiso y aprendizaje compartido. ¡Que empiece el juego! 🎮