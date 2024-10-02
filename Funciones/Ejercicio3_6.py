# Ejercicio 3-6: Realizar un programa que: asigne a la variable numero1 un valor
# solicitado al usuario, valide el mismo entre 10 y 100, realice un descuento del 5% a
# dicho valor a través de una función llamada realizarDescuento(). Mostrar el resultado
# por pantalla. Atención: pueden reutilizarse funciones ya creadas.
#Alumno: Agustin Barrero 
#Comision 213
from Ejercicio3_4 import ingresar_numero

numero = ingresar_numero(10, 100)
print(f'El número ingresado (SIN EL DESCUENTO) es: {numero}')

def realizarDescuento(numero):
    descuento = numero * 0.95 
    print(f'El número ingresado (CON EL DESCUENTO) es: {descuento}')

realizarDescuento(numero)

#Duda: Me esta tomando el numero = ingresar_numero(10,90) del archivo Ejercicio3_4 pero no deberia ser asi porque la variable numero no esta dentro de la funcion y si entendi bien la importacion unicamente debe traer la funcion, entonces no entiendo porque al principio sale el input de ingresar un numero entre 10 y 90