masculinos_iot_ia = 0
no_ia_no_femenino_o_edad_33_40 = 0
total_empleados = 0
mayor_edad_masculino = 0
nombre_mayor_edad = ""
tecnologia_mayor_edad = ""

for _ in range(10):
    nombre = input("Ingrese el nombre del empleado: ")
    edad = int(input("Ingrese la edad del empleado (no menor a 18): "))
    while edad <= 18:
        print("La edad debe ser mayor o igual a 18.")
        edad = int(input("Ingrese la edad del empleado: "))

    genero = input("Ingrese el género del empleado (Masculino, Femenino, Otro): ")
    tecnologia = input("Ingrese la tecnología de interés (IA , RV, IOT): ")
    tecnologias_validas = ["IA", "RV", "IOT"]
    while tecnologia not in tecnologias_validas:
        print("Opción inválida. Por favor, ingrese IA, RV o IOT.")
        tecnologia = input("Ingrese la tecnología de interés: ")

    total_empleados += 1

    if genero == 'Masculino' and tecnologia in ['IOT', 'IA'] and 25 <= edad <= 50:
        masculinos_iot_ia += 1

    if tecnologia != 'IA' and (genero != 'Femenino' or 33 <= edad <= 40):
        no_ia_no_femenino_o_edad_33_40 += 1

    if genero == 'Masculino' and edad > mayor_edad_masculino:
        mayor_edad_masculino = edad
        nombre_mayor_edad = nombre
        tecnologia_mayor_edad = tecnologia

print(f"Cantidad de empleados masculinos entre 25 y 50 años que votaron por IOT o IA: {masculinos_iot_ia}")
print(f"Porcentaje de empleados que no votaron por IA y cumplen la condición: {(no_ia_no_femenino_o_edad_33_40 / total_empleados) * 100:.2f}%")
print(f"Empleado masculino de mayor edad: {nombre_mayor_edad}, tecnología: {tecnologia_mayor_edad}")