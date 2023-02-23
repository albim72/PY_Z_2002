import time
import asyncio

def count():
    print("początek...")
    time.sleep(1)
    print("ważna informacja")

async def countas():
    print("początek...")
    await asyncio.sleep(1)
    print("ważna informacja")

def printczas(info):
    s = time.perf_counter()
    print(info)
    k = time.perf_counter()
    print(f"czas potrzebny na wyposanie kominukatu [print()]: {k-s} s")

def main():
    for _ in range(3):
        count()

async def mainas():
    await asyncio.gather(countas(),countas(),countas())

if __name__ == '__main__':
    s = time.perf_counter()
    main()
    elapsed = time.perf_counter() - s
    print(f"{__file__} został wykonany w  {elapsed:.2f} s")

    s = time.perf_counter()
    asyncio.run(mainas())
    elapsed = time.perf_counter() - s
    print(f"{__file__} został wykonany [asynchronicznie] w  {elapsed:.2f} s")
    printczas("badamy czas potrzebny na wyświetlenie komunikatu...")
