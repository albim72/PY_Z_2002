liczby = [999,45,67,8,9,123,0,-456,-789,134,1109,678,234,12,3,89,-7,16,99]

def pokaz_statystyki(lista):
    minimum = min(lista)
    maksimum = max(lista)
    rozstep = maksimum - minimum
    suma = sum(lista)
    liczba_el = len(lista)
    avg = suma/liczba_el
    return minimum,maksimum,rozstep,suma,liczba_el,avg

wynik = pokaz_statystyki(liczby)
print(wynik)
print(type(wynik))

mini,maxi,roz,sm,le,av = pokaz_statystyki(liczby)
print(f"wartość -> największa: {maxi}, najmniejsza: {mini}, rozstęp: {roz}, suma: {sm}, "
      f"liczbe elementów: {le}, średnia arytmetyczna: {av:.2f}")
