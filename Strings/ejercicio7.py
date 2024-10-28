# Desarrollar una función “ordenar” que recibe un string y un número (1 o 
# -1). Se debe retornar el string ordenado de manera ascendente (si recibió 1 por 
# parámetros) o descendente (si recibió -1)
# Nota: Determinar parámetros y retornos de manera que las funciones sean 
# genéricas y reutilizables.

def ordenar(string: str, numero: int) -> str:
    resultado = ""

    for _ in range(len(string)):
        minimo_o_maximo = None
        
        for caracter in string:
            if numero == 1:
                if minimo_o_maximo is None or (caracter < minimo_o_maximo):
                    minimo_o_maximo = caracter
            
            elif numero == -1:
                if minimo_o_maximo is None or (caracter > minimo_o_maximo):
                    minimo_o_maximo = caracter
        
        resultado += minimo_o_maximo
        string = string.replace(minimo_o_maximo, "", 1)  
        
    return resultado


prueba1 = ordenar('Feliz Navidad',1)
print(prueba1)
print('--------------------------')
prueba2 = ordenar('Feliz Navidad',-1)
print(prueba2)
    
