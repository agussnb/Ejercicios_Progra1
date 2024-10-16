# Dadas las siguientes listas:
# Estudiantes =
# ["Ana","Luis","Juan","Sol","Roberto","Sonia","María","Sofia","Maria","Pedro","Anto
# nio", "Eugenia", "Soledad", "Mario", "María"]
# Apellidos = 
# [“Sosa”,”Gutierrez”,”Alsina”,”Martinez”,”Sosa”,”Ramirez”,”Perez”,”Lopez”,”Arregui”
# ,”Mitre”,”Andrade”,”Loza”,”Antares”,”Roca”,”Perez”]
# Nota = [8,4,9,10,8,6,4,8,7,5,6,7,10,4,8]
# Desarrollar una función que realice el ordenamiento de las listas por apellido de 
# manera ascendente, si el apellido es el mismo, debe ordenar por nombre de manera 
# ascendente, si el nombre también es el mismo, debe ordenar por nota de manera 
# descendente.

def ordenar_listas_por_apellido_nombre_nota(estudiantes, apellidos, notas):
    for i in range(len(apellidos) - 1):
        for j in range(len(apellidos) - 1 - i):
            if apellidos[j] > apellidos[j + 1]:
                apellidos[j], apellidos[j + 1] = apellidos[j + 1], apellidos[j]
                estudiantes[j], estudiantes[j + 1] = estudiantes[j + 1], estudiantes[j]
                notas[j], notas[j + 1] = notas[j + 1], notas[j]
            elif apellidos[j] == apellidos[j + 1] and estudiantes[j] > estudiantes[j + 1]:
                estudiantes[j], estudiantes[j + 1] = estudiantes[j + 1], estudiantes[j]
                notas[j], notas[j + 1] = notas[j + 1], notas[j]
            elif apellidos[j] == apellidos[j + 1] and estudiantes[j] == estudiantes[j + 1] and notas[j] < notas[j + 1]:
                notas[j], notas[j + 1] = notas[j + 1], notas[j]

Estudiantes = ["Ana", "Luis", "Juan", "Sol", "Roberto", "Sonia", "María", "Sofia", "Maria", "Pedro", "Antonio", "Eugenia", "Soledad", "Mario", "María"]
Apellidos = ["Sosa", "Gutierrez", "Alsina", "Martinez", "Sosa", "Ramirez", "Perez", "Lopez", "Arregui", "Mitre", "Andrade", "Loza", "Antares", "Roca", "Perez"]
Nota = [8, 4, 9, 10, 8, 6, 4, 8, 7, 5, 6, 7, 10, 4, 8]

ordenar_listas_por_apellido_nombre_nota(Estudiantes, Apellidos, Nota)

print("Estudiantes ordenados:", Estudiantes)
print("Apellidos ordenados:", Apellidos)
print("Notas correspondientes:", Nota)
