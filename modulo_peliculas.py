"""
Agenda de peliculas.
Modulo de calculos basicos y reglas de negocio.
"""


def crear_pelicula(nombre: str, genero: str, duracion: int, anio: int,
                   clasificacion: str, hora: int, dia: str) -> dict:
    """Crea y devuelve un diccionario con los datos de una pelicula."""
    pelicula = {
        "nombre": str(nombre).strip(),
        "genero": str(genero).strip(),
        "duracion": int(duracion),
        "anio": int(anio),
        "clasificacion": str(clasificacion).strip(),
        "hora": int(hora),
        "dia": str(dia).strip()
    }
    return pelicula


def encontrar_pelicula(nombre_pelicula: str, p1: dict, p2: dict,
                       p3: dict, p4: dict, p5: dict) -> dict:
    """Busca una pelicula entre cinco diccionarios por su nombre."""
    if not nombre_pelicula:
        return None

    nombre_buscado = nombre_pelicula.strip().lower()
    peliculas = [p1, p2, p3, p4, p5]

    for p in peliculas:
        if p is not None and p.get("nombre", "").strip().lower() == nombre_buscado:
            return p
    return None


def encontrar_pelicula_mas_larga(p1: dict, p2: dict, p3: dict,
                                  p4: dict, p5: dict) -> dict:
    """Devuelve la pelicula de mayor duracion entre cinco peliculas."""
    peliculas = [p for p in (p1, p2, p3, p4, p5) if p is not None]
    if not peliculas:
        return None

    mas_larga = peliculas[0]
    for p in peliculas[1:]:
        if p["duracion"] > mas_larga["duracion"]:
            mas_larga = p

    return mas_larga


def duracion_promedio_peliculas(p1: dict, p2: dict, p3: dict,
                                p4: dict, p5: dict) -> str:
    """Devuelve la duracion promedio de las peliculas en formato HH:MM."""
    peliculas = [p for p in (p1, p2, p3, p4, p5) if p is not None]
    if not peliculas:
        return "00:00"

    duracion_total = sum(p["duracion"] for p in peliculas)
    promedio = round(duracion_total / len(peliculas))
    horas = promedio // 60
    minutos = promedio % 60
    return f"{horas:02d}:{minutos:02d}"


def encontrar_estrenos(p1: dict, p2: dict, p3: dict, p4: dict,
                       p5: dict, anio: int) -> str:
    """Devuelve los nombres de peliculas estrenadas despues del anio indicado."""
    peliculas = [p for p in (p1, p2, p3, p4, p5) if p is not None]
    nombres = [p["nombre"] for p in peliculas if p.get("anio", 0) > anio]

    if len(nombres) == 0:
        return "Ninguna"
    return ", ".join(nombres)


def cuantas_peliculas_18_mas(p1: dict, p2: dict, p3: dict,
                             p4: dict, p5: dict) -> int:
    """Cuenta peliculas con clasificacion 18+."""
    peliculas = [p for p in (p1, p2, p3, p4, p5) if p is not None]
    cantidad = sum(1 for p in peliculas if str(p.get("clasificacion", "")).strip() == "18+")
    return cantidad


def reagendar_pelicula(peli: dict, nueva_hora: int, nuevo_dia: str,
                       control_horario: bool, p1: dict, p2: dict,
                       p3: dict, p4: dict, p5: dict) -> bool:
    """Reagenda una pelicula si no hay conflicto de horario."""
    if peli is None:
        return False

    if nueva_hora < 0 or nueva_hora > 2359:
        return False

    if nueva_hora % 100 >= 60:
        return False

    if control_horario and (nueva_hora < 800 or nueva_hora > 2200):
        return False

    dia_limpio = nuevo_dia.strip().lower()
    peliculas = [p for p in (p1, p2, p3, p4, p5) if p is not None]

    for pelicula in peliculas:
        if pelicula != peli and pelicula.get("dia", "").strip().lower() == dia_limpio:
            if pelicula.get("hora") == nueva_hora:
                return False

    peli["hora"] = nueva_hora
    peli["dia"] = nuevo_dia.strip().capitalize()
    return True


def decidir_invitar(peli: dict, edad_invitado: int,
                    autorizacion_padres: bool) -> bool:
    """Comprueba si un invitado puede ver la pelicula segun edad, genero y autorizacion."""
    if peli is None:
        return False

    # Regla 1: Mayores de edad pueden ver cualquier pelicula
    if edad_invitado >= 18:
        return True

    genero_pelicula = peli.get("genero", "").lower()
    clasificacion = peli.get("clasificacion", "").strip()

    # Regla 2: Menores de 15 anos no pueden ver peliculas de Terror
    if edad_invitado < 15 and "terror" in genero_pelicula:
        return False

    # Regla 3: Menores de 10 anos o menos solo pueden ver peliculas Familiares
    if edad_invitado <= 10 and "familiar" not in genero_pelicula:
        return False

    # Regla 4: Validacion por clasificacion de edad y excepcion de Documental
    es_documental = "documental" in genero_pelicula

    if clasificacion == "Todos":
        return True
    elif clasificacion == "7+":
        return edad_invitado >= 7 or autorizacion_padres or es_documental
    elif clasificacion in ("12+", "13+"):
        return edad_invitado >= 12 or autorizacion_padres or es_documental
    elif clasificacion in ("15+", "16+"):
        return edad_invitado >= 15 or autorizacion_padres or es_documental
    elif clasificacion == "18+":
        return edad_invitado >= 18 or autorizacion_padres or es_documental

    return False
