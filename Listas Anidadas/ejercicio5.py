# Desarrollar un programa para el control de stock de una ferretería para 
# sus artículos de tornillos y tarugos. Los mismos se encuentran almacenados en una 
# cajonera de ferretería metálica con cajones.
# La disposición de los mismos es la siguiente: Una estantería de 4 filas con 4 cajones 
# por fila.
# Armar la lista estantería para contener los cajones con listas anidadas
# Representación de la estantería de 4 filas con 4 cajones por fila
# Cada cajón contendrá una tupla con el nombre del producto (tamaño y cantidad)
estanteria = [
    # Fila 1
    [("tornillo to12", 65), ("tornillo to16", 86), ("tornillo to20", 65), ("tornillo to25", 45)],
    
    # Fila 2
    [("tornillo to30", 68), ("tornillo to35", 73), ("tornillo to40", 85), ("tornillo to45", 89)],

    # Fila 3
    [("tarugo ta4", 58), ("tarugo ta5", 48), ("tarugo ta6", 64), ("tarugo ta7", 96)],

    # Fila 4
    [("tarugo ta8", 36), ("tarugo ta10", 72), ("tarugo ta12", 78), ("tarugo ta14", 71)]
]

def mostrar_estanteria(estanteria):
    for fila in range(len(estanteria)):
        print(f"Fila {fila + 1}:")
        for cajon in range(len(estanteria[fila])):
            producto, cantidad = estanteria[fila][cajon]
            print(f"  Cajón {cajon + 1}: {producto}, Cantidad: {cantidad}")
        print()

def buscar_producto(estanteria, nombre_producto):
    for fila in range(len(estanteria)):
        for cajon in range(len(estanteria[fila])):
            producto, cantidad = estanteria[fila][cajon]
            if nombre_producto in producto:
                print(f"Producto encontrado: {producto}, Cantidad: {cantidad}, Ubicación: Fila {fila + 1}, Cajón {cajon + 1}")
                return
    print("Producto no encontrado.")

def modificar_cantidad(estanteria, nombre_producto, nueva_cantidad):
    for fila in range(len(estanteria)):
        for cajon in range(len(estanteria[fila])):
            producto, cantidad = estanteria[fila][cajon]
            if nombre_producto in producto:
                estanteria[fila][cajon] = (producto, nueva_cantidad)
                print(f"Cantidad de {producto} modificada a {nueva_cantidad}.")
                return
    print("Producto no encontrado.")

mostrar_estanteria(estanteria)

buscar_producto(estanteria, "to16")

modificar_cantidad(estanteria, "to16", 90)

print("\nEstantería actualizada:")
mostrar_estanteria(estanteria)
