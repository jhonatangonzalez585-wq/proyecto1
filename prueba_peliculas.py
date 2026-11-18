"""
Pruebas integrales de la Agenda de Peliculas.
Verifica las funciones de modulo_peliculas.py.
"""

from modulo_peliculas import (
    crear_pelicula,
    encontrar_pelicula,
    encontrar_pelicula_mas_larga,
    duracion_promedio_peliculas,
    encontrar_estrenos,
    cuantas_peliculas_18_mas,
    reagendar_pelicula,
    decidir_invitar
)

print("========================================")
print("     PRUEBAS: MODULO PELICULAS          ")
print("========================================")

# 1. Prueba: crear_pelicula
p1 = crear_pelicula("Toy Story", "Animacion,Familiar", 81, 1995, "Todos", 1400, "Lunes")
p2 = crear_pelicula("Titanic", "Drama,Romance", 195, 1997, "12+", 1600, "Martes")
p3 = crear_pelicula("Avatar", "Ciencia ficcion,Accion", 162, 2009, "12+", 1800, "Miercoles")
p4 = crear_pelicula("El Conjuro", "Terror", 112, 2013, "15+", 2100, "Jueves")
p5 = crear_pelicula("Planeta Tierra", "Documental", 90, 2016, "18+", 1900, "Viernes")

print("\n[1] Prueba crear_pelicula:")
print("  Pelicula 1 creada:", p1["nombre"], f"({p1['duracion']} min)")
print("  Pelicula 4 creada:", p4["nombre"], f"({p4['genero']})")
assert p1["nombre"] == "Toy Story"
assert p1["duracion"] == 81

# 2. Prueba: encontrar_pelicula
print("\n[2] Prueba encontrar_pelicula:")
buscada = encontrar_pelicula("titanic", p1, p2, p3, p4, p5)
assert buscada is not None and buscada["nombre"] == "Titanic"
print("  'titanic' encontrada correctamente:", buscada["nombre"])

no_existe = encontrar_pelicula("Pelicula Inexistente", p1, p2, p3, p4, p5)
assert no_existe is None
print("  Busqueda de inexistente retorno None correctamente.")

# 3. Prueba: encontrar_pelicula_mas_larga
print("\n[3] Prueba encontrar_pelicula_mas_larga:")
larga = encontrar_pelicula_mas_larga(p1, p2, p3, p4, p5)
assert larga["nombre"] == "Titanic"
assert larga["duracion"] == 195
print("  Pelicula mas larga:", larga["nombre"], f"con {larga['duracion']} minutos.")

# 4. Prueba: duracion_promedio_peliculas
print("\n[4] Prueba duracion_promedio_peliculas:")
promedio = duracion_promedio_peliculas(p1, p2, p3, p4, p5)
# Duraciones: 81 + 195 + 162 + 112 + 90 = 640. 640 / 5 = 128 minutos = 02:08
assert promedio == "02:08"
print("  Duracion promedio calculada:", promedio, "(Esperado: 02:08)")

# 5. Prueba: encontrar_estrenos
print("\n[5] Prueba encontrar_estrenos:")
estrenos_2000 = encontrar_estrenos(p1, p2, p3, p4, p5, 2000)
print("  Estrenos despues del anio 2000:", estrenos_2000)
assert "Avatar" in estrenos_2000 and "El Conjuro" in estrenos_2000

# 6. Prueba: cuantas_peliculas_18_mas
print("\n[6] Prueba cuantas_peliculas_18_mas:")
cant_18 = cuantas_peliculas_18_mas(p1, p2, p3, p4, p5)
print("  Cantidad de peliculas 18+:", cant_18)
assert cant_18 == 1

# 7. Prueba: reagendar_pelicula
print("\n[7] Prueba reagendar_pelicula:")
# Reagendar a horario valido sin conflicto
exito_ok = reagendar_pelicula(p1, 1000, "Sabado", True, p1, p2, p3, p4, p5)
assert exito_ok is True
assert p1["hora"] == 1000 and p1["dia"] == "Sabado"
print("  Reagendado exitoso a Sabado 10:00.")

# Conflicto: misma hora y dia que p2 (Martes a las 1600)
exito_conflicto = reagendar_pelicula(p1, 1600, "Martes", True, p1, p2, p3, p4, p5)
assert exito_conflicto is False
print("  Conflicto detectado correctamente al intentar chocar con Titanic.")

# Horario fuera de rango con control horario (2300 hrs)
exito_fuera_rango = reagendar_pelicula(p1, 2300, "Domingo", True, p1, p2, p3, p4, p5)
assert exito_fuera_rango is False
print("  Control de horario (fuera de 08:00 - 22:00) detectado correctamente.")

# 8. Prueba: decidir_invitar
print("\n[8] Prueba decidir_invitar:")
# Caso a: Mayor de edad (>=18) siempre puede
assert decidir_invitar(p4, 20, False) is True
print("  Adulto de 20 anos puede ver El Conjuro (Terror 15+): OK")

# Caso b: Menor de 15 anos NO puede ver Terror, aun con autorizacion
assert decidir_invitar(p4, 14, True) is False
print("  Menor de 14 anos NO puede ver Terror aun con autorizacion: OK")

# Caso c: Menor de 10 anos o menos SOLO puede ver genero Familiar
assert decidir_invitar(p1, 8, False) is True
assert decidir_invitar(p2, 8, True) is False  # Titanic no es Familiar
print("  Nino de 8 anos solo puede ver peliculas con genero Familiar: OK")

# Caso d: Excepcion documental (Planeta Tierra es 18+ Documental, invitado de 16 sin autorizacion puede verla)
assert decidir_invitar(p5, 16, False) is True
print("  Excepcion de genero Documental aplicada correctamente: OK")

print("\n========================================")
print("¡TODAS LAS PRUEBAS PASARON EXITOSAMENTE!")
print("========================================")
