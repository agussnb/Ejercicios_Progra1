# Realizar una función con el siguiente Menú de Opciones:
# 1-Listar los alumnos por orden ascendente de apellido, si se repite, 
# ordenar por nombre. Mostrar legajo, nombre, apellido y edad
# 2-Obtener el promedio de notas para cada estudiante
# 3-Listar legajo, nombre, apellido y edad de los estudiantes que cursan el 
# programa de “Ingenieria en Informatica”
# 4-Obtener un promedio de edad de los estudiantes. Mostrar nombre y 
# apellido
# 5-Informar el alumno con mayor pomedio de notas. Mostrar nombre y 
# apellido
# 6-Listar nombre y apellido de los alumnos que forman el grupo “Club de 
# Informática” con sus respectivos promedios
# 7-Listar legajo, nombre, apellido y programas que cursan los alumnos
# más jóvenes.
from biblioteca_estudiantes.funciones import *
from estudiantes import * 

def mostrar_menu():
    print("----- Menú de Opciones -----")
    print("1 - Listar alumnos por apellido y nombre")
    print("2 - Obtener promedio de notas para cada estudiante")
    print("3 - Listar alumnos en 'Ingeniería en Informática'")
    print("4 - Obtener promedio de edad de los estudiantes")
    print("5 - Informar alumno con mayor promedio de notas")
    print("6 - Listar alumnos en 'Club de Informática' con promedios")
    print("7 - Listar alumnos más jóvenes")
    print("0 - Salir")

def ejecutar_menu():
    while True:
        mostrar_menu()
        opcion = input("Elija una opción: ")
        
        if opcion == "0":
            print("Saliendo del programa.")
            break

        if opcion == "1":
            listar_alumnos(estudiantes)
        elif opcion == "2":
            promedio_estudiantes(estudiantes)
        elif opcion == "3":
            info_ing_informatica_estudiantes(estudiantes)
        elif opcion == "4":
            obtener_promedio_edad(estudiantes)
        elif opcion == "5":
            info_mayor_promedio_notas(estudiantes)
        elif opcion == "6":
            info_club_informatica(estudiantes)
        elif opcion == "7":
            info_alumnos_mas_jovenes(estudiantes)
        else:
            print("Opción inválida. Intente nuevamente.")
    

ejecutar_menu()