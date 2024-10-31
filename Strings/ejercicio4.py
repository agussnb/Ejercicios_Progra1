# Desarrollar una función que convierta los elementos de lista_peli en una 
# cadena y muestre: 
# ej. "Se recomienda ver "Matrix", "El Padrino" y "Titanic" "" para cada elemento
lista_peli = [
 ["Matrix", "El Padrino", "Titanic"],
 ["Forrest Gump", "Pulp Fiction", "Gladiador"], 
 ["Blade Runner", "El Rey León", "Volver al Futuro"], 
 ["La La Land", "El Gran Lebowski", "Blade Runner"], 
 ["Jurassic Park", "Avatar", "El Resplandor", "El Sexto Sentido"],
 ["Harry Potter", "Forrest Gump", "Pulp Fiction"],
 ["Titanic", "Star Wars", "El Señor de los Anillos"], 
 ["The Truman Show", "The Shape of Water", "The Big Lebowski"], 
 ["Forrest Gump", "The Godfather", "Goodfellas"],
 ["The Terminator", "The Sixth Sense", "The Great Gatsby"]
]
def peliculas_recomendadas():
    pelis = ' '.join(lista_peli[0])
    print(f"Se recomienda ver {pelis}")
            
peliculas_recomendadas()