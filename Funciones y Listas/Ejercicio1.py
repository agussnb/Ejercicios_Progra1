# Ejercicio 1: Desarrollar una función que pida 10 nombres de manera secuencial, los 
# guarde en una lista y la retorne. El programa principal debe invocar a la función y
# mostrar por pantalla el retorno.
def give_names():
    nombres = []
    for i in range(10):
        nombre_ingresado = input('Ingrese un nombre: ')
        nombres.append(nombre_ingresado)
    return nombres

# Llamada a la función y muestra el resultado
lista_nombres = give_names()
print(lista_nombres)