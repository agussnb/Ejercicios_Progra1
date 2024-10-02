def get_int(mensaje: str, mensaje_error: str, minimo: int, maximo: int, reintentos: int) -> int | None:

    print(mensaje)
    dato_ingresado = int(input())
    while (dato_ingresado < minimo) or (dato_ingresado > maximo):
        print(mensaje_error)
        reintentos -= 1
        print('Le quedan reintentos = ',reintentos)
        if reintentos == 0:
            return None
        dato_ingresado = int(input())
    return dato_ingresado

resultado = get_int("Ingrese un número entre 0 y 100: ", "Número inválido.", 0, 100, 3)
if resultado is None:
    print("Se agotaron los intentos.")
else:
    print("El número ingresado es:", resultado)