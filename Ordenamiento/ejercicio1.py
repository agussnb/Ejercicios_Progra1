# Dadas las siguientes listas:
# Nombres =
# ["Ana","Luis","Juan","Sol","Roberto","Sonia","Ulises","Sofia","Maria","Pedro","Anto
# nio", "Eugenia", "Soledad", "Mario", "Mariela"]
# Edades = [23,45,34,23,46,23,45,67,37,68,25,55,45,27,43]
# Desarrollar una función que realice el ordenamiento de las listas por nombre de 
# manera ascendente.
def ordenar_listas_por_nombre(nombres, edades):
    for i in range(len(nombres) - 1):
        for j in range(len(nombres) - 1 - i):
            if nombres[j] > nombres[j + 1]:
                nombres[j], nombres[j + 1] = nombres[j + 1], nombres[j]
                edades[j], edades[j + 1] = edades[j + 1], edades[j]


Nombres = ["Ana", "Luis", "Juan", "Sol", "Roberto", "Sonia", "Ulises", "Sofia", "Maria", "Pedro", "Antonio", "Eugenia", "Soledad", "Mario", "Mariela"]
Edades = [23, 45, 34, 23, 46, 23, 45, 67, 37, 68, 25, 55, 45, 27, 43]

ordenar_listas_por_nombre(Nombres, Edades)

print("Nombres ordenados:", Nombres)
print("Edades correspondientes:", Edades)
