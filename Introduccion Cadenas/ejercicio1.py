# Desarrollar una función que reciba una letra y una cadena.
# Debe retornar las veces que la letra está incluida en el texto.
def contar_letra(letra, cadena):
    contador = 0
 
    for caracter in cadena:
        if caracter == letra:
            contador += 1
            
    return contador

letra = input("Ingresa una letra: ")
cadena = input("Ingresa una cadena de texto: ")
resultado = contar_letra(letra, cadena)
print(f"La letra '{letra}' aparece {resultado} veces en la cadena.")
