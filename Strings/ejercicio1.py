# Desarrollar una función que Invierte el orden de los caracteres en una 
# cadena.
def invertir_cadena(cadena):
    return ''.join([cadena[i] for i in range(len(cadena) - 1, -1, -1)])

cadena = 'Profesional'
prueba = invertir_cadena(cadena)
print(prueba)