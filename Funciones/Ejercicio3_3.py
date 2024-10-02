# Ejercicio 3-3: Crear una función que permita determinar si un número es par o no. La
# función retorna “True” en caso afirmativo y “False en caso contrario. Probar en el
# programa principal realizando la invocación o llamada
#Alumno: Agustin Barrero 
#Comision 213
def numero_es_par_o_no (numero) :
    if numero % 2 == 0 :
        return True
    else :
        return False

numero = int(input('Ingrese un numero '))
print(numero_es_par_o_no(numero))
