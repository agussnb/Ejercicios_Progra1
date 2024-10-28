# Crear una clase Persona que tenga las características nombre y edad. La persona debe poder 
# mostrar un mensaje saludando presentándose con su nombre y edad. Se debe crear la clase e 
# implementarla.

class Persona():
    def __init__(self, nombre:str, edad:int):
        self.nombre = nombre
        self.edad = edad

persona_uno = Persona('Mati',21)
print(f'Hola! mi nombre es {persona_uno.nombre} y mi edad es {persona_uno.edad}')