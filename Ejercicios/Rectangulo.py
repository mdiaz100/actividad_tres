from Punto import Punto


class Rectangulo:

    def __init__(self, punto_1: Punto, punto_2: Punto):
        self.punto_1: Punto = punto_1
        self.punto_2: Punto = punto_2

    def calcular_area(self):
        base = abs(self.punto_2.x - self.punto_1.x)
        altura = abs(self.punto_2.y - self.punto_1.y)
        return base * altura

    def calcular_perimetro(self):
        base = abs(self.punto_2.x - self.punto_1.x)
        altura = abs(self.punto_2.y - self.punto_1.y)
        return (base + altura) * 2

    def es_cuadrado(self):
        base = abs(self.punto_2.x - self.punto_1.x)
        altura = abs(self.punto_2.y - self.punto_1.y)
        return base == altura
