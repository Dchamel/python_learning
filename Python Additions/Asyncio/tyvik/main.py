# tyvik.ru/posts/asyncio-for-the-working-python-developer

import time
from collections import namedtuple
from time import sleep, perf_counter
import asyncio
from concurrent.futures import FIRST_COMPLETED, ALL_COMPLETED
from typing import Callable

import aiohttp


def working_time(func: Callable) -> Callable:
    async def wrapper():
        t1 = perf_counter()
        wr_fun = await func()
        t2 = perf_counter()
        print(f'Working time: {t2 - t1:.2f} seconds')
        return wr_fun

    return wrapper


async def fetch_ip(service):
    t1 = time.time()
    print(f'Fetching IP from{service.name}...')
    # response = await aiohttp.request('GET', service.url)
    async with aiohttp.request('GET', service.url) as response:
        json = await response.json()
        ip = json[service.ip_attr]

    return f'{service.name} : {ip}, took {time.time() - t1} seconds'


async def asynchronous():
    futures = [fetch_ip(service) for service in services]
    done, pending = await asyncio.wait(
        futures, return_when=ALL_COMPLETED
    )
    print(done.pop().result())

    for future in pending:
        future.cancel()


# @working_time
# def main() -> None:
#     pass


if __name__ == '__main__':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    service = namedtuple('Service', ['name', 'url', 'ip_attr'])

    services = (
        # service('ipify', 'https://api.ipify.org?format=json', 'ip'),
        service('ip-api', 'http://ip-api.com/json', 'query')
    )
    ioloop = asyncio.get_event_loop()
    ioloop.run_until_complete(asynchronous())
    ioloop.close()
