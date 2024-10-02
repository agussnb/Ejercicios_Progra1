# Ejercicio 2: Desarrollar una función que inicialice una lista de 10 números en 0, pida 
# posición y número a guardar al usuario, lo guarde en una lista en la posición 
# solicitada aleatoriamente y la retorne. El programa principal debe invocar a la 
# función y mostrar por pantalla el retorno.
def give_number_and_position(number:int,position:int):
    lista = [0,0,0,0,0,0,0,0,0,0]
    lista[position] = number
    return lista

numero_ingresado = int(input('Ingrese un numero '))
posicion_ingresada = int(input('Ingrese una posicion '))
prueba = give_number_and_position(numero_ingresado,posicion_ingresada)
print(prueba)