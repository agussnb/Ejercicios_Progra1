# Crear una clase Animal que tenga la característica nombre. La clase Perro que herede de Animal 
# las características y realice el sonido “guau guau”. La clase Gato que herede de Animal las 
# características y realice el sonido “Miau”. Del gato y el perro se debe poder mostrar el sonido que 
# realizan. Se debe crear la clase e implementarla.

class Animal:
    def __init__(self, edad: int, patas: int, raza: str, sexo: str):
        self.edad = edad
        self.patas = patas
        self.raza = raza
        self.sexo = sexo

class Perro(Animal):
    def __init__(self, edad: int, raza: str, sexo: str):
        super().__init__(edad, 4, raza, sexo)

    def ruido(self):
        return 'guau guau'

class Gato(Animal):
    def __init__(self, edad: int, patas: int, raza: str, sexo: str):
        super().__init__(edad, patas, raza, sexo)

    def ruido(self):
        return 'miau'

perro = Perro(2, "Caniche", "Macho")
gato = Gato(4, 4, "Naranja", "Macho")

print(f'El perro hace {perro.ruido()} y el gato hace {gato.ruido()}')