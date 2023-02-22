import time
import concurrent.futures

value = [8000000,7000000]

def counting(n):
    start = time.time()
    while n >0:
        n-=1
    return time.time()-start

def procmain():
    start = time.time()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for number, time_taken in zip(value,executor.map(counting,value)):
            print(f'start: {number} -> czas: {time_taken} s')
    print(f'czas całkowity: {time.time() - start} s')

def threadmain():
    start = time.time()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        for number, time_taken in zip(value,executor.map(counting,value)):
            print(f'start: {number} -> czas: {time_taken} s')
    print(f'czas całkowity: {time.time() - start} s')

if __name__ == '__main__':
    print("ProcessPoolExecutor()")
    procmain()
    print("ThreadPoolExecutor()")
    threadmain()
