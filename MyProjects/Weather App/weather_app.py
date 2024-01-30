import asyncio
# import json
# import os
# from dotenv import load_dotenv
from time import perf_counter
from aiohttp import ClientSession, web
from aiologger.loggers.json import JsonLogger

from googletrans import Translator

t1 = perf_counter()

# load_dotenv()
# yapi_key = os.environ['GOOGLE_API_KEY']

logger = JsonLogger.with_default_handlers(
    level='DEBUG',
    serializer_kwargs={'ensure_ascii': False},
)


async def get_weather(city: str) -> list:
    async with ClientSession() as session:
        url = f'http://api.openweathermap.org/data/2.5/weather'
        params = {
            'q': city,
            'APPID': '2a4ff86f9aaa70041ec8e82db64abf56',
            'units': 'metric'
        }

        async with session.get(url=url, params=params) as response:
            weather_json = await response.json()
            try:
                city_main = f'{city}: {weather_json["weather"][0]["main"]}({weather_json["weather"][0]["description"]})'
                city_temp = f'Temperature: {weather_json["main"]["temp"]:.1f}\N{DEGREE SIGN}c Feels Like: {weather_json["main"]["feels_like"]:.1f}\N{DEGREE SIGN}c\n'
                city_weather = [city_main, city_temp]
                return city_weather
            except KeyError:
                return 'No data'
            # print(json.dumps(weather_json, indent=4))


# Finally make it works but only with googletrans==3.1.0a0
def get_translation(text, main='en', dest='ru'):
    translator = Translator()
    try:
        translated_list = translator.translate(text, src=main, dest=dest)
        translated_text = '\n'.join([i.text for i in translated_list])
    except KeyError:
        logger.error(f"Can't translate: {text}")
        return text

    return translated_text


async def handle(request):
    city = request.rel_url.query['city']
    weather_en = await get_weather(city)
    weather_ru = get_translation(weather_en, 'en', 'ru')
    # weather_json = json.dumps(weather_ru, ensure_ascii=False)
    result = web.Response(text=weather_ru)
    return result


async def main():
    app = web.Application()
    app.add_routes([web.get('/weather', handle)])
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, 'localhost', 8000)
    await site.start()

    while True:
        await asyncio.sleep(3000)


if __name__ == '__main__':
    asyncio.run(main())

    # tasks = []

    # for city in cities_:
    #     tasks.append(asyncio.create_task(get_weather(city)))
    #
    # for task in tasks:
    #     await task

# cities = ['Samara', 'Pskov', 'Moscow', 'St. Petersburg', 'Szczecin']
# # cities = ['Samara']
# asyncio.run(main(cities))

t2 = perf_counter()
print(f'Working time: {t2 - t1:.5f} sec')
