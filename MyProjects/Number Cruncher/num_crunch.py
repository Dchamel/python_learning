import asyncio, time
from concurrent.futures import ThreadPoolExecutor
from time import perf_counter

t1 = perf_counter()


def num_crunch():
    for i in range(10000000):
        _ = i ** 3


async def main(n):
    loop = asyncio.get_running_loop()

    with ThreadPoolExecutor() as pool:
        tasks = [loop.run_in_executor(pool, num_crunch) for _ in range(n)]

        await asyncio.gather(*tasks)


n = 3
asyncio.run(main(n))

t2 = perf_counter()
print(f'Working time: {t2 - t1:.2f} sec')
