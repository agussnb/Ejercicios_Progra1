# Crear una clase Cuenta Bancaria que tenga las características titular y saldo encapsulado. De la 
# cuenta bancaria se puede obtener el saldo, depositar o retirar (en cada caso imprimir que fue
# exitoso). Se debe crear la clase e implementarla.

class CuentaBancaria:
    def __init__(self, titular: str, saldo_encapsulado: int):
        self.titular = titular
        self.saldo_encapsulado = saldo_encapsulado

    def obtener_saldo(self):
        print('Su saldo es :')
        return self.saldo_encapsulado

    def depositar(self):
        # Usar input para pedir el dinero a depositar
        dinero_depositado = int(input('Ingrese el dinero que quiere depositar: '))
        self.saldo_encapsulado += dinero_depositado
        print(f'Se depositaron {dinero_depositado} en su cuenta.')

    def retirar(self):
        dinero_retirado = int(input('Ingrese la cantidad que desea retirar: '))
        if dinero_retirado <= self.saldo_encapsulado:
            self.saldo_encapsulado -= dinero_retirado
            print(f'Se retiraron {dinero_retirado} de su cuenta.')
        else:
            print("Fondos insuficientes.")

def mostrar_menu():
    print("----- Menú de Opciones -----")
    print("1 - Ver saldo")
    print("2 - Depositar")
    print("3 - Retirar dinero")
    print("0 - Salir")
    
def pedir_numero(prompt):
    num = input(prompt)
    while not num.isdigit() or int(num) < -99999999 or int(num) > 99999999:
        print("Error, seleccione un número entre 0 y 9.")
        num = input(prompt)
    return int(num)

def ejecutar_menu():
    cuenta_bancaria = CuentaBancaria("Agustin", 5000)
    while True:
        mostrar_menu()
        opcion = input("Elija una opción: ")
        
        if opcion == "0":
            print("Saliendo del programa.")
            break

        if opcion in ["1", "2", "3"]:
            if opcion == "1":
                resultado = cuenta_bancaria.obtener_saldo()
                print(resultado)
            elif opcion == "2":
                cuenta_bancaria.depositar()
            elif opcion == "3":
                cuenta_bancaria.retirar()
            
            continuar = input("¿Desea realizar otra operación? (si/no): ").lower()
            if continuar != "si":
                print("Saliendo del programa.")
                break
        else:
            print("Opción inválida. Intente nuevamente.")

ejecutar_menu()
