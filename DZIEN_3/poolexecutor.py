from concurrent.futures import ProcessPoolExecutor
from time import sleep

def task(message):
    sleep(2)
    return message

def main():
    executor = ProcessPoolExecutor()
    future = executor.submit(task,("Zakończone!"))
    print(future.done())
    sleep(2)
    print(future.done())
    print(future.result())

if __name__ == '__main__':
    main()
