# Desarrollar una función “char_at” que recibe una cadena y un número. 
# Se debe retornar el caracter en la posición indicada por el número si ésta es válida. 
# **IMPORTANTE: **Las posiciones de los caracteres en un string van del 0 hasta el 
# <número de caracteres> - 1.

def char_at(cadena, numero):
    if numero < 0 or numero >= len(cadena):
        return "La posición no es válida."

    return cadena[numero]

cadena = input("Ingresa una cadena: ")
numero = int(input("Ingresa un número (posición): "))
resultado = char_at(cadena, numero)
print(f"El carácter en la posición {numero} es: {resultado}")
