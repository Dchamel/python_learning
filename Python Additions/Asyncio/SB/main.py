# # new event loop
# import asyncio
#
# async def main() -> None:
#     await asyncio.sleep(1)
#
#
# loop = asyncio.new_event_loop()
# try:
#     loop.run_until_complete(main())
# finally:
#     loop.close()

# # --------------------------------------------------------------------------------
# import asyncio
#
#
# def call_later() -> None:
#     print("Calling later")
#
#
# async def delay(delay_seconds: int) -> int:
#     print(f"Delaying {delay_seconds}")
#     await asyncio.sleep(delay_seconds)
#     print('continue after "call_later"')
#     print(f"Delayed {delay_seconds}")
#     return delay_seconds
#
#
# # I just Announced it in advance
# # async def fetch_status(session: ClientSession, url: str) -> int:
# #     async with session.get(url) as result:
# #         return result.status
#
#
# async def main() -> None:
#     # get existing event loop
#     loop = asyncio.get_running_loop()
#     # create new event loop if it not exists(instruction recommends use get_running_loop
#     # because creating new event loop with get_event_loop may cause unforeseen consequences)
#     # loop = asyncio.get_event_loop()
#     loop.call_soon(call_later)
#     await delay(2)
#
#
# asyncio.run(main())

# # --------------------------------------------------------------------------------
# import asyncio
# import time
# from time import perf_counter
#
#
# def working_time(func):
#     async def wrapper():
#         t1 = perf_counter()
#         wr_fun = await func()
#         t2 = perf_counter()
#         print(f'Working time: {t2 - t1:.2f} seconds')
#         return wr_fun
#
#     return wrapper
#
#
# async def delay(delay_seconds: int) -> int:
#     print(f"Delaying {delay_seconds}")
#     await asyncio.sleep(delay_seconds)
#     print('continue after "call_later"')
#     print(f"Delayed {delay_seconds}")
#     return delay_seconds
#
#
# async def task_no_sleep() -> None:
#     task1 = asyncio.create_task(delay(1))
#     task2 = asyncio.create_task(delay(2))
#     print('Task 1 started (gather)')
#     await asyncio.gather(task1, task2)
#
#
# async def task_with_sleep() -> None:
#     task1 = asyncio.create_task(delay(1))
#     await asyncio.sleep(0)
#     task2 = asyncio.create_task(delay(2))
#     await asyncio.sleep(0)
#     print('Task 2 started (gather)')
#     await asyncio.gather(task1, task2)
#
#
# @working_time
# async def main() -> None:
#     print('Starting main loop - task_no_sleep')
#     await task_no_sleep()
#     print('Starting main loop - task_with_sleep')
#     await task_with_sleep()
#     # time.sleep(1)
#
#
# asyncio.run(main())

# # Working with Lock
# # --------------------------------------------------------------------------------
# import asyncio
# from asyncio import Lock
# from time import perf_counter
#
#
# def working_time(func):
#     async def wrapper():
#         t1 = perf_counter()
#         wr_fun = await func()
#         t2 = perf_counter()
#         print(f'Working time: {t2 - t1:.2f} seconds')
#         return wr_fun
#
#     return wrapper
#
#
# async def delay(delay_seconds: int) -> int:
#     print(f"Delaying {delay_seconds}")
#     await asyncio.sleep(delay_seconds)
#     print('continue after "call_later"')
#     print(f"Delayed {delay_seconds}")
#     return delay_seconds
#
#
# async def increment(lock):
#     async with lock:
#         global counter
#         tmp_counter = counter
#         tmp_counter += 1
#         await asyncio.sleep(0.01)
#         counter = tmp_counter
#
#
# @working_time
# async def main() -> None:
#     global counter
#     lock = Lock()
#     for _ in range(1000):
#         tasks = [asyncio.create_task(increment(lock)) for _ in range(100)]
#         await asyncio.gather(*tasks)
#         print(f'Counter is: {counter}')
#         assert counter == 100
#         counter = 0
#
#
# if __name__ == '__main__':
#     counter: int = 0
#     asyncio.run(main())

# Working with Semaphore
# --------------------------------------------------------------------------------
import asyncio
from asyncio import Semaphore
from time import perf_counter
# for types
from typing import Callable


def working_time(func: Callable) -> Callable:
    async def wrapper():
        t1 = perf_counter()
        wr_fun = await func()
        t2 = perf_counter()
        print(f'Working time: {t2 - t1:.2f} seconds')
        return wr_fun

    return wrapper


async def delay(delay_seconds: int) -> int:
    print(f"Delaying {delay_seconds}")
    await asyncio.sleep(delay_seconds)
    print('continue after "call_later"')
    print(f"Delayed {delay_seconds}")
    return delay_seconds


@working_time
async def main() -> None:
    pass


if __name__ == '__main__':
    asyncio.run(main())
