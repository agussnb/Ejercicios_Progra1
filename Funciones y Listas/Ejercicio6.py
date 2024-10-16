# Analizar los datos del archivo listas_personas.py. Utilizando el archivo 
# listas_personas.py. Importar los nombres a una lista. Realizar una función que 
# muestre los mismos.
from listas_personas import *

def mostrar_datos():
    for nombre in Nombres:
        print(nombre)

mostrar_datos()