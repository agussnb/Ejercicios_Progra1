# Dadas las siguientes listas:
# Nombres=["Ana","Luis","Juan","Sol","Roberto","Sonia","Ulises","Sofia","Maria","Ped
# ro","Antonio", "Eugenia", "Soledad", "Mario", "Mariela"]
# edades = [23,45,34,23,46,23,45,67,37,68,25,55,45,27,43]
# Desarrollar una función que reciba por parámetro la lista de edades, busque a las 
# personas de menor edad (puede ser más de una) y las retorne. El programa 
# principal deberá mostrar nombre y edad de los menores

def buscar_menores(nombres: list, edades: list):
    min_edad = min(edades)  
    menores = []

    for i in range(len(edades)):
        if edades[i] == min_edad:
            menores.append(i)

    for pos in menores:
        print("Menores:", nombres[pos])

nombres = ["Ana","Luis","Juan","Sol","Roberto","Sonia","Ulises","Sofia","Maria","Pedro","Antonio", "Eugenia", "Soledad", "Mario", "Mariela"]
edades = [23,45,34,23,46,23,45,67,37,68,25,55,45,27,43] 
buscar_menores(nombres,edades)