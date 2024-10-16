# Crear una función que reciba como parámetro una cadena y determine si la
# misma es o no un palíndromo. Deberá retornar un valor booleano indicando
# lo sucedido.
def es_palindromo(cadena):
    cadena = cadena.replace(" ", "").lower()

    return cadena == cadena[::-1]

cadena = "Anita lava la tina"
resultado = es_palindromo(cadena)

if resultado:
    print(f"La cadena '{cadena}' es un palíndromo.")
else:
    print(f"La cadena '{cadena}' no es un palíndromo.")

