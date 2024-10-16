# Dadas las siguientes listas:
# Nombres = ["Matematica","Investigacion Operativa","Ingles","Literatura","Ciencias 
# Sociales","Computacion","Ingles","Algebra","Contabilidad","Artistica", "Algoritmos", 
# "Base de Datos", "Ergonomia", "Naturaleza"]
# Puntos = [100,98,56,25,87,38,64,42,28,91,66,35,49,57,98]
# Desarrollar una función que realice el ordenamiento de las listas por nombre de 
# manera ascendente, si el nombre es el mismo, debe ordenar por puntos de manera 
# descendente.

def ordenar_listas_por_nombre_y_puntos(nombres, puntos):
    for i in range(len(nombres) - 1):
        for j in range(len(nombres) - 1 - i):
            if nombres[j] > nombres[j + 1]:
                nombres[j], nombres[j + 1] = nombres[j + 1], nombres[j]
                puntos[j], puntos[j + 1] = puntos[j + 1], puntos[j]
            elif nombres[j] == nombres[j + 1] and puntos[j] < puntos[j + 1]:
                puntos[j], puntos[j + 1] = puntos[j + 1], puntos[j]


Nombres = ["Matematica", "Investigacion Operativa", "Ingles", "Literatura", "Ciencias Sociales", "Computacion", 
           "Ingles", "Algebra", "Contabilidad", "Artistica", "Algoritmos", "Base de Datos", "Ergonomia", "Naturaleza"]
Puntos = [100, 98, 56, 25, 87, 38, 64, 42, 28, 91, 66, 35, 49, 57, 98]

ordenar_listas_por_nombre_y_puntos(Nombres, Puntos)

print("Nombres ordenados:", Nombres)
print("Puntos correspondientes:", Puntos)
