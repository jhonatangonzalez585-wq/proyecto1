from modulo_peliculas import (
    crear_pelicula,
    encontrar_pelicula,
    encontrar_pelicula_mas_larga,
    duracion_promedio_peliculas
)

p1 = crear_pelicula("Toy Story", "Animacion", 81, 1995, "Todos", 1400, "Lunes")
p2 = crear_pelicula("Titanic", "Drama", 195, 1997, "12+", 1600, "Martes")
p3 = crear_pelicula("Avatar", "Ciencia ficcion", 162, 2009, "12+", 1800, "Miercoles")
p4 = crear_pelicula("Coco", "Animacion", 105, 2017, "Todos", 1500, "Jueves")
p5 = crear_pelicula("Interestelar", "Ciencia ficcion", 169, 2014, "12+", 1900, "Viernes")

buscada = encontrar_pelicula("Titanic", p1, p2, p3, p4, p5)
if buscada is not None:
    print("Pelicula encontrada:", buscada["nombre"])
else:
    print("Pelicula no encontrada")

larga = encontrar_pelicula_mas_larga(p1, p2, p3, p4, p5)
print("Pelicula mas larga:", larga["nombre"])
print("Duracion:", larga["duracion"], "minutos")

promedio = duracion_promedio_peliculas(p1, p2, p3, p4, p5)
print("Duracion promedio:", promedio)
