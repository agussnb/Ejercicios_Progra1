suma = 0
contador = 0

for i in range(10):
    numero = float(input("Ingresa un número (o 0 para terminar): "))
    
    if numero == 0:
        break
    
    suma += numero
    contador += 1

if contador > 0:
    promedio = suma / contador
else:
    promedio = 0

print(f"Suma de los números: {suma}")
print(f"Promedio de los números: {promedio}")
