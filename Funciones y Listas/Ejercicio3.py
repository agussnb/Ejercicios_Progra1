# Desarrollar una función que pida 10 números dentro de un rango 
# especificado, validar los números solicitados dentro de ese rango, guardar en una 
# lista y retornarla. El programa principal debe invocar a la función y mostrar por 
# pantalla el retorno.
def diez_numeros(a:int,b:int):
    lista_numeros = [0,0,0,0,0,0,0,0,0,0]
    for i in range(10):
        numero_ingresado = int(input(f"Ingrese un numero entre {a} y {b}: "))
        while numero_ingresado < a or numero_ingresado > b:
            print(f'El número ingresado no está entre {a} y {b}.')
            numero_ingresado = int(input(f'Ingrese un número entre {a} y {b}: '))
        lista_numeros[i] = numero_ingresado
    return lista_numeros

resultado = diez_numeros(100,300) 
print(resultado)