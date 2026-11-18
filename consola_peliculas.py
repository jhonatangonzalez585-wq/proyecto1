"""
Agenda de peliculas.
Modulo de consola: interfaz de usuario que interactua con el usuario
y delega la logica en modulo_peliculas.
"""

import os
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


def cargar_peliculas():
    """Lee las primeras cinco peliculas de datos_peliculas.txt."""
    ruta_archivo = os.path.join(os.path.dirname(__file__), "datos_peliculas.txt")
    peliculas = []

    if os.path.exists(ruta_archivo):
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                datos = linea.strip().split("|")
                if len(datos) == 7:
                    p = crear_pelicula(
                        datos[0],
                        datos[1],
                        int(datos[2]),
                        int(datos[3]),
                        datos[4],
                        int(datos[5]),
                        datos[6]
                    )
                    peliculas.append(p)
                if len(peliculas) == 5:
                    break

    # Asegurar que siempre tengamos 5 variables (si faltan, se completan como None)
    while len(peliculas) < 5:
        peliculas.append(None)

    return peliculas[0], peliculas[1], peliculas[2], peliculas[3], peliculas[4]


def mostrar_pelicula(pelicula: dict):
    """Muestra los datos formateados de una pelicula."""
    if pelicula is None:
        print("Espacio vacio en la agenda (sin pelicula asignada).")
        return

    print(f"  Nombre:        {pelicula.get('nombre')}")
    print(f"  Genero:        {pelicula.get('genero')}")
    print(f"  Duracion:      {pelicula.get('duracion')} minutos")
    print(f"  Anio:          {pelicula.get('anio')}")
    print(f"  Clasificacion: {pelicula.get('clasificacion')}")
    print(f"  Hora:          {pelicula.get('hora'):04d} hrs")
    print(f"  Dia:           {pelicula.get('dia')}")


def mostrar_todas_las_peliculas(p1, p2, p3, p4, p5):
    """Muestra todas las peliculas cargadas en la agenda."""
    peliculas = [("Pelicula 1", p1), ("Pelicula 2", p2),
                 ("Pelicula 3", p3), ("Pelicula 4", p4),
                 ("Pelicula 5", p5)]

    print("\n--- PELICULAS EN LA AGENDA ---")
    for etiqueta, p in peliculas:
        print(f"\n[{etiqueta}]")
        mostrar_pelicula(p)


def ejecutar_crear_pelicula(p1, p2, p3, p4, p5):
    """Solicita los datos al usuario y crea una pelicula en la posicion elegida."""
    print("\n--- CREAR / AGREGAR PELICULA ---")
    nombre = input("Nombre de la pelicula: ").strip()
    genero = input("Genero (ej. Animacion, Drama, Terror, Familiar, etc.): ").strip()

    try:
        duracion = int(input("Duracion en minutos (ej. 120): ").strip())
        anio = int(input("Anio de estreno (ej. 2020): ").strip())
    except ValueError:
        print("Error: La duracion y el anio deben ser numeros enteros.")
        return p1, p2, p3, p4, p5

    clasificacion = input("Clasificacion (Todos, 7+, 12+, 15+, 18+): ").strip()

    try:
        hora = int(input("Hora militar (ej. 1400 para 2:00 PM): ").strip())
    except ValueError:
        print("Error: La hora debe ser un numero entero (ej. 1600).")
        return p1, p2, p3, p4, p5

    dia = input("Dia de la semana (ej. Lunes, Martes, etc.): ").strip()

    nueva = crear_pelicula(nombre, genero, duracion, anio, clasificacion, hora, dia)

    print("\nEn que posicion de la agenda desea guardarla? (1 a 5)")
    pos = input("Elige posicion [1-5]: ").strip()

    if pos == "1":
        p1 = nueva
    elif pos == "2":
        p2 = nueva
    elif pos == "3":
        p3 = nueva
    elif pos == "4":
        p4 = nueva
    elif pos == "5":
        p5 = nueva
    else:
        print("Posicion no valida. No se guardo la pelicula.")
        return p1, p2, p3, p4, p5

    print(f"\n¡Pelicula '{nombre}' creada y guardada con exito en la posicion {pos}!")
    return p1, p2, p3, p4, p5


def ejecutar_encontrar_pelicula(p1, p2, p3, p4, p5):
    """Busca una pelicula usando la funcion del modulo."""
    print("\n--- BUSCAR PELICULA ---")
    nombre = input("Escribe el nombre de la pelicula a buscar: ").strip()
    encontrada = encontrar_pelicula(nombre, p1, p2, p3, p4, p5)

    if encontrada is not None:
        print("\n¡Pelicula encontrada!")
        mostrar_pelicula(encontrada)
    else:
        print(f"\nNo se encontro ninguna pelicula con el nombre '{nombre}'.")


def ejecutar_encontrar_pelicula_mas_larga(p1, p2, p3, p4, p5):
    """Encuentra y muestra la pelicula con mayor duracion."""
    print("\n--- PELICULA MAS LARGA ---")
    mas_larga = encontrar_pelicula_mas_larga(p1, p2, p3, p4, p5)

    if mas_larga is not None:
        print("La pelicula con mayor duracion es:")
        mostrar_pelicula(mas_larga)
    else:
        print("No hay peliculas en la agenda.")


def ejecutar_duracion_promedio(p1, p2, p3, p4, p5):
    """Calcula y muestra la duracion promedio en formato HH:MM."""
    print("\n--- DURACION PROMEDIO ---")
    promedio = duracion_promedio_peliculas(p1, p2, p3, p4, p5)
    print(f"La duracion promedio de las peliculas es: {promedio} (HH:MM)")


