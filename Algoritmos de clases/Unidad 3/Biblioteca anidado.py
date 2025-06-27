"""
Ejercicio: Biblioteca con diccionario anidado
Crea un diccionario vacío llamado biblioteca. Agrega 3 libros al diccionario. La clave será el título del libro y el valor será 
otro diccionario con la siguiente información:
Autor
Año de publicación
Género literario
Los libros son:

"Don Quijote":
Autor: "Miguel de Cervantes"
Año: 1605
Género: "Novela"
"La Odisea":
Autor: "Homero"
Año: -800
Género: "Épica"
"1984":
Autor: "George Orwell"
Año: 1949
Género: "Distopía"
Imprime el diccionario completo.
Imprime solo el año de publicación de "1984".
Cambia el género de "La Odisea" a "Poesía Épica".
Imprime nuevamente el diccionario para ver los cambios
"""

biblioteca = {}

biblioteca["Don quijote"] = {"Autor": "Miguel de Cervantes",
                             "Año": 1605,
                             "Genero": "Novela"}

biblioteca["La Odisea"] = {"Autor": "Homero",
                           "Año": -800,
                           "Genero": "Épica"}

biblioteca["1984"] = {"Autor": "George Orwell",
                      "Año": 1949,
                      "Genero": "Distopía"}
#Ejercicio 1
print(biblioteca)
#Ejercicio 2
print (biblioteca["1984"]["Año"])
#Ejercicio 3
biblioteca["1984"]["Año"] = 2025
print (biblioteca["1984"]["Año"])
#Ejercicio 4
print (biblioteca)
