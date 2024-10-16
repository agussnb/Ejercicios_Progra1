# Crear una función que reciba una cadena por parámetro y suprima las
# vocales de la misma.
# Ej: Si recibe como parámetro la cadena “Hola” debe devolver “Hl”.
def suprimir_vocales(cadena):
    vocales = "aeiouAEIOU"
    
    resultado = ""

    for caracter in cadena:
        if caracter not in vocales:
            resultado += caracter
    
    return resultado

cadena = "Hola"
resultado = suprimir_vocales(cadena)

print(f"La cadena sin vocales es: {resultado}")
