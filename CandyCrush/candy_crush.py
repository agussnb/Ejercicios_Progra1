"""
Desarrollar una función que genere números al azar entre 1 y 3, y completar las listas para que queden de la siguiente forma:
● [2, 3, 3, 3, 3, 3, 1]
● [1, 1, 1, 1, 1, 1, 3]
● [3, 1, 2, 3, 1, 1, 1]
● [1, 1, 3, 2, 3, 2, 2]
(los número son generados al azar)
Solicitar al usuario una posición (fila y una 
columna). Verificar si, de forma vertical, existen desde esa posición elegida, hacia arriba o hacia abajo 3 números iguales, es decir 3 unos, 3 dos o 3 tres. Si existen mostra el mensaje "HA GANADO 10 PUNTOS", sino "SEGUI PARTICIPANDO" Utilizar funciones, validar el ingreso de datos.
"""

from Biblioteca_Candy_Crash.funciones import *

tablero = [
    {"piezas": []},
    {"piezas": []},
    {"piezas": []},
    {"piezas": []}
]

ejecutar_juego(tablero)
