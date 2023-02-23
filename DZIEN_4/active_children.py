from time import sleep
from multiprocessing import active_children
from multiprocessing import Process,cpu_count

def task():
    sleep(1)

if __name__ == '__main__':
    #tworzenie kilku procesu typu child
    processes = [Process(target=task) for _ in range(5)]

    for process in processes:
        process.start()
    #wszystkie aktywne procesy Child
    children = active_children()

    print(f'Liczba aktywnych procesów Child: {len(children)}')
    for child in children:
        print(child)

    num_cores = cpu_count()
    print(f'liczba rdzeni... {num_cores}')
