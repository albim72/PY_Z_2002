import time
import asyncio

async def main():
    loop = asyncio.get_running_loop()
    loop.run_in_executor(None,blocking)
    print(f'{time.ctime()} Witaj!')
    await asyncio.sleep(1.0)
    print(f'{time.ctime()} Żegnaj!')

def blocking():
    time.sleep(1.5)
    print(f"{time.ctime()} powitanie z wątku!")

if __name__ == '__main__':
    asyncio.run(main())
