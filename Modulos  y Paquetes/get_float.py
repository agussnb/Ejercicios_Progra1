def get_float(mensaje: str, mensaje_error: str, minimo: float, maximo: float, reintentos: int) -> int | None:

    print(mensaje)
    dato_ingresado = float(input())
    while (dato_ingresado < minimo) or (dato_ingresado > maximo):
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