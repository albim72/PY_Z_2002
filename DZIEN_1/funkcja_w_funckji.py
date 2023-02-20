#przykład 1

def witaj(imie):
    return f"miło Cię widzieć {imie}"

def konkurs(imie,punkty):
    return f"uczetnik konkursu {imie} otrzymał {punkty} punktów"

def osoba(funkcja,*args):
    return funkcja(*args)

print(osoba(witaj,"Leon"))
print(osoba(konkurs,"Olga",67))


#przykład 2

def rejestracja(oplata):
    def lista():
        return "jesteś na liście zawodników"
    def brak():
        return "jeśli nie uiścisz opłaty startowej zostaniesz usunięty z listy startowej"
    def error():
        return "brak potwierdzenia, podaj wartość 1 -> opłata, 0->brak opłaty"

    if oplata == 1:
        return lista
    elif oplata == 0:
        return brak
    else:
        return error

print(rejestracja(1)())
print(rejestracja(0)())
print(rejestracja(13)())

#przykład 3




