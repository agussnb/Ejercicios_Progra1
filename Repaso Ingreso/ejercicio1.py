"""""
Enunciado/s:
Tabla de Posiciones de Torneo de Ping-Pong
Cargar los datos de los jugadores con el propósito de realizar estadísticas (no se sabe cuántos):.
Los datos que se cargarán son:
Nombre del jugador
Edad (validar)
Cantidad de puntos (validar-número entero positivo, hasta 60).
Número de partidos ganados (validar-número entero positivo, hasta 35).
Tipo de saque ("plano", "liftado", "cortado")
Categoría ("elite", "experto", "avanzado")
Se necesita saber
Tema A:
1-Cantidad de jugadores de la categoría "elite" con tipo de saque “plano”, cuya edad esté entre 19 y 25 años
inclusive.
2-Nombre y Categoría del jugador de menor edad con más de 50 puntos.
3-Porcentaje de jugadores de categoría "experto".
4-Mostrar el promedio de edad de los jugadores cuya categoría es “avanzado”.
5-Determinar el tipo de saque más usado por los jugadores, cuya categoría sea “elite”.

"""""
# Inicialización de contadores y acumuladores
contador_elite_plano = 0
menor_edad = float('inf')
jugador_menor = None
total_jugadores = 0
total_expertos = 0
suma_edad_avanzado = 0
contador_avanzado = 0
contadores_saque = {"plano": 0, "liftado": 0, "cortado": 0}

while True:
    nombre = input("Ingrese el nombre del jugador (o 'fin' para terminar): ")
    if nombre.lower() == 'fin':
        break

    # Validar edad
    while True:
        edad = input("Ingrese la edad del jugador (18-100): ")
        if edad.isdigit() and 18 <= int(edad) <= 100:
            edad = int(edad)
            break
        else:
            print("Edad no válida. Debe estar entre 18 y 100 años.")

    # Validar puntos
    while True:
        puntos = input("Ingrese la cantidad de puntos (0-60): ")
        if puntos.isdigit() and 0 <= int(puntos) <= 60:
            puntos = int(puntos)
            break
        else:
            print("La cantidad de puntos debe estar entre 0 y 60.")

    # Validar partidos ganados
    while True:
        partidos_ganados = input("Ingrese la cantidad de partidos ganados (0-35): ")
        if partidos_ganados.isdigit() and 0 <= int(partidos_ganados) <= 35:
            partidos_ganados = int(partidos_ganados)
            break
        else:
            print("La cantidad de partidos ganados debe estar entre 0 y 35.")

    # Validar tipo de saque
    while True:
        tipo_saque = input("Ingrese el tipo de saque (plano, liftado, cortado): ").lower()
        if tipo_saque in ["plano", "liftado", "cortado"]:
            break
        else:
            print("Tipo de saque no válido. Debe ser 'plano', 'liftado' o 'cortado'.")

    # Validar categoría
    while True:
        categoria = input("Ingrese la categoría (elite, experto, avanzado): ").lower()
        if categoria in ["elite", "experto", "avanzado"]:
            break
        else:
            print("Categoría no válida. Debe ser 'elite', 'experto' o 'avanzado'.")

    # Contar jugadores de la categoría "elite" con tipo de saque "plano" y edad entre 19 y 25
    if categoria == "elite" and tipo_saque == "plano" and 19 <= edad <= 25:
        contador_elite_plano += 1

    # Buscar el jugador de menor edad con más de 50 puntos
    if puntos > 50 and edad < menor_edad:
        menor_edad = edad
        jugador_menor = (nombre, categoria)

    # Contar jugadores de categoría "experto"
    if categoria == "experto":
        total_expertos += 1

    # Sumar edad de jugadores en la categoría "avanzado"
    if categoria == "avanzado":
        suma_edad_avanzado += edad
        contador_avanzado += 1

    # Contar tipos de saque
    if tipo_saque in contadores_saque:
        contadores_saque[tipo_saque] += 1

    total_jugadores += 1

# Resultados
print("\nResultados:")
print(f"Cantidad de jugadores de la categoría 'elite' con tipo de saque 'plano' y edad entre 19 y 25: {contador_elite_plano}")

if jugador_menor:
    print(f"Jugador de menor edad con más de 50 puntos: {jugador_menor[0]} (Categoría: {jugador_menor[1]})")
else:
    print("No hay jugadores con más de 50 puntos.")

if total_jugadores > 0:
    porcentaje_expertos = (total_expertos / total_jugadores) * 100
    print(f"Porcentaje de jugadores de categoría 'experto': {porcentaje_expertos:.2f}%")
else:
    print("No se registraron jugadores.")

if contador_avanzado > 0:
    promedio_edad_avanzado = suma_edad_avanzado / contador_avanzado
    print(f"Promedio de edad de jugadores en la categoría 'avanzado': {promedio_edad_avanzado:.2f}")
else:
    print("No hay jugadores en la categoría 'avanzado'.")

# Determinar el tipo de saque más usado por los jugadores de categoría "elite"
tipo_saque_mas_usado = max(contadores_saque, key=contadores_saque.get)
print(f"Tipo de saque más usado por jugadores de categoría 'elite': {tipo_saque_mas_usado}")
