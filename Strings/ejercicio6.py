#  Desarrollar una función que verifique si una cadena es un palíndromo:
# Palíndromo: Palabra o frase cuyas letras están dispuestas de tal manera que resulta 
# la misma leída de izquierda a derecha que de derecha a izquierda; por ejemplo, 
# No deseo yo ese don.
def invertir_cadena(cadena):
    return ''.join([cadena[i] for i in range(len(cadena) - 1, -1, -1)])
def es_palindromo(string:str) -> str:
    string_invertido = invertir_cadena(string)
    string_sin_espacios_invertido = ''.join(string_invertido.split())
    string_sin_espacios = ''.join(string.split())
    
    string_sin_espacios = string_sin_espacios.strip()
    string_sin_espacios_invertido = string_sin_espacios_invertido.strip()
    
    if string_sin_espacios.lower() == string_sin_espacios_invertido.lower():
        print('Es palidromo')
    else: 
        print('No es palindromo')



print('Prueba con palindromo: No deseo yo ese don')
prueba = 'No deseo yo ese don'
es_palindromo(prueba)
print('Prueba con palabra no palindromo: Hoy voy a entrenar')
es_palindromo('Hoy voy a entrenar')