def ejecutar_encontrar_estrenos(p1, p2, p3, p4, p5):
    """Muestra los estrenos posteriores a un anio dado."""
    print("\n--- BUSCAR ESTRENOS ---")
    try:
        anio = int(input("Ingresa el anio de referencia: ").strip())
    except ValueError:
        print("Error: El anio debe ser un numero entero.")
        return

    estrenos = encontrar_estrenos(p1, p2, p3, p4, p5, anio)
    print(f"Peliculas estrenadas despues del anio {anio}: {estrenos}")


def ejecutar_cuantas_18_mas(p1, p2, p3, p4, p5):
    """Muestra cuantas peliculas son para mayores de 18 anos."""
    print("\n--- PELICULAS 18+ ---")
    cantidad = cuantas_peliculas_18_mas(p1, p2, p3, p4, p5)
    print(f"Cantidad de peliculas con clasificacion 18+: {cantidad}")


def ejecutar_reagendar_pelicula(p1, p2, p3, p4, p5):
    """Reagenda el horario de una pelicula existente."""
    print("\n--- REAGENDAR PELICULA ---")
    nombre = input("Nombre de la pelicula a reagendar: ").strip()
    pelicula = encontrar_pelicula(nombre, p1, p2, p3, p4, p5)

    if pelicula is None:
        print(f"No se encontro la pelicula '{nombre}'.")
        return

    try:
        nueva_hora = int(input("Nueva hora militar (ej. 1500): ").strip())
    except ValueError:
        print("Error: La hora debe ser un numero entero.")
        return

    nuevo_dia = input("Nuevo dia (ej. Sabado): ").strip()
    control_str = input("Aplicar control de horario (8:00 a 22:00)? (s/n): ").strip().lower()
    control_horario = control_str in ("s", "si", "yes", "y", "true")

    exito = reagendar_pelicula(pelicula, nueva_hora, nuevo_dia, control_horario, p1, p2, p3, p4, p5)

    if exito:
        print(f"¡Pelicula '{nombre}' reagendada exitosamente al dia {nuevo_dia} a las {nueva_hora:04d} hrs!")
    else:
        print("No fue posible reagendar la pelicula (conflicto de horario o datos invalidos).")


def ejecutar_decidir_invitar(p1, p2, p3, p4, p5):
    """Evalua si se puede invitar a una persona a ver una pelicula."""
    print("\n--- DECIDIR INVITAR ---")
    nombre = input("Nombre de la pelicula: ").strip()
    pelicula = encontrar_pelicula(nombre, p1, p2, p3, p4, p5)

    if pelicula is None:
        print(f"No se encontro la pelicula '{nombre}' en la agenda.")
        return

    try:
        edad = int(input("Edad del invitado: ").strip())
    except ValueError:
        print("Error: La edad debe ser un numero entero.")
        return

    auth_str = input("¿Cuenta con autorizacion de los padres? (s/n): ").strip().lower()
    autorizacion = auth_str in ("s", "si", "yes", "y", "true")

    puede_invitar = decidir_invitar(pelicula, edad, autorizacion)

    if puede_invitar:
        print(f"-> ¡SI es posible invitar a la persona a ver '{pelicula['nombre']}'!")
    else:
        print(f"-> NO es posible invitar a la persona a ver '{pelicula['nombre']}' (no cumple las restricciones).")


def main():
    p1, p2, p3, p4, p5 = cargar_peliculas()

    opcion = ""

    while opcion != "10":
        print("\n========================================")
        print("         AGENDA DE PELICULAS            ")
        print("========================================")
        print("1.  Mostrar todas las peliculas")
        print("2.  Crear / Agregar una pelicula")
        print("3.  Encontrar una pelicula")
        print("4.  Encontrar la pelicula mas larga")
        print("5.  Calcular duracion promedio de peliculas")
        print("6.  Encontrar estrenos posteriores a un anio")
        print("7.  Contar peliculas para mayores de 18 anos")
        print("8.  Reagendar una pelicula")
        print("9.  Decidir invitar a una persona")
        print("10. Salir")
        print("========================================")

        opcion = input("Elige una opcion [1-10]: ").strip()

        if opcion == "1":
            mostrar_todas_las_peliculas(p1, p2, p3, p4, p5)
        elif opcion == "2":
            p1, p2, p3, p4, p5 = ejecutar_crear_pelicula(p1, p2, p3, p4, p5)
        elif opcion == "3":
            ejecutar_encontrar_pelicula(p1, p2, p3, p4, p5)
        elif opcion == "4":
            ejecutar_encontrar_pelicula_mas_larga(p1, p2, p3, p4, p5)
        elif opcion == "5":
            ejecutar_duracion_promedio(p1, p2, p3, p4, p5)
        elif opcion == "6":
            ejecutar_encontrar_estrenos(p1, p2, p3, p4, p5)
        elif opcion == "7":
            ejecutar_cuantas_18_mas(p1, p2, p3, p4, p5)
        elif opcion == "8":
            ejecutar_reagendar_pelicula(p1, p2, p3, p4, p5)
        elif opcion == "9":
            ejecutar_decidir_invitar(p1, p2, p3, p4, p5)
        elif opcion == "10":
            print("\n¡Gracias por usar la Agenda de Peliculas! Hasta luego.")
        else:
            print("\nOpcion no valida. Por favor elige un numero del 1 al 10.")


if __name__ == "__main__":
    main()
