# Ejercicio 3-7: Realizar un programa que: asigne a las variables numero1 y numero2
# los valores solicitados al usuario, valide los mismos entre 10 y 100, asigne a la
# variable operacion el valor solicitado al usuario: 's'-sumar, 'r'-restar (validar),realice 
# la operación de dichos valores a través de una función. Mostrar el resultado por
# pantalla.
#Alumno: Agustin Barrero 
#Comision 213
def ingresar_numero(desde, hasta):
    numero_ingresado_uno = int(input(f'Ingrese un número entre {desde} y {hasta}: '))
    numero_ingresado_dos = int(input(f'Ingrese un número entre {desde} y {hasta}: '))
  
    while numero_ingresado_uno < desde or numero_ingresado_uno > hasta:
        print(f'El número ingresado no está entre {desde} y {hasta}.')
        numero_ingresado_uno = int(input(f'Ingrese un número entre {desde} y {hasta}: '))
        
    while numero_ingresado_dos < desde or numero_ingresado_dos > hasta:
        print(f'El número ingresado no está entre {desde} y {hasta}.')
        numero_ingresado_dos = int(input(f'Ingrese un número entre {desde} y {hasta}: '))
    return numero_ingresado_uno,numero_ingresado_dos
         
from funciones import Restar3
from funciones import Sumar

operacion = input('Ingrese una operacion : "s" = sumar "r" : restar ')
while operacion != "s" and operacion != "r":
      operacion = input('Operacion incorrecta, vuelva a ingresar la operacion solicitada. "s" = sumar "r" : restar ')
        
match operacion:
    case "s":
        numero = ingresar_numero(10,100)
        suma_ingresos = Sumar(*numero)
    case "r":
        numero = ingresar_numero(10,100)
        resta_ingresos = Restar3(*numero)

#Explicacion codigo:
#Como guardo los dos numeros en una sola variable llamada numero tuve que buscar en google como acceder a esos valores dentro de la variable numero yo lo pense como si fuera un array de javascript entonces intente usar como parametros de la funcion sumar numero.index[0],numero.index[1] pero luego leyendo como funciona index vi que solo traia el la primer posicion del indice entonces no me servia, hasta que encontre que usando el asterisco se separan los numeros que estan dentro de numero 


