def czytajliste(lista):
    for i,j in enumerate(lista):
        print(f"element listy nr {i+1} -> {j}")
        
def czytajslownik(slownik):
    for x,y in slownik.items():
        print(f"klucz -> {x}: wartość > {y}")
