# Desarrollar una función que cuente cuántas palabras hay en una cadena

def contar_palabras(string:str) -> str:
    string_separado = string.split()
    print(f'La cantidad de palabras en {string} es : {len(string_separado)}')

resultado = 'Tecnicatura en Programacion'
contar_palabras(resultado)
