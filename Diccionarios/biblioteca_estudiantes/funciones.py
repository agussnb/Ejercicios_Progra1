from estudiantes import *
def listar_alumnos(estudiantes: list) -> list:
    for i in range(len(estudiantes)):
        for j in range(0, len(estudiantes) - i - 1):
            if (estudiantes[j]["apellido"] > estudiantes[j + 1]["apellido"]) or \
               (estudiantes[j]["apellido"] == estudiantes[j + 1]["apellido"] and 
                estudiantes[j]["nombre"] > estudiantes[j + 1]["nombre"]):
                estudiantes[j], estudiantes[j + 1] = estudiantes[j + 1], estudiantes[j]

    for estudiante in estudiantes:
        print(f"Legajo: {estudiante['legajo']}, Nombre: {estudiante['nombre']}, "
              f"Apellido: {estudiante['apellido']}, Edad: {estudiante['edad']}")

    return estudiantes  
def promedio_estudiantes(estudiantes:list) -> list:
    for estudiante in estudiantes:
        notas = (estudiante['notas'])
        suma_notas = 0
        for nota in notas:
            suma_notas +=nota
        if len(notas) > 0:
            promedio = suma_notas / len(notas)
        else:
            promedio = 0
        print(f"Nombre: {estudiante['nombre']}, Apellido: {estudiante['apellido']}, promedio nota: {promedio}")
def info_ing_informatica_estudiantes(estudiantes: list) -> None:
    for estudiante in estudiantes:
        if estudiante['programa']['nombre'] == 'Ingenieria en Informatica':
            print(f"Legajo: {estudiante['legajo']}, Nombre: {estudiante['nombre']}, "
                  f"Apellido: {estudiante['apellido']}, Edad: {estudiante['edad']}")
def obtener_promedio_edad(estudiantes: list) -> float:
    suma_edades = 0
    for estudiante in estudiantes:
        suma_edades += estudiante['edad']  
    if len(estudiantes) > 0:
        promedio_edad = suma_edades / len(estudiantes)  
    else:
        promedio_edad = 0  
    return promedio_edad
def mostrar_promedio(promedio_edad):
    print(f"Promedio de edad de los estudiantes: {promedio_edad:.2f}") 
def info_mayor_promedio_notas(estudiantes: list) -> None:
    mayor_promedio = 0
    estudiante_mayor = None
    for estudiante in estudiantes:
        notas = estudiante['notas']
        if len(notas) > 0:
            suma_notas = 0
            for nota in notas:
                suma_notas += nota
            promedio = suma_notas / len(notas)

            if promedio > mayor_promedio:
                mayor_promedio = promedio
                estudiante_mayor = estudiante
    if estudiante_mayor:
        print(f"El alumno con mayor promedio de notas es: {estudiante_mayor['nombre']} {estudiante_mayor['apellido']} con un promedio de {mayor_promedio:.2f}")
    else:
        print("No hay estudiantes con notas para calcular el promedio.")
def info_club_informatica(estudiantes: list) -> None:
    for estudiante in estudiantes:
        if 'grupos' in estudiante:
            for grupo in estudiante['grupos']:
                if grupo['nombre'] == "Club de Informatica":
                    notas = estudiante['notas']
                    if len(notas) > 0:
                        suma_notas = sum(notas)  
                        promedio = suma_notas / len(notas)
                    else:
                        promedio = 0  

                    print(f"Nombre: {estudiante['nombre']}, Apellido: {estudiante['apellido']}, Promedio: {promedio:.2f}")
        else:

            print(f"El estudiante {estudiante['nombre']} no tiene grupos asignados.")
def info_alumnos_mas_jovenes(estudiantes: list) -> None:
    edad_minima = min(estudiante['edad'] for estudiante in estudiantes)
    for estudiante in estudiantes:
        if estudiante['edad'] == edad_minima:
            legajo = estudiante['legajo']
            nombre = estudiante['nombre']
            apellido = estudiante['apellido']
            programa = estudiante['programa']['nombre']
            print(f"Legajo: {legajo}, Nombre: {nombre}, Apellido: {apellido}, Programa: {programa}")
