class Pierwsza:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.pierwszacr()

    def pierwszacr(self):
        print("powstał obiekt klasy Pierwsza")

    def policz(self):
        return self.x*self.y

class Dodatkowa:
    def __init__(self,h,k):
        self.h=h
        self.k=k
        self.dodatkowacr()

    def dodatkowacr(self):
        print("powstał obiekt klasy Dodatkowa")

    def policzhk(self):
        return self.h - self.k


class Druga(Pierwsza,Dodatkowa):
    pass

