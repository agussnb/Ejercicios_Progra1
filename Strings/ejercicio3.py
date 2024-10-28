# Desarrollar una función que reemplaza una palabra específica por otra 
# en una cadena.

def reemplazar_palabra(string:str) ->str:
    string_separado = string.split()
    string_reemplazado = string.replace(string_separado[2],"Edificio")
    print(f"El string original era {string} y se reemplazo {string_separado[2]} con 'Edificio' y el resultado final es {string_reemplazado}")

resultado = 'Tecnicatura en Programacion'
reemplazar_palabra(resultado)

