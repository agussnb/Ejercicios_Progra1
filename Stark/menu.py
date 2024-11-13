def mostrar_menu():
    print("\n----- Menú de Opciones -----")
    print("1 - Ordenar por nombre ascendente y mostrar en tabla")
    print("2 - Listar masculinos más débiles")
    print("3 - Contar personajes por color de ojos")
    print("4 - Agrupar personajes por color de pelo")
    print("5 - Agrupar personajes por tipo de inteligencia")
    print("6 - Listar personajes con fuerza mayor al promedio de género femenino")
    print("7 - Calcular y agregar IMC a cada personaje y mostrar en tabla")
    print("0 - Salir")

def ejecutar_menu(super_heroes):
    while True:
        mostrar_menu()
        opcion = input("Elija una opción: ")

        match opcion:
            case "1":
                super_heroes.ordenar_por_nombre()
                super_heroes.mostrar_superheroes_en_tabla()
            case "2":
                mas_debil = super_heroes.buscar_debil()
                print(mas_debil)
            case "3":
                super_heroes.contar_por_color_ojos()
            case "4":
                super_heroes.ordenar_por_color_pelo()
            case "5":
                super_heroes.ordenar_por_inteligencia()
            case "6":
                super_heroes.superheroes_mas_fuertes()
            case "7":
                super_heroes.calcular_y_agregar_imc()
            case "0":
                print("Saliendo del programa.")
                break
            case _:
                print("Opción no válida. Intente nuevamente.")
