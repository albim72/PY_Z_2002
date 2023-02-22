from numba import jit, cuda
from timeit import default_timer as timer
import numpy as np

def policz(a):
    for i in range(10000000):
        a[i]+=1

@jit(target_backend='cuda')
def policz_g(a):
    for i in range(10000000):
        a[i]+=1
if __name__ == '__main__':
    n = 10000000
    a = np.ones(n,dtype=np.float64)

    start = timer()
    policz(a)
    print(f"obliczenie na CPU: {timer()-start} s")

    start = timer()
    policz_g(a)
    print(f"obliczenie na GPU: {timer() - start} s")
    
