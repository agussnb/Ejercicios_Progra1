# Ejercicio 3-5: Realizar un programa en donde se puedan utilizar los prototipos de la
# función Restar en sus 4 combinaciones.
#  Restar1(int, int)->int:
#  Restar2()->int:
#  Restar3(int, int):
#  Restar4():
#Alumno: Agustin Barrero 
#Comision 213
    #Aclaraciones: 
        #1- Uso :int en los parametros para que la funcion entienda que se espera un numero.
        #2- Me hubiese gustado que el Restar3 tuviera el print Restar3:... pero al llamar a la funcion dentro del print devuelve None porque la funcion no tiene retorno, asi que la tuve que llamar sin usar el print.
def Restar1 (numero1: int, numero2:int) :
    return numero1 - numero2

def Restar2 () :
    numero1 = int(input('Ingrese un numero '))
    numero2 = int(input('Ingrese un numero '))
    return numero1 - numero2

def Restar3 (numero1: int, numero2: int) :
   print(f"La resta es: {numero1 - numero2}")

def Restar4 () :
    numero1 = int(input('Ingrese un numero '))
    numero2 = int(input('Ingrese un numero '))
    resta = numero1-numero2
    return resta

print(f"Restar1: {Restar1(10,5)}")
print(f"Restar2: {Restar2()}")
#print(f"Restar3: {Restar3(4,2)}")
Restar3(4,2)
print(f"Restar4: {Restar4()}")
