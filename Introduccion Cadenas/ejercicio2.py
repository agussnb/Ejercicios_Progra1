#Desarrollar una función que reciba una cadena y dos índices. 
#Se debe retornar la cadena que va entre las posiciones indicadas por los índices. 
#Si las posiciones no son válidas se debe informar.

def subcadena_por_indices(cadena, indice_inicial, indice_final):
    if indice_inicial < 0 or indice_final >= len(cadena) or indice_inicial > indice_final:
        return "Los índices no son válidos."

    return cadena[indice_inicial:indice_final + 1]

cadena = input("Ingresa una cadena: ")
indice_inicial = int(input("Ingresa el índice inicial: "))
indice_final = int(input("Ingresa el índice final: "))
resultado = subcadena_por_indices(cadena, indice_inicial, indice_final)
print(f"La subcadena es: {resultado}")

