# Una startup desea analizar las estadísticas de los usuarios de su sitio de 
# compras on-line recientemente lanzado al mercado para ello necesita un programa 
# que le permita acceder a los datos relevados.
# Agregar los siguientes puntos al Menú de Opciones:
# 1-Importar listas Hecho
# 2-Listar los datos de los usuarios de México Hecho
# 3-Listar los nombre, mail y teléfono de los usuarios de Brasil Hecho
# 4-Listar los datos del/los usuario/s más joven/es Hecho
# 5-Obtener un promedio de edad de los usuarios Hecho
# 6-De los usuarios de Brasil, listar los datos del usuario de mayor edad Hecho 
# 7-Listar los datos de los usuarios de México y Brasil cuyo código postal sea
# mayor a 8000 Hecho
# 8-Listar nombre, mail y teléfono de los usuarios italianos mayores a 40 
# años. Hecho
# 9-Listar los datos de los usuarios de México ordenados por nombre
# 10-Listar los datos del/los usuario/s más joven/es ordenados por edad de 
# manera ascendente (Si la edad se repite, ordenar por nombre de manera 
# ascendente)
# 11-Listar los datos de los usuarios de México y Brasil cuyo código postal 
# sea mayor a 8000 ordenado por nombre y edad de manera descendente
from biblioteca_stats.funciones import *

def mostrar_menu():
    print("----- Menú de Opciones -----")
    print("1 - Importar listas")
    print("2 - Listar los datos de los usuarios de México")
    print("3 - Listar nombre, mail y teléfono de los usuarios de Brasil")
    print("4 - Listar los datos del/los usuario/s más joven/es")
    print("5 - Obtener un promedio de edad de los usuarios")
    print("6 - Listar los datos del usuario de mayor edad de Brasil")
    print("7 - Listar los datos de los usuarios de México y Brasil con código postal mayor a 8000")
    print("8 - Listar nombre, mail y teléfono de los usuarios italianos mayores a 40 años")
    print("9 - Listar los datos de los usuarios de México ordenados por nombre")
    print("10 - Listar los datos del/los usuario/s más joven/es ordenados por edad y nombre")
    print("11 - Listar los datos de los usuarios de México y Brasil con código postal mayor a 8000, ordenados por nombre y edad")
    print("0 - Salir")

def ejecutar_menu():
    while True:
        mostrar_menu()
        opcion = input("Elija una opción: ")

        match opcion:
            case "1":
                importar_listas()
                print("Listas importadas exitosamente.")
            case "2":
                listar_datos_mex()
            case "3":
                listar_datos_br()
            case "4":
                listar_datos_users_jovenes()
            case "5":
                promedio = listar_promedio_edad_users()
                print(f"El promedio de edad de los usuarios es: {promedio:.2f}")
            case "6":
                listar_br_user_max_age()
            case "7":
                listar_br_mex_cp()
            case "8":
                listar_ita_users_mayores_cuarenta()
            case "9":
                listar_datos_mex_ordenados_nombre()
            case "10":
                listar_datos_users_jovenes_ordenados()
            case "11":
                listar_br_mex_cp_ordenado()
            case "0":
                print("Saliendo del programa.")
                break
            case _:
                print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    ejecutar_menu()

