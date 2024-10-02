# Desarrollar una función que reciba por parámetro, una lista de números 
# y un número especificado. La misma debe buscar el número especificado en la lista 
# y retornar “True” si existe.
def buscar_num_en_lista(lista: list, num: int) -> bool:
    for i in range(len(lista)):
        if num == lista[i]:
            return True
    return False

lista = [1,2,5,8,10,12,15,20,30,50,100]
num = int(input("Ingrese un numero para buscar en la lista: "))
resultado = buscar_num_en_lista(lista, num)

if resultado:
    print("El numero ingresado se encuentra en la lista")
else:
    print("El numero ingresado no se encuentra en la lista")