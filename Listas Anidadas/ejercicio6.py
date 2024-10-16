# Armar el siguiente menú de opciones:
# 1- Reponer mercadería (productos existentes)
# 2- Vender mercadería (producto existente, solo si alcanza el stock)
# 3- Listar inventario
# 5- Salir
from estanteria import estanteria
from biblioteca_ferreteria.funciones import *
def menu():
    while True:
        print("\nMenú de opciones:")
        print("1 - Reponer mercadería (productos existentes)")
        print("2 - Vender mercadería (producto existente, solo si alcanza el stock)")
        print("3 - Listar inventario")
        print("5 - Salir")
        
        opcion = int(input("Ingrese una opción: "))
        
        match opcion:
            case 1:
                producto = input("Ingrese el nombre del producto a reponer: ")
                cantidad = int(input("Ingrese la cantidad a reponer: "))
                reponer_mercaderia(estanteria, producto, cantidad)
            case 2:
                producto = input("Ingrese el nombre del producto a vender: ")
                cantidad = int(input("Ingrese la cantidad a vender: "))
                vender_mercaderia(estanteria, producto, cantidad)
            case 3:
                listar_inventario(estanteria)
            case 5:
                print("Saliendo del programa.")
                break
            case _:
                print("Opción inválida, por favor intente nuevamente.")

menu()