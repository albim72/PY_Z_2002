import math
import time

def pomiarczasu(funkcja):
    def wrapper():
        starttime = time.perf_counter()
        funkcja()
        endtime = time.perf_counter()
        print(f"czasy wykonania funkcji {funkcja.__name__} -> {endtime-starttime} s")
    return wrapper

def sleep(funkcja):
    def wrapper():
        time.sleep(3)
        return funkcja()
    return wrapper


@pomiarczasu
@sleep
def big_lista():
    sum([i**7 for i in range(1000000)])

big_lista()

def debug(funkcja):
    def wrapper(*args,**kwargs):
        print(f'wołana funckja: {funkcja.__name__}')
        funkcja(*args,**kwargs)
    return wrapper

@debug
def info(inn):
    print(f"informacja: {inn}")


info("ABC 123")

def repeater(n):
    def wrapper(funkcja):
        def inner(*args):
            for i in range(n):
                funkcja(*args)
        return inner
    return wrapper


@repeater(n=8)
def komunikat(k,n):
    print(f'komunikat: {n*k}')

komunikat('xyz',4)

komunikat(6,9.9)


