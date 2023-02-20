from funkcje.bfunkcje import *

class DKlasa:
    def __init__(self,lista,slownik):
        self.lista = lista
        self.slownik = slownik
        
    def czytajl(self):
        return czytajliste(self.lista)
    
    def czytajs(self):
        return czytajslownik(self.slownik)
        
