import time
import concurrent.futures
from sum_prime_number import find_prime_numbers_sum

numbers = [(1,10000),(3,50000),(5000,100000),(4,900),(800,15000)]

def synchroniczna():
    starttime = time.time()
    for pair in numbers:
        prime_sum = find_prime_numbers_sum(*pair)
        print(prime_sum)
    endtime = time.time()
    print(f'Total time to crunch prime numbers - synchronic: {endtime-starttime:.2f} s')

def run_heavy_function(params):
    return find_prime_numbers_sum(*params)

def asynchroniczna():
    starttime = time.time()
    with concurrent.futures.ProcessPoolExecutor(max_workers=7) as executor:
        result = executor.map(run_heavy_function,numbers)
    print(list(result))
    endtime = time.time()
    print(f'Total time to run multitreads - asynchronic: {endtime-starttime:.2f} s')


if __name__ == '__main__':
    synchroniczna()
    asynchroniczna()
