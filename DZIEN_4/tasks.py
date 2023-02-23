import threading
import os

def task1():
    print(f"task 1 melduje się w wątku... {threading.current_thread().name}")
    print(f"ID procesu dla task 1: {os.getpid()}")

def task2():
    print(f"task 2 melduje się w wątku... {threading.current_thread().name}")
    print(f"ID procesu dla task 2: {os.getpid()}")

if __name__ == '__main__':
    print(f"ID procesu dla progamu głównego: {os.getpid()}")
    print(f"Główny wątek: {threading.current_thread().name}")

    t1 = threading.Thread(target=task1, name='t1')
    t2 = threading.Thread(target=task2, name='t2')

    t1.start()
    t2.start()
    t1.join()
    t2.join()
