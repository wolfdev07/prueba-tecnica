"""
Dado el siguiente diccionario, que representa las calificaciones de un estudiante.
"""

ratings = {
    "cálculo vectorial": 85,
    "física": 90,
    "química": 88,
    "inglés": 92,
    "bases de datos": 78,
    "redes": 83,
    "economía":96, 
}

# Funcion que calcule su Promedio
def average(ratings):
    global_average = sum(ratings.values()) / len(ratings)
    return print(f"Average: {global_average}")

# Escribe una Funcion que imprima su tira de materias ordenada por calificacion de mandera Ascendente
def averages_list(ratings):
    ascending_list = sorted(ratings.items(), key=lambda item: item[1])
    for course, qualification in ascending_list:
        print(f"{course}: {qualification}")


averages_list(ratings)
average(ratings)