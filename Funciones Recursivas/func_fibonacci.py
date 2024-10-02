#Realizar una función para calcular el número de Fibonacci de un número ingresado por consola. 
import Package_Input.Input

def calcular_fibonacci(numero: int) -> int:
    if numero <= 1:
        return numero
    
    a, b = 0, 1
    for _ in range(2, numero + 1):
        a, b = b, a + b
    return b

numero = Package_Input.Input.get_int()

resultado = calcular_fibonacci(numero)
print(f"El número de Fibonacci en la posición {numero} es: {resultado}")
       

