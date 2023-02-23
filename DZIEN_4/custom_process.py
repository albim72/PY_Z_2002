from time import sleep
from multiprocessing import Process
from multiprocessing import Value

class CustomProcess(Process):
    def __init__(self):
        Process.__init__(self)
        self.data = Value('i',0)

    def run(self) -> None:
        sleep(1)
        self.data.value = 99
        print(f'Child składuje: {self.data.value}')

if __name__ == '__main__':
    process = CustomProcess()
    process.start()
    print('Oczekiwanie na zakończenie procesu Child....')
    process.join()
    print(f'Proces Parent posiada wartość: {process.data.value}')


