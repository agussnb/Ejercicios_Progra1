#Realizar una función recursiva que permita realizar la suma de los dígitos de un número:
def sumar_digitos(numero: int) -> int:
    if numero == 0:
        return 0
    else:
        ultimo_digito = numero % 10
        resto = numero // 10
        return ultimo_digito + sumar_digitos(resto)

print(f"El resultado de la suma de los digitos es : {sumar_digitos(123)}")  