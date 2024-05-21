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

import asyncio


def call_later() -> None:
    print("Calling later")


async def delay(delay_seconds: int) -> int:
    print(f"Delaying {delay_seconds}")
    await asyncio.sleep(delay_seconds)
    print('continue after "call_later"')
    print(f"Delayed {delay_seconds}")
    return delay_seconds


# I just Announced it in advance
# async def fetch_status(session: ClientSession, url: str) -> int:
#     async with session.get(url) as result:
#         return result.status


async def main() -> None:
    # get existing event loop
    loop = asyncio.get_running_loop()
    # create new event loop if it not exists(instruction recommends use get_running_loop
    # because creating new event loop with get_event_loop may cause unforeseen consequences)
    # loop = asyncio.get_event_loop()
    loop.call_soon(call_later)
    await delay(2)


asyncio.run(main())
