# Desarrollar una función que capitalice palabras en una cadena.
def capitalizar(string:str) -> str:
    return string.capitalize()


string = 'hola'
resultado = capitalizar(string)
print(resultado)