from data_stark import lista_personajes
def ordenar_por_nombre(lista:list, clave:str):
    """
     Listar ordenado por Nombre. Lista todos los datos de cada superhéroe ordenados por 
     Nombre de manera ascendente.
    """
    n = len(lista)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if lista[j][clave] > lista[j + 1][clave]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]  
    return lista

def mostrar_personajes_ordenados(lista, claves):
    anchos = {clave: max(len(str(fila[clave])) for fila in lista) for clave in claves}
    
    encabezado = " | ".join(f"{clave.upper():<{anchos[clave]}}" for clave in claves)
    print(encabezado)
    print("-" * len(encabezado))

    for fila in lista:
        fila_formateada = []
        for clave in claves:
            valor = fila[clave]

            if clave == 'peso' or clave == 'altura':
                valor = f"{float(valor):.2f}"
            
            fila_formateada.append(f"{str(valor):<{anchos[clave]}}")
        
        print(" | ".join(fila_formateada))

    
def buscar_debil(lista:list):
    """
    Listar Masculinos débiles. Recorrer la lista y determinar cuál es el superhéroe más débil de 
    género M, es decir, el que tenga la menor fuerza.
    """
    mas_debil = None  
    fuerza_minima = float('inf')  

    for superheroe in lista:
        if superheroe['genero'] == 'M':
            fuerza = int(superheroe['fuerza'])
            if fuerza < fuerza_minima:
                fuerza_minima = fuerza
                mas_debil = superheroe

    if mas_debil:
        return f"El superhéroe más débil es: {mas_debil['nombre']}, con fuerza {mas_debil['fuerza']}"
    else:
        return "No se encontraron superhéroes masculinos."


        
def contar_por_color_ojos(lista:list):
    """
    Cantidad por color de ojos. Determinar cuántos superhéroes tienen cada tipo de color de 
    ojos.
    """
    contador_ojos_azules = 0
    contador_ojos_rojos = 0
    contador_ojos_verdes = 0
    contador_ojos_amarillos = 0 
    contador_ojos_marrones = 0
    contador_ojos_plateados = 0
    contador_ojos_avellana = 0 

    for superheroe in lista:
        if superheroe['color_ojos'] == 'Brown':
            contador_ojos_marrones += 1
        elif superheroe['color_ojos'] == 'Blue':
            contador_ojos_azules += 1
        elif superheroe['color_ojos'] == 'Yellow':
            contador_ojos_amarillos += 1
        elif superheroe['color_ojos'] == 'Red':
            contador_ojos_rojos += 1
        elif superheroe['color_ojos'] == 'Silver':
            contador_ojos_plateados += 1
        elif superheroe['color_ojos'] == 'Hazel':
            contador_ojos_avellana += 1
        elif superheroe['color_ojos'] == 'Green':
            contador_ojos_verdes += 1

    colores = {
        'Brown': contador_ojos_marrones,
        'Blue': contador_ojos_azules,
        'Yellow': contador_ojos_amarillos,
        'Red': contador_ojos_rojos,
        'Silver': contador_ojos_plateados,
        'Hazel': contador_ojos_avellana,
        'Green': contador_ojos_verdes
    }
    
    colores_lista = list(colores.items()) 
    n = len(colores_lista)

    for i in range(n):
        for j in range(0, n-i-1):
            if colores_lista[j][1] < colores_lista[j+1][1]: 
                colores_lista[j], colores_lista[j+1] = colores_lista[j+1], colores_lista[j]  

    print("\nCantidad de personajes por color de ojos:")
    print(f"{'Color de Ojos':<15} | {'Cantidad':<10}")
    print("-" * 30)

    for color, cantidad in colores_lista:
        print(f"{color:<15} | {cantidad:<10}")


    
