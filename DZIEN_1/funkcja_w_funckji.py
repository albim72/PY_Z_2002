#przykład 1

def witaj(imie):
    return f"miło Cię widzieć {imie}"

def konkurs(imie,punkty):
    return f"uczetnik konkursu {imie} otrzymał {punkty} punktów"

def osoba(funkcja,*args):
    return funkcja(*args)

print(osoba(witaj,"Leon"))
print(osoba(konkurs,"Olga",67))
