import random
import csv

# def generar_tablero():
#     tablero = [{'piezas': []} for _ in range(4)]
#     generar_numeros(tablero)
#     return tablero
#To do agregar bloques try except para validaciones de ingreso de datos (filas, columnas, otros)   

def generar_numeros(tablero):
    for elemento in tablero:
        while len(elemento['piezas']) < 7:
            numero = random.randint(1, 3)                                       
            elemento['piezas'].append(numero)
        print(elemento)
    return tablero
    

def pedir_coordenadas() -> list:
    fila = int(input("Eliga una fila: [0-3] ")) 
    while fila < 0 or fila > 3:
        fila = int(input("La fila debe estar entre 0 y 3: "))
    columna = int(input("Eliga una columna: [0-6] ")) 
    while columna < 0 or columna > 6:
        columna = int(input("La columna debe estar entre 0 y 6: "))
    return [fila, columna]

def verificar_juego(tablero:list,x:int,y:int):
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
    jugador = input('Ingresa tu nombre: ')
    
    with open('CandyCrush/score.csv', 'a', newline='') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow([jugador, score])
    
    
def parametros_for(tablero,x):
    parametros_arriba = [x -1,-1,-1]
    parametros_abajo = [x +1,len(tablero)]
    parametros_para_for = [parametros_arriba,parametros_abajo]
    #print(parametros_para_for)
    #print(f"Parametros con el * atras para ver que devuelve ",*parametros_para_for)
    return parametros_para_for
    
def verificar_consecutivos(tablero:list, x:int,y:int, valor:int) ->bool:
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
    # parametros_para_for = parametros_for(tablero,x)
    # for parametros in parametros_para_for:
    #     for i in range(*parametros):
    #         if tablero[i]['piezas'][y] == valor:
    #             if parametros == parametros_para_for[0]:
    #                 contador_arriba+=1
    #             else:
    #                 contador_abajo+=1
    #         else:
    #             break
    # return contador_arriba + contador_abajo >=2
#Hacer otra funcion para poner como parametro dentro del for un string con los parametros

def mostrar_scoreboard():
    print("Scoreboard: \n")
    with open('CandyCrush/score.csv','r') as archivo:
        lector = csv.reader(archivo)
        for contenido in lector:
            print(contenido)
        

def ejecutar_juego(tablero):
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
            
        
        