def ordenar_por_color_pelo(lista:list):
    """
    Listar por color de Pelo. Agrupar los superhéroes por color de pelo y mostrar sus nombres.
    """
    pelo_rojo = []
    pelo_negro = []
    pelo_verde = []
    pelo_rubio = []
    pelo_marron = []
    pelo_blanco = []
    calvos = []
    pelo_castano = []
    sin_pelo = []

    for superheroe in lista:
        if superheroe['color_pelo'] == 'Red':
            pelo_rojo.append(superheroe['nombre'])
        elif superheroe['color_pelo'] == 'Black':
            pelo_negro.append(superheroe['nombre'])
        elif superheroe['color_pelo'] == 'Green':
            pelo_verde.append(superheroe['nombre'])
        elif superheroe['color_pelo'] == 'Blond':
            pelo_rubio.append(superheroe['nombre'])
        elif superheroe['color_pelo'] == 'Brown':
            pelo_marron.append(superheroe['nombre'])
        elif superheroe['color_pelo'] == 'White':
            pelo_blanco.append(superheroe['nombre'])
        elif superheroe['color_pelo'] == 'No Hair':
            calvos.append(superheroe['nombre'])
        elif superheroe['color_pelo'] == 'Auburn':
            pelo_castano.append(superheroe['nombre'])
        elif superheroe['color_pelo'] == '':
            sin_pelo.append(superheroe['nombre'])

    colores = [
        ('Rojo', pelo_rojo),
        ('Negro', pelo_negro),
        ('Verde', pelo_verde),
        ('Rubio', pelo_rubio),
        ('Marrón', pelo_marron),
        ('Blanco', pelo_blanco),
        ('Calvo', calvos),
        ('Castaño', pelo_castano),
        ('""',sin_pelo)
    ]

    colores_ordenados = sorted(colores, key=lambda x: len(x[1]), reverse=True)
    
    print("\nSuperhéroes agrupados por color de pelo:")
    print(f"{'Color de Pelo':<15} | {'Superhéroes'}")
    print("-" * 50)

    for color, personajes in colores_ordenados:
        if personajes:
            print(f"{color:<15} | {', '.join(personajes)}")
        else:
            print(f"{color:<15} | {'Ninguno'}")


def ordenar_por_inteligencia(lista:list):
    """
    Listar inteligencia. Listar todos los superhéroes agrupados por tipo de inteligencia.
    """
    superheroes_int_good = []
    superheroes_int_average = []
    superheroes_int_high = []
    for superheroe in lista:
        if superheroe['inteligencia'] == 'good':
            superheroes_int_good.append(superheroe['nombre'])
        elif superheroe['inteligencia'] == 'average':
            superheroes_int_average.append(superheroe['nombre'])
        elif superheroe['inteligencia'] == 'high':
            superheroes_int_high.append(superheroe['nombre'])
    print("\nSuperheroes agrupados por inteligencia:")
    print(f"{'Nivel de inteligencia':<15} | {'Nombres'}")
    print("-"*50)
    
    print(f"{'Average':<15} | {', '.join(superheroes_int_average)}")
    print(f"{'Good':<15} | {', '.join(superheroes_int_good)}")
    print(f"{'High':<15} | {', '.join(superheroes_int_high)}")
def promediar_fuerza_f(lista:list):
    """
    Listar Promedio. Recorrer la lista y mostrar nombre y peso de los superhéroes (cualquier género) los cuales su fuerza supere a la fuerza promedio de todas las superhéroes de género femenino
    """
    acumulador_fuerza_f = 0
    contador_f = 0
    for superheroe in lista:
        if superheroe['genero'] == "F":
            acumulador_fuerza_f +=int(superheroe['fuerza'])
            contador_f +=1
    promedio_fuerza_f = acumulador_fuerza_f / contador_f
    return  promedio_fuerza_f
def superheroes_mas_fuertes(promedio_fuerza_f,lista:list):
    """
    Listar Promedio. Recorrer la lista y mostrar nombre y peso de los superhéroes (cualquier género) los cuales su fuerza supere a la fuerza promedio de todas las superhéroes de género femenino
    """
    superheroes_mas_fuertes = []
    for superheroe in lista:
        if int(superheroe['fuerza']) > promedio_fuerza_f:
            superheroes_mas_fuertes.append(superheroe['nombre'])
    print("\nSuperheroes con mas fuerza que el promedio femenino")
    print(f"{', '.join(superheroes_mas_fuertes)} ")
def calcular_imc(lista: list):
    """
    Calcular el IMC de cada superhéroe.
    """
    imc_lista = []
    for superheroe in lista:
        altura_m2 = float(superheroe['altura']) / 100  
        imc = float(superheroe['peso']) / (altura_m2 ** 2)  
        imc_lista.append(imc)
    return imc_lista

def agregar_imc(lista: list, imc_lista: list):
    """
    Asignar el IMC calculado a cada superhéroe usando una función lambda dentro de un bucle.
    """
    for superheroe, imc in zip(lista, imc_lista):
        (lambda superheroe, imc: superheroe.update({'IMC': imc}))(superheroe, imc)

def calcular_y_agregar_imc(lista: list):
    """
    Calcular el IMC de cada superhéroe y agregarlo a cada uno en el diccionario.
    """
    imc_lista = calcular_imc(lista)  
    agregar_imc(lista, imc_lista)  

    print(f"{'Nombre':<20} | {'Altura (cm)':<12} | {'Peso (kg)':<10} | {'IMC':<15}")
    print("-" * 60)
    for superheroe in lista:
        print(f"{superheroe['nombre']:<20} | {float(superheroe['altura']):.2f} | {float(superheroe['peso']):.2f} | {superheroe['IMC']:.2f}")


