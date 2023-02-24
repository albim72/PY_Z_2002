from aiomultiprocess import Pool
import signal
from multiprocessing import Manager
from functools import partial
import asyncio

class SignalHandler:
    KEEP_PROCESSING = True
    def __init__(self):
        signal.signal(signal.SIGINT, self.exit_gracefully)
        signal.signal(signal.SIGTERM, self.exit_gracefully)

    def exit_gracefully(self,signum,frame):
        print(signum)
        print("wyjście z gracją!")
        self.KEEP_PROCESSING = False

async def task(processing_flag):
    if processing_flag[0]:
        print("zadanie startuje....")
        await asyncio.sleep(5)
        print("wykonano!")

signal_handler = SignalHandler()

async def do_something():
    m = Manager()
    processing_flag = m.list([1])
    task_with_data = partial(task,processing_flag)
    async with Pool(processes=2, childconcurrency=3) as pool:
        while signal_handler.KEEP_PROCESSING:
            asyncio.create_task(pool.apply(task_with_data))
            await asyncio.sleep(0.0005)
        processing_flag[0]=0
        pool.close()
        await pool.join()

async def run():
    await do_something()

if __name__ == '__main__':
    asyncio.run(run())
