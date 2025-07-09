
def colision_jugador_enemigo(estado):
    if not estado["invulnerable"]:
        for competidor in estado["competidores"][:]:
            if estado["jugador"].colliderect(competidor["rect"]):
                estado["competidores"].remove(competidor)
                estado["vidas"] -= 1
                estado["invulnerable"] = True
                estado["ultimo_toque"] = estado["current_time"]
                break

    if estado["invulnerable"] and (estado["current_time"] - estado["ultimo_toque"]) > estado["pausa_invulnerable"]:
        estado["invulnerable"] = False

    return estado



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
                puntos += 5  # Puntos por eliminar
                break
    return puntos
