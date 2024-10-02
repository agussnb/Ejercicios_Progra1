#Realizar una función recursiva que calcule la suma de los primeros números naturales
def sumar_naturales(numero:int)-> int:
    if numero == 1 :
        return 1 
    else:
        return numero + sumar_naturales(numero - 1)
   
 
print(f"El resultado del calculo fue : {sumar_naturales(7)}")