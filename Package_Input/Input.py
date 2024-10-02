from Validate import *
def get_int(mensaje: str, mensaje_error: str, minimo: int, maximo: int, reintentos: int) -> int | None:
    print(mensaje)
    dato_ingresado = int(input())
    
    while not validate_int(dato_ingresado, minimo, maximo):
        print(mensaje_error)
        reintentos -= 1
        print('Le quedan reintentos =', reintentos)
        
        if reintentos == 0:
            return None
        
        dato_ingresado = int(input())
    
    return dato_ingresado

resultado = get_int("Ingrese un número entre 0 y 100: ", "Número inválido.", 0, 100, 3)
if resultado is None:
    print("Se agotaron los intentos.")
else:
    print("El número ingresado es:", resultado)

def get_float(mensaje: str, mensaje_error: str, minimo: float, maximo: float, reintentos: int) -> int | None:

    print(mensaje)
    dato_ingresado = float(input())
    while not validate_float(dato_ingresado,minimo,maximo):
        print(mensaje_error)
        reintentos -= 1
        print('Le quedan reintentos = ',reintentos)
        if reintentos == 0:
            return None
        dato_ingresado = float(input())
    return dato_ingresado

resultado = get_float("Ingrese un número entre 0 y 100: ", "Número inválido.", 0, 100, 3)
if resultado is None:
    print("Se agotaron los intentos.")
else:
    print("El número ingresado es:", resultado)

def get_string(longitud: int) -> str | None:
    print(f"Ingrese un string que tenga como máximo {longitud} caracteres")
    string_ingresado = input()
    while not validate_string(string_ingresado,longitud):
        print("Error, el string ingresado tenía una cantidad mayor de caracteres que la solicitada")
        string_ingresado = input(f"Ingrese un string que tenga como máximo {longitud} caracteres")
    return string_ingresado

resultado = get_string(13)
if resultado is None:
    print("El string tenía más caracteres de los solicitados")
else:
    print(f'El string ingresado es : {resultado}')