
def colision_jugador_enemigo(jugador, competidores, invulnerable, ultimo_toque,
                             pausa_invulnerable, current_time, vidas):
    """
    Maneja el choque jugador–enemigo, devuelve (vidas, invulnerable, ultimo_toque).
    """
    # Si no estoy en modo invulnerable, chequeo impacto
    if not invulnerable:
        for c in competidores[:]:
            if jugador.colliderect(c["rect"]):
                competidores.remove(c)
                vidas -= 1
                invulnerable = True
                ultimo_toque = current_time
                break

    # Chequeo fin de invulnerabilidad
    if invulnerable and (current_time - ultimo_toque) > pausa_invulnerable:
        invulnerable = False

    return vidas, invulnerable, ultimo_toque


def colision_proyectil_enemigo(proyectiles, competidores):
    """
    Maneja el choque proyectil–enemigo, devuelve puntos ganados.
    """
    puntos = 0
    for p in proyectiles[:]:
        for c in competidores[:]:
            if c["rect"].colliderect(p["rect"]):
                competidores.remove(c)
                proyectiles.remove(p)
                puntos += 5
                break
    return puntos
