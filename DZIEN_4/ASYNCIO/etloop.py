import asyncio

async def main():
    while True:
        print('<Twoja aplikacja działa....>')
        await asyncio.sleep(1)

loop = asyncio.get_event_loop()
task = loop.create_task(main())
try:
    loop.run_until_complete(task)
except KeyboardInterrupt:
    print('Odebrano sygnał: SIGINT, zamykanie aplikacji...')

tasks = asyncio.all_tasks(loop=loop)
for t in tasks:
    t.cancel()
group = asyncio.gather(*tasks,return_exceptions=True)
loop.run_until_complete(group)
loop.close()
