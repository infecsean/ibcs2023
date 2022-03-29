# networking/nonblocking/async_test.py

import asyncio
import time


async def message(message: str, delay: int = 2):
    await asyncio.sleep(delay)
    print(message)


async def no_tasks():
    print(f"Started at {time.strftime('%X')}")

    tasks = []
    delay = 1
    for i in range(3):
        tasks.append(message(f"First Loop {i}", delay))

    delay = 2
    for i in range(3):
        tasks.append(message(f"Second loop {i}", delay))

    for task in tasks:
        await task

    print(f"Finished at {time.strftime('%X')}")


if __name__ == "__main__":
    asyncio.run(no_tasks())
