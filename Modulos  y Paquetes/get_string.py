def get_string(longitud: int) -> str | None:
    print(f"Ingrese un string que tenga como máximo {longitud} caracteres")
    string_ingresado = input()
    while len(string_ingresado) > longitud:
        print("Error, el string ingresado tenía una cantidad mayor de caracteres que la solicitada")
        string_ingresado = input(f"Ingrese un string que tenga como máximo {longitud} caracteres")
    return string_ingresado

resultado = get_string(13)
if resultado is None:
    print("El string tenía más caracteres de los solicitados")
else:
    print(f'El string ingresado es : {resultado}')