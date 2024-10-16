#  El almacén de barrio nos pide un programa para almacenar, ordenar y 
# controlar stock de su mercadería por día.
# Comienza el día con la siguiente disposición en su góndola:
# Cada celda (fila/columna) muestra la ubicación de cada producto, ejemplo: en (1,2)
# se guardan las botellas, etc.
# Armar la lista de Productos con nombre, cantidad y ubicación (fila, columna)
# Definimos los productos con su cantidad y ubicación
productos = [
    {"nombre": "botellas", "cantidad": 3, "ubicacion": (1, 1)},
    {"nombre": "botellas", "cantidad": 3, "ubicacion": (1, 2)},
    {"nombre": "frascos", "cantidad": 4, "ubicacion": (1, 4)},
    {"nombre": "fideos", "cantidad": 5, "ubicacion": (2, 3)},
    {"nombre": "leche", "cantidad": 6, "ubicacion": (3, 4)}
]

def mostrar_stock(productos):
    print(f"{'Producto':<10} {'Cantidad':<10} {'Ubicación':<10}")
    print("-" * 35)
    for producto in productos:
        nombre = producto["nombre"]
        cantidad = producto["cantidad"]
        ubicacion = producto["ubicacion"]
        print(f"{nombre:<10} {cantidad:<10} {ubicacion}")

def actualizar_stock(productos, nombre, cantidad, fila, columna):
    for producto in productos:
        if producto["nombre"] == nombre and producto["ubicacion"] == (fila, columna):
            producto["cantidad"] += cantidad
            break

mostrar_stock(productos)

actualizar_stock(productos, "botellas", 2, 1, 2)

print("\nStock actualizado:")
mostrar_stock(productos)
