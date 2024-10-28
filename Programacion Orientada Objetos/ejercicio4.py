# Crear una clase Calculadora que pueda calcular suma, resta, multiplicación y división. Se debe 
# crear la clase e implementarla

class Calculadora:
    def __init__(self):
        pass
    def suma(self, num_a: int, num_b: int) -> int:
        return num_a + num_b

    def resta(self, num_a: int, num_b: int) -> int:
        return num_a - num_b

    def multiplicacion(self, num_a: int, num_b: int) -> int:
        return num_a * num_b

    def division(self, num_a: int, num_b: int) -> float:
        return num_a / num_b if num_b != 0 else "Error: División por cero"

def mostrar_menu():
    print("----- Menú de Opciones -----")
    print("1 - Sumar")
    print("2 - Restar")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("0 - Salir")

def pedir_numero(prompt):
    num = input(prompt)
    while not num.isdigit() or int(num) < -99999999 or int(num) > 99999999:
        print("Error, seleccione un número entre 0 y 9.")
        num = input(prompt)
    return int(num)

def ejecutar_menu():
    calculadora = Calculadora()
    while True:
        mostrar_menu()
        opcion = input("Elija una opción: ")
        
        if opcion == "0":
            print("Saliendo del programa.")
            break

        if opcion in ["1", "2", "3", "4"]:
            num_a = pedir_numero("Seleccione el primer número : ")
            num_b = pedir_numero("Seleccione el segundo número : ")

            if opcion == "1":
                resultado = calculadora.suma(num_a, num_b)
                print(f"Resultado de la suma: {resultado}")
            elif opcion == "2":
                resultado = calculadora.resta(num_a, num_b)
                print(f"Resultado de la resta: {resultado}")
            elif opcion == "3":
                resultado = calculadora.multiplicacion(num_a, num_b)
                print(f"Resultado de la multiplicación: {resultado}")
            elif opcion == "4":
                resultado = calculadora.division(num_a, num_b)
                print(f"Resultado de la división: {resultado}")
            
            continuar = input("¿Desea realizar otra operación? (si/no): ").lower()
            if continuar != "si":
                print("Saliendo del programa.")
                break
        else:
            print("Opción inválida. Intente nuevamente.")

ejecutar_menu()
