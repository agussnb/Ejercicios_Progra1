# Crear una función que reciba una cadena y un caracter. La función deberá
# devolver el índice en el que se encuentre la primera incidencia de dicho
# caracter, o -1 en caso de que no esté
def encontrar_indice(cadena, caracter):
    for i in range(len(cadena)):
        if cadena[i] == caracter:
            return i  
    
    return -1


cadena = "Supermercado Coto"
caracter = 'f'
#caracter = 'e' #para probar si no retorna -1 en caso de encontrar un caracterer, sacar el comentario en esta linea.
indice = encontrar_indice(cadena, caracter)

print(f"El índice de '{caracter}' es: {indice}")
