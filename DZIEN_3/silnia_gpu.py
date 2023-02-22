#n! = 1*2*3*...*n
#1.8E+308
#171!
import sys
from numba import jit, cuda
from timeit import default_timer as timer
sys.setrecursionlimit(0x1000000)

def silnia_rek(n):
    if n<0:
        raise ValueError('silnia dla liczb ujemnych jest niezdefiniowana...')
    if n==0:
        return 1
    else:
        return n*silnia_rek(n-1)

@jit(target_backend='cuda')
def silnia_rek_gpu(n):
    if n<0:
        raise ValueError('silnia dla liczb ujemnych jest niezdefiniowana...')
    if n==0:
        return 1
    else:
        return n*silnia_rek_gpu(n-1)

@jit(target_backend='cuda')
def silnia_2(n):
    if n<0:
        raise ValueError('silnia dla liczb ujemnych jest niezdefiniowana...')
    wynik = 1
    for i in range(1,n+1):
        wynik*=i
    return wynik


try:
    n = int(input("podaj argument silnii n: "))
    start = timer()
    print(f'dla n = {n} silnia rekurencyjna wynosi: {silnia_rek(n)}')
    print(f"czas wykonania na CPU: {timer() - start} s")
    start = timer()
    print(f'dla n = {n} silnia rekurencyjna GPU wynosi: {silnia_rek_gpu(n)}')
    print(f"czas wykonania na GPU: {timer() - start} s")
    start = timer()
    print(f'dla n = {n} silnia iteracyjna GPU wynosi: {silnia_2(n)}')
    print(f"czas wykonania na GPU: {timer() - start} s")
except ValueError as v:
    print(v)
