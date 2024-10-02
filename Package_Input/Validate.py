def validate_int(valor: int, minimo: int, maximo: int) -> bool:
    return minimo <= valor <= maximo

def validate_float(valor: float, minimo: float, maximo: float) -> bool:
    return minimo <= valor <= maximo

def validate_string(valor:str,longitud:int) -> bool:
    return len(valor) <= longitud