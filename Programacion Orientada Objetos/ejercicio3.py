# Crear una clase rectángulo que tenga las características base y altura. Del rectángulo se debe 
# poder calcular el área y el perímetro. Se debe crear la clase e implementarla

class Rectangulo():
    def __init__(self, base:int, altura:int):
        self.base = base
        self.altura = altura
    def calcular_area(self) -> int:
        return self.base * self.altura
    def calcular_perimetro(self) -> int:
        return 2*(self.base+self.altura)
    

rectangulo = Rectangulo(20,10)
print(f'La base del rectangulo es {rectangulo.base} y la altura es {rectangulo.altura} por lo tanto, su area es {rectangulo.calcular_area()} y su perimetro es {rectangulo.calcular_perimetro()}')