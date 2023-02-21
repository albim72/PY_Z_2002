import math
from figura import Figura

class Kolo(Figura):

    def __init__(self, a):
        super().__init__(a, None)

    def policz_pole(self):
        return math.pi*self.a**2

    def opis(self):
        pass
