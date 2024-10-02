# Ejercicio 3-4: Especializar la función del punto 3.1 y 3.2 para que valide el número en
# un rango determinado pasado por parámetro “desde”-“hasta”.
#Alumno: Agustin Barrero 
#Comision 213
def ingresar_numero(desde, hasta):
    numero_ingresado = int(input(f'Ingrese un número entre {desde} y {hasta}: '))
    
    while numero_ingresado < desde or numero_ingresado > hasta:
        print(f'El número ingresado no está entre {desde} y {hasta}.')
        numero_ingresado = int(input(f'Ingrese un número entre {desde} y {hasta}: '))
    
    return numero_ingresado



#En este caso puse desde 10 a 90 pero podria ser desde cualquier rango de numeros.
numero = ingresar_numero(10, 90)
print(f'El número ingresado es: {numero}')
