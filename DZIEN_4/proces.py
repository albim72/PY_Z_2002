from time import sleep
from multiprocessing import Process

def task():
    sleep(1)
    print('ta wiadomość pochodzi z innego procesu')

if __name__ == '__main__':
    process = Process(target=task)
    process.start()
    print('oczekiwanie na proces...')
    process.join()
