#n! = 1*2*3*...*n
#1.8E+308
#171!
import sys
sys.set_int_max_str_digits(1000000)
sys.setrecursionlimit(0x1000000)

def silnia(n):
    if n<0:
        raise ValueError('silnia dla liczb ujemnych jest niezdefiniowana...')
    wynik = 1
    for i in range(1,n+1):
        wynik*=i
    return wynik

def silnia_rek(n):
    if n<0:
        raise ValueError('silnia dla liczb ujemnych jest niezdefiniowana...')
    if n==0:
        return 1
    else:
        return n*silnia_rek(n-1)


try:
    n = int(input("podaj argument silnii n: "))
    print(f'dla n = {n} silnia wynosi: {silnia(n)}')
    print(f'dla n = {n} silnia rekurencyjna wynosi: {silnia_rek(n)}')
except ValueError as v:
    print(v)
