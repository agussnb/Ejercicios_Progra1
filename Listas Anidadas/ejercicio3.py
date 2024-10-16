def listar_productos(productos):
    print(f"{'Producto':<10} {'Cantidad':<10} {'Ubicación':<10}")
    print("-" * 35)
    for producto in productos:
        nombre = producto["nombre"]
        cantidad = producto["cantidad"]
        ubicacion = producto["ubicacion"]
        print(f"{nombre:<10} {cantidad:<10} {ubicacion}")

def alta_producto(productos):
    nombre = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad: "))
    fila = int(input("Ingrese la fila de ubicación: "))
    columna = int(input("Ingrese la columna de ubicación: "))
    productos.append({"nombre": nombre, "cantidad": cantidad, "ubicacion": (fila, columna)})
    print("Producto agregado con éxito.")

def baja_producto(productos):
    nombre = input("Ingrese el nombre del producto a eliminar: ")
    productos[:] = [producto for producto in productos if producto["nombre"] != nombre]
    print(f"Producto '{nombre}' eliminado.")

def modificar_producto(productos):
    nombre = input("Ingrese el nombre del producto a modificar: ")
    for producto in productos:
        if producto["nombre"] == nombre:
            nuevo_valor = input("¿Desea modificar la cantidad o la ubicación? (c/u): ").lower()
            if nuevo_valor == 'c':
                cantidad = int(input("Ingrese la nueva cantidad: "))
                producto["cantidad"] = cantidad
            elif nuevo_valor == 'u':
                fila = int(input("Ingrese la nueva fila de ubicación: "))
                columna = int(input("Ingrese la nueva columna de ubicación: "))
                producto["ubicacion"] = (fila, columna)
            print(f"Producto '{nombre}' modificado.")
            return
    print(f"Producto '{nombre}' no encontrado.")

def listar_ordenado(productos):
    productos_ordenados = sorted(productos, key=lambda x: x["nombre"])
    listar_productos(productos_ordenados)