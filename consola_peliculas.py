"""
Agenda de peliculas.
Modulo de consola: permite usar las funciones desde un menu sencillo.
"""

from modulo_peliculas import (
    crear_pelicula,
    encontrar_pelicula,
    encontrar_pelicula_mas_larga,
    duracion_promedio_peliculas
)


def cargar_peliculas():
    """Lee las peliculas guardadas en datos_peliculas.txt."""
    peliculas = []
    archivo = open("datos_peliculas.txt", "r", encoding="utf-8")

    for linea in archivo:
        datos = linea.strip().split("|")

        if len(datos) == 7:
            pelicula = crear_pelicula(
                datos[0],
                datos[1],
                int(datos[2]),
                int(datos[3]),
                datos[4],
                int(datos[5]),
                datos[6]
            )
            peliculas.append(pelicula)

    archivo.close()
    return peliculas


def mostrar_pelicula(pelicula):
    """Muestra los datos de una pelicula."""
    print("Nombre:", pelicula["nombre"])
    print("Genero:", pelicula["genero"])
    print("Duracion:", pelicula["duracion"], "minutos")
    print("Anio:", pelicula["anio"])
    print("Clasificacion:", pelicula["clasificacion"])
    print("Hora:", pelicula["hora"])
    print("Dia:", pelicula["dia"])


def main():
    peliculas = cargar_peliculas()

    if len(peliculas) == 0:
        print("No se cargaron peliculas. Revisa datos_peliculas.txt.")
        return

    opcion = ""

    while opcion != "5":
        print()
        print("===== AGENDA DE PELICULAS =====")
        print("1. Mostrar todas las peliculas")
        print("2. Encontrar una pelicula")
        print("3. Encontrar la pelicula mas larga")
        print("4. Calcular duracion promedio")
        print("5. Salir")

        opcion = input("Elige una opcion: ")

        if opcion == "1":
            for pelicula in peliculas:
                print("--------------------")
                mostrar_pelicula(pelicula)

        elif opcion == "2":
            nombre = input("Escribe el nombre de la pelicula: ")
            encontrada = None

            for pelicula in peliculas:
                if pelicula["nombre"].lower() == nombre.lower():
                    encontrada = pelicula

            if encontrada is not None:
                print("Pelicula encontrada:")
                mostrar_pelicula(encontrada)
            else:
                print("No se encontro esa pelicula.")

        elif opcion == "3":
            mas_larga = peliculas[0]

            for pelicula in peliculas:
                if pelicula["duracion"] > mas_larga["duracion"]:
                    mas_larga = pelicula

            print("La pelicula mas larga es:")
            mostrar_pelicula(mas_larga)

        elif opcion == "4":
            total = 0

            for pelicula in peliculas:
                total = total + pelicula["duracion"]

            promedio = total // len(peliculas)
            horas = promedio // 60
            minutos = promedio % 60

            print("Duracion promedio:", str(horas).zfill(2) + ":" + str(minutos).zfill(2))

        elif opcion == "5":
            print("Hasta luego.")

        else:
            print("Opcion no valida. Intenta de nuevo.")


if __name__ == "__main__":
    main()
