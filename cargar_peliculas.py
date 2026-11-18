import os
from modulo_peliculas import crear_pelicula

ruta_archivo = os.path.join(os.path.dirname(__file__), "datos_peliculas.txt")

peliculas = []
with open(ruta_archivo, "r", encoding="utf-8") as archivo:
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

print("PELICULAS CARGADAS")
print("-------------------")

for pelicula in peliculas:
    print(pelicula["nombre"])

print("-------------------")
print("Total de peliculas:", len(peliculas))
