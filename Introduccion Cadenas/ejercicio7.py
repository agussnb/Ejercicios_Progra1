# Crear una función que reciba como parámetro una cadena y suprima los
# caracteres repetidos
#Ej: Si recibe como parámetro la cadena “Hooola” debe devolver “Hola”.
def suprimir_repetidos(cadena):
    resultado = ""
    
    for caracter in cadena:
        if caracter not in resultado:
            resultado += caracter
    
    return resultado

cadena = "Hooola"
resultado = suprimir_repetidos(cadena)

print(f"La cadena sin caracteres repetidos es: {resultado}")
