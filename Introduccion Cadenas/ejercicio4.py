# Crear una función que reciba como parámetro una cadena y determine la
# cantidad de vocales que hay de cada una (individualmente). La función
# retornará una matriz indicando en la columna 1 cada vocal, y en la columna 2
# la cantidad.
def contar_vocales(cadena):
    vocales = ['a', 'e', 'i', 'o', 'u']
    
    conteo_vocales = [0] * len(vocales)
    
    cadena = cadena.lower()
    
    for letra in cadena:
        if letra in vocales:
            indice = vocales.index(letra)
            conteo_vocales[indice] += 1

    matriz = []
    for i in range(len(vocales)):
        matriz.append([vocales[i], conteo_vocales[i]])
    
    return matriz

cadena = "Hola, cómo estás?"
resultado = contar_vocales(cadena)

for fila in resultado:
    print(f"Vocal: {fila[0]}, Cantidad: {fila[1]}")
