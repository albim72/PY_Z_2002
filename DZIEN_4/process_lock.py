from time import sleep
from random import random
from multiprocessing import Process,Lock

def task(lock,identifier,value):
    with lock:
        print(f'>>proces {identifier} zostanie zablokowany, opóźnienie: {value} s')
        sleep(value)

if __name__ == '__main__':
    lock = Lock()
    processes = [Process(target=task,args=(lock,i, random())) for i in range(10)]
    for process in processes:
        process.start()

    for process in processes:
        process.join()
