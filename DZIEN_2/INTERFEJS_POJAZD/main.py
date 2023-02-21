from pojazd import Pojazd

p1 = Pojazd()
odl = float(input("podaj odległość [km]: "))
litry = float(input("podaj liczbę litrów paliwa [spalonych]: "))
cn = float(input("podaj cenę litra paliwa [zł]: "))


print(f'spalanie [l/100km]: {p1.spalanie_100(litry,odl):.2f}')
print(f'koszty przejazdu na trasie {odl} km -> {p1.kosztyprzejazdu(litry,odl,cn):.2f} zł')
