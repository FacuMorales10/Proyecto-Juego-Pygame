def colision_jugador_enemigo(jugador,
                            competidores,
                            invulnerable,
                            ultimo_toque,
                            pausa_invulnerable,
                            current_time,
                            vidas):
    """
    Maneja el choque jugador-enemigo, devuelve (vidas, invulnerable, ultimo_toque).
    """
    # Si no estoy en modo invulnerable, chequeo impacto
    if not invulnerable:
        for competidor in competidores[:]:
            if jugador.colliderect(competidor["rect"]):
                competidores.remove(competidor)
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
    Maneja el choque proyectil-enemigo, devuelve puntos ganados.
    """
    puntos = 0
    for proyectil in proyectiles[:]:
        for competidor in competidores[:]:
            if competidor["rect"].colliderect(proyectil["rect"]):
                competidores.remove(competidor)
                proyectiles.remove(proyectil)
                puntos += 5
                break
    return puntos

