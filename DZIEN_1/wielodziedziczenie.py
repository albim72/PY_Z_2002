class Pierwsza:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.pierwszacr()

    def pierwszacr(self):
        print("powstał obiekt klasy Pierwsza")

    def policz(self):
        return self.x*self.y
    
class Tajna:
    def __init__(self,paleta):
        self.paleta = paleta
        self.kolor = 'black'
        
    def printcolor(self):
        return f"kolor: {self.kolor}, paleta: {self.paleta}"
    
    def setcolor(self,nkolor):
        self.kolor = nkolor

class Dodatkowa(Tajna):
    def __init__(self,h,k,paleta):
        super().__init__(paleta)
        self.h=h
        self.k=k
        self.dodatkowacr()

    def dodatkowacr(self):
        print("powstał obiekt klasy Dodatkowa")

    def policzhk(self):
        return self.h - self.k


class Druga(Pierwsza,Dodatkowa):
    pass

