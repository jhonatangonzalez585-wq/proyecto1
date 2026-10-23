from modulo_peliculas import crear_pelicula

archivo = open("datos_peliculas.txt", "r", encoding="utf-8")
peliculas = []

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

print("PELICULAS CARGADAS")
print("-------------------")

for pelicula in peliculas:
    print(pelicula["nombre"])

print("-------------------")
print("Total de peliculas:", len(peliculas))
