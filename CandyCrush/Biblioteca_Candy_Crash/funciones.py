import random
import csv

def generar_numeros(tablero):
    """
    Funcion que se encargar de rellenar el tablero con numeros aleatorios desde 1 a 3
    """
    for elemento in tablero:
        while len(elemento['piezas']) < 7:
            numero = random.randint(1, 3)                                       
            elemento['piezas'].append(numero)
        print(elemento)
    return tablero
    
def pedir_coordenadas() -> list:
    """
    Funcion que le solicita al usuario una fila y una columna
    """
    fila = int(input("Eliga una fila: [0-3] ")) 
    while fila < 0 or fila > 3:
        fila = int(input("La fila debe estar entre 0 y 3: "))
    columna = int(input("Eliga una columna: [0-6] ")) 
    while columna < 0 or columna > 6:
        columna = int(input("La columna debe estar entre 0 y 6: "))
    return [fila, columna]

def verificar_consecutivos(tablero:list, x:int,y:int, valor:int) ->bool:
    """
    Funcion para verificar si las coordenadas elegidas por el jugador contienen arriba o abajo, un mismo numero, es decir
    si se elige una posicion x,y donde hay un 2, verificar si hay un 2 arriba y abajo de la posicion elegida.
    """
    contador_arriba = 0
    contador_abajo = 0
    for i in range(x -1, -1, -1):
        if tablero[i]['piezas'][y] == valor:
            contador_arriba +=1
        else:
            break
    for i in range(x + 1, len(tablero)):
        if tablero[i]['piezas'][y] == valor:
            contador_abajo +=1
        else:
            break
    return contador_arriba + contador_abajo >=2 
    
def verificar_juego(tablero:list,x:int,y:int):
    """
    Funcion que verifica si en las coordenadas elegidas por el jugador, hay 3 numeros iguales de manera vertical, el mismo ganara 10 puntos, de lo contrario se le dira que siga participando
    """
    valor_actual = tablero[x]['piezas'][y]
    score = 0
    if verificar_consecutivos(tablero,x,y,valor_actual):
            score+=10
            scoreboard(score)
            print("Ganaste 10 puntos")
    else:
        score = 0
        scoreboard(score)
        print("Segui participando")

def scoreboard(score:int):
    """
    Funcion que crea un archivo csv donde se guardan los puntajes de los jugadores 
    """
    jugador = input('Ingresa tu nombre: ')
    
    with open('CandyCrush/score.csv', 'a', newline='') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow([jugador, score])

def mostrar_scoreboard():
    """
    Funcion que muestra el scoreboard
    """
    print("Scoreboard: \n")
    with open('CandyCrush/score.csv','r') as archivo:
        lector = csv.reader(archivo)
        for contenido in lector:
            print(contenido)
        
def ejecutar_juego(tablero):
    """
    Funcion que ejecuta el juego en un bucle hasta que el jugador decida no seguir jugando.
    """
    seguir = 'si'
    while seguir == 'si':
        lista_tablero = generar_numeros(tablero)
        coordenadas = pedir_coordenadas()
        verificar_juego(lista_tablero,coordenadas[0],coordenadas[1])
        seguir = input('Queres seguir jugando? si/no ')
        if seguir == 'si':
            tablero = [
                    {"piezas": []},
                    {"piezas": []},
                    {"piezas": []},
                    {"piezas": []}
                    ]
        if seguir == 'no':
            mostrar_scoreboard()
            