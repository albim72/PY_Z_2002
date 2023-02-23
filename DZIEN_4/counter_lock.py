import threading
import time
import random

class Counter(object):
    def __init__(self,strart=0):
        self.lock = threading.Lock()
        self.value = strart

    def increment(self):
        print('oczekiwanie na zablokowanie wątku....')
        self.lock.acquire()
        try:
            print("zablokowanie wątku...")
            self.value = self.value + 1
        finally:
            print("odblokowanie wątku...")
            self.lock.release()

def worker(c):
    for i in range(2):
        r = random.random()
        print(f'wartość[czas oczekiwania] r: {r:.2f}')
        time.sleep(r)
        c.increment()
    print("Wykonane....")

if __name__ == '__main__':
    counter = Counter()
    for i in range(2):
        t = threading.Thread(target=worker,args=(counter,))
        t.start()

    print('oczekiwanie na wątki robocze...')
    mainthread = threading.currentThread()
    for t in threading.enumerate():
        if t is not mainthread:
            t.join()
    print(f"counter: {counter.value}")
