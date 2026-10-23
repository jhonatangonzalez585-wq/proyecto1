"""
Agenda de peliculas.
Modulo de calculos basicos.
"""

def crear_pelicula(nombre: str, genero: str, duracion: int, anio: int,
                   clasificacion: str, hora: int, dia: str) -> dict:
    """Crea y devuelve un diccionario con los datos de una pelicula."""
    pelicula = {
        "nombre": nombre,
        "genero": genero,
        "duracion": duracion,
        "anio": anio,
        "clasificacion": clasificacion,
        "hora": hora,
        "dia": dia
    }
    return pelicula


def encontrar_pelicula(nombre_pelicula: str, p1: dict, p2: dict,
                       p3: dict, p4: dict, p5: dict) -> dict:
    """Busca una pelicula entre cinco diccionarios."""
    if p1["nombre"].lower() == nombre_pelicula.lower():
        return p1
    elif p2["nombre"].lower() == nombre_pelicula.lower():
        return p2
    elif p3["nombre"].lower() == nombre_pelicula.lower():
        return p3
    elif p4["nombre"].lower() == nombre_pelicula.lower():
        return p4
    elif p5["nombre"].lower() == nombre_pelicula.lower():
        return p5
    else:
        return None


def encontrar_pelicula_mas_larga(p1: dict, p2: dict, p3: dict,
                                  p4: dict, p5: dict) -> dict:
    """Devuelve la pelicula de mayor duracion entre cinco peliculas."""
    pelicula_mas_larga = p1

    if p2["duracion"] > pelicula_mas_larga["duracion"]:
        pelicula_mas_larga = p2
    if p3["duracion"] > pelicula_mas_larga["duracion"]:
        pelicula_mas_larga = p3
    if p4["duracion"] > pelicula_mas_larga["duracion"]:
        pelicula_mas_larga = p4
    if p5["duracion"] > pelicula_mas_larga["duracion"]:
        pelicula_mas_larga = p5

    return pelicula_mas_larga


def duracion_promedio_peliculas(p1: dict, p2: dict, p3: dict,
                                p4: dict, p5: dict) -> str:
    """Devuelve la duracion promedio en formato HH:MM."""
    duracion_total = (
        p1["duracion"] + p2["duracion"] + p3["duracion"] +
        p4["duracion"] + p5["duracion"]
    )
    promedio = duracion_total // 5
    horas = promedio // 60
    minutos = promedio % 60
    return str(horas).zfill(2) + ":" + str(minutos).zfill(2)


def encontrar_estrenos(p1: dict, p2: dict, p3: dict, p4: dict,
                       p5: dict, anio: int) -> str:
    """Devuelve los nombres de peliculas estrenadas despues del anio indicado."""
    peliculas = [p1, p2, p3, p4, p5]
    nombres = []

    for pelicula in peliculas:
        if pelicula["anio"] > anio:
            nombres.append(pelicula["nombre"])

    if len(nombres) == 0:
        return "Ninguna"
    return ", ".join(nombres)


def cuantas_peliculas_18_mas(p1: dict, p2: dict, p3: dict,
                             p4: dict, p5: dict) -> int:
    """Cuenta peliculas con clasificacion 18+."""
    peliculas = [p1, p2, p3, p4, p5]
    cantidad = 0

    for pelicula in peliculas:
        if pelicula["clasificacion"] == "18+":
            cantidad += 1

    return cantidad


def reagendar_pelicula(peli: dict, nueva_hora: int, nuevo_dia: str,
                       control_horario: bool, p1: dict, p2: dict,
                       p3: dict, p4: dict, p5: dict) -> bool:
    """Reagenda una pelicula si no hay conflicto de horario."""
    if nueva_hora < 0 or nueva_hora > 2359:
        return False

    if nueva_hora % 100 >= 60:
        return False

    peliculas = [p1, p2, p3, p4, p5]

    for pelicula in peliculas:
        if pelicula != peli and pelicula["dia"].lower() == nuevo_dia.lower():
            if pelicula["hora"] == nueva_hora:
                return False

    if control_horario and (nueva_hora < 800 or nueva_hora > 2200):
        return False

    peli["hora"] = nueva_hora
    peli["dia"] = nuevo_dia
    return True


def decidir_invitar(peli: dict, edad_invitado: int,
                    autorizacion_padres: bool) -> bool:
    """Comprueba si la edad permite ver la pelicula."""
    clasificacion = peli["clasificacion"]

    if clasificacion == "Todos":
        return True
    elif clasificacion == "7+":
        return edad_invitado >= 7
    elif clasificacion == "12+":
        return edad_invitado >= 12
    elif clasificacion == "15+":
        return edad_invitado >= 15
    elif clasificacion == "18+":
        return edad_invitado >= 18 or autorizacion_padres

    return False
