#Realizar una función recursiva que calcule la potencia de un número:
def calc_potencia(base:int,exponente:int)-> int:
    if exponente == 0:
        return 1
    else:
        return base * calc_potencia(base, exponente -1)
   
resultado = calc_potencia(5,2)
print(f"El resultado del calculo fue : {resultado}")