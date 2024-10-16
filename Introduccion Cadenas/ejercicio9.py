# Crear una función para contar cuántas veces aparece una subcadena dentro
# de una cadena.
# Ej: Si recibe la cadena “El pan del panadero” y la subcadena “pan” deberá
# retornar el valor 2.
def contar_subcadena(cadena, subcadena):
    return cadena.count(subcadena)

cadena = "El pan del panadero"
subcadena = "pan"
resultado = contar_subcadena(cadena, subcadena)

print(f"La subcadena '{subcadena}' aparece {resultado} veces en la cadena '{cadena}'.")
