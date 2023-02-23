from time import sleep
from multiprocessing import Process,Condition

def task(condition):
    sleep(1)
    print('Proces Child wysyła notyfikację...',flush=True)
    with condition:
        condition.notify()
    sleep(1)


if __name__ == '__main__':
    condition = Condition()
    print(f"proces główny czeka na dane...")
    with condition:
        worker = Process(target=task,args=(condition,))
        worker.start()
        condition.wait()
    print("Proces główny wykonał całość...")
