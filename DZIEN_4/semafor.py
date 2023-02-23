from time import sleep
from random import random
from threading import Thread
from threading import Semaphore


#target function
def task(semaphore,number):
    with semaphore:
        value = random()
        sleep(value)
        print(f"Wątek {number} -> wartość: {value}")

semaphore = Semaphore()
for i in range(10):
    worker = Thread(target=task,args=(semaphore,i))
    worker.start()
