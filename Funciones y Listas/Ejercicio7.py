# Una startup desea analizar las estadísticas de los usuarios de su sitio de 
# compras on-line recientemente lanzado al mercado para ello necesita un programa 
# que le permita acceder a los datos relevados.
# Realizar una función con el siguiente Menú de Opciones:
# 1-Importar listas
# 2-Listar los datos de los usuarios de México
# 3-Listar los nombre, mail y teléfono de los usuarios de Brasil
# 4-Listar los datos del/los usuario/s más joven/es
# 5-Obtener un promedio de edad de los usuarios
# 6-De los usuarios de Brasil, listar los datos del usuario de mayor edad
# 7-Listar los datos de los usuarios de México y Brasil cuyo código postal 
# sea mayor a 8000
# 8-Listar nombre, mail y teléfono de los usuarios italianos mayores a 40 
# años.
from listas_personas import *
from biblioteca_stats.funciones import *
def menu():
    while True:
        print("\nMenú de Opciones:")
        print("1 - Importar listas")
        print("2 - Listar los datos de los usuarios de México")
        print("3 - Listar los nombre, mail y teléfono de los usuarios de Brasil")
        print("4 - Listar los datos del/los usuario/s más joven/es")
        print("5 - Obtener un promedio de edad de los usuarios")
        print("6 - De los usuarios de Brasil, listar los datos del usuario de mayor edad")
        print("7 - Listar los datos de los usuarios de México y Brasil cuyo código postal sea mayor a 8000")
        print("8 - Listar nombre, mail y teléfono de los usuarios italianos mayores a 40 años")
        print("9 - Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            importar_listas()
            print("Listas importadas.")
        elif opcion == "2":
            listar_datos_mex()
        elif opcion == "3":
            listar_datos_br()
        elif opcion == "4":
            listar_datos_users_jovenes()
        elif opcion == "5":
            promedio = listar_promedio_edad_users()
            print(f"El promedio de edad es: {promedio:.2f}")
        elif opcion == "6":
            listar_br_user_max_age()
        elif opcion == "7":
            listar_br_mex_cp()
        elif opcion == "8":
            listar_ita_users_mayores_cuarenta()
        elif opcion == "9":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

menu()
