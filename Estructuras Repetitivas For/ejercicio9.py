numero = int(input("Ingresa un número: "))

contador_divisores = 0

print(f"Divisores de {numero}:")
for i in range(1, numero + 1):
    if numero % i == 0:
        print(i)  
        contador_divisores += 1 

print(f"Cantidad de divisores encontrados: {contador_divisores}")
