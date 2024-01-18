import asyncio
from time import perf_counter
from aiohttp import ClientSession

t1 = perf_counter()


async def get_weather(city):
    async with ClientSession() as session:
        url = f'http://api.openweathermap.org/data/2.5/weather'
        params = {
            'q': city,
            'APPID': '2a4ff86f9aaa70041ec8e82db64abf56',
            'units': 'metric'
        }

        async with session.get(url=url, params=params) as response:
            weather_json = await response.json()
            print(f'{city}: {weather_json["weather"][0]["main"]}({weather_json["weather"][0]["description"]})')
            print(
                f'Temperature: {weather_json["main"]["temp"]:.1f}\N{DEGREE SIGN}c Feels Like: {weather_json["main"]["feels_like"]:.1f}\N{DEGREE SIGN}c\n')


async def main(cities_):
    tasks = []
    for city in cities_:
        tasks.append(asyncio.create_task(get_weather(city)))

    for task in tasks:
        await task


cities = ['Samara', 'Pskov', 'Moscow', 'St. Petersburg', 'Szczecin']
asyncio.run(main(cities))

t2 = perf_counter()
print(f'Working time: {t2 - t1:.5f} sec')
