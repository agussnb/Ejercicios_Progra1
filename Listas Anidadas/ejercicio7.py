#Crear una función para cada opción de menú.
def listar_inventario(estanteria):
    print(f"{'Producto':<15} {'Cantidad':<10}")
    print("-" * 30)
    for fila in estanteria:
        for producto, cantidad in fila:
            print(f"{producto:<15} {cantidad:<10}")
    print()

def reponer_mercaderia(estanteria, nombre_producto, cantidad_a_reponer):
    for fila in estanteria:
        for i in range(len(fila)):
            producto, cantidad = fila[i]
            if nombre_producto in producto:
                fila[i] = (producto, cantidad + cantidad_a_reponer)
                print(f"Producto {producto} repuesto. Cantidad actual: {cantidad + cantidad_a_reponer}")
                return
    print(f"Producto {nombre_producto} no encontrado.")

def vender_mercaderia(estanteria, nombre_producto, cantidad_a_vender):
    for fila in estanteria:
        for i in range(len(fila)):
            producto, cantidad = fila[i]
            if nombre_producto in producto:
                if cantidad >= cantidad_a_vender:
                    fila[i] = (producto, cantidad - cantidad_a_vender)
                    print(f"Producto {producto} vendido. Cantidad restante: {cantidad - cantidad_a_vender}")
                else:
                    print(f"No hay suficiente stock de {producto}. Stock actual: {cantidad}")
                return
    print(f"Producto {nombre_producto} no encontrado.")