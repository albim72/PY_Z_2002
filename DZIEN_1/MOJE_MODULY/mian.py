#import dane
#import dane as dn
from dane import nbf as filia
from dane import book as ksiazka
from funkcje.bfunkcje import czytajliste,czytajslownik

print("_______wypisanie bezpośrednio_________")
print(filia)
print(ksiazka)

print("_______wypisanie za pomocą funckji_________")
czytajliste(filia)
czytajslownik(ksiazka)
