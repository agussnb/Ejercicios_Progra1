# Crear una clase Libro que tenga las características títuto, autor y año de publicación. Del libro se 
# debe poder obtener información, mostrando por mensaje todos sus datos. Se debe crear la clase 
# e implementarla.

class Libro():
    def __init__(self, titulo:str, autor:str, publicacion:int):
        self.titulo = titulo
        self.autor = autor
        self.publicacion = publicacion
    def return_data(self) -> str:
        return 'Título: {}, Autor: {}, Año de Publicación: {}'.format(self.titulo, self.autor, self.publicacion)
        

libro = Libro('Un mounstro viene a verme','Patrick Ness',2011)

print(libro.return_data())