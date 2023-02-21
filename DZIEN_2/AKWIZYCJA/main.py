"""
Przykład na użycie konstruktora __repr__
class A:
    def __init__(self,n):
        self.n= n

    def __str__(self):
        return f"wartość x  = {self.n} by __str__"

    def __repr__(self):
        return f"wartość x  = {self.n}"

oba = A(5)
print(oba)"""

from decimal import Decimal
from akwizytor import Akwizytor
from akwizytornaetacie import AkwizytorNaEtacie

class Boss:

    def __repr__(self):
        return 'Szef otrzymuje stały ryczałt!'

    def zarobek(self):
        return Decimal('12_000_000.00')

b = Boss()
s = Akwizytor('Jan','Kot','456342543',Decimal('457900.00'),Decimal('5.5'))
c = AkwizytorNaEtacie('Olga','Nowak','9458498',Decimal('420900.00'),Decimal('4.6'),Decimal('4500'))

pracownicy = [c,s,b]
for p in pracownicy:
    print(p)
    print(f'zarobek: {p.zarobek():,.2f}\n')
