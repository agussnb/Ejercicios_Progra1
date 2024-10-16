# Armar el siguiente menú de opciones:
# 1-Alta de productos (producto nuevo)
# 2-Baja de productos (producto existente)
# 3-Modificar productos (cantidad, ubicación)
# 4-Listar productos
# 5-Lista de productos ordenado por nombre
# 6-Salir
from productos import productos
from biblioteca_gondola.funciones import *
def menu():
    while True:
        print("\nMenú de opciones:")
        print("1 - Alta de productos (producto nuevo)")
        print("2 - Baja de productos (producto existente)")
        print("3 - Modificar productos (cantidad, ubicación)")
        print("4 - Listar productos")
        print("5 - Lista de productos ordenado por nombre")
        print("6 - Salir")
        opcion = int(input("Ingrese una opción: "))

        match opcion:
            case 1:
                alta_producto(productos)
            case 2:
                baja_producto(productos)
            case 3:
                modificar_producto(productos)
            case 4:
                listar_productos(productos)
            case 5:
                listar_ordenado(productos)
            case 6:
                print("Saliendo del programa.")
                break
            case _:
                print("Opción inválida, por favor intente nuevamente.")

menu()