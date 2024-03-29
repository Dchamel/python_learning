import asyncio, logging, aiosqlite
from datetime import datetime
from time import perf_counter
from aiohttp import ClientSession, web
from aiohttp.abc import AbstractAccessLogger
from googletrans import Translator

t1 = perf_counter()

logger = logging.getLogger('WeatherLog')

# storage for client sessions
app_storage = {}


# Изменения


# load_dotenv()
# yapi_key = os.environ['GOOGLE_API_KEY']

class AccessLogger(AbstractAccessLogger):

    def log(self, request, response, time: float) -> None:
        self.logger.info(f'{request.remote}\t'
                         f'{request.method}'
                         f'{request.path}\t'
                         f'-- done in {time:.2f}s: {response.status}\n')


async def create_table():
    async with aiosqlite.connect('weather.db') as db:
        await db.execute('CREATE TABLE IF NOT EXISTS requests'
                         '(date, city text, weather text)')
        await db.commit()


async def save_to_db(city, weather):
    async with aiosqlite.connect('weather.db') as db:
        await db.execute('INSERT INTO requests VALUES (?, ?, ?)',
                         (datetime.now(), city, weather))
        await db.commit()


async def get_weather(city: str) -> list[str]:
    url = f'http://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city,
        'APPID': '2a4ff86f9aaa70041ec8e82db64abf56',
        'units': 'metric'
    }
    logger.info('Send request to the weather Server')
    async with app_storage['session'].get(url=url, params=params) as response:
        weather_json = await response.json()
        try:
            city_main = f'{city}: {weather_json["weather"][0]["main"]}({weather_json["weather"][0]["description"]})'
            city_temp = f'Temperature: {weather_json["main"]["temp"]:.1f}\N{DEGREE SIGN}c Feels Like: {weather_json["main"]["feels_like"]:.1f}\N{DEGREE SIGN}c\n'
            city_weather = [city_main, city_temp]
            logger.info('Data has been received')
            return city_weather
        except KeyError:
            logger.info('No data')
            return 'No data'


# Finally make it works but only with googletrans==3.1.0a0
async def get_translation(text: list[str], main='en', dest='ru') -> list[str]:
    logger.info('Start translation')
    translator = Translator()
    try:
        translated_list = translator.translate(text, src=main, dest=dest)
        translated_text = '\n'.join([i.text for i in translated_list])
        logger.info('Translation finished successfully')
    except KeyError:
        logger.info('No translation')
        return text

    return translated_text


async def handle(request):
    city = request.rel_url.query['city']
    weather_en = await get_weather(city)
    weather_ru = await get_translation(weather_en, 'en', 'ru')
    await save_to_db(city, weather_ru)
    result = web.Response(text=weather_ru)
    return result


async def main() -> None:
    # creating session 4 the whole app
    app_storage['session'] = ClientSession()
    async with app_storage['session']:
        await create_table()
        app = web.Application()
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s %(name)-14s %(levelname)s: %(message)s')
        app.add_routes([web.get('/weather', handle)])
        runner = web.AppRunner(app, access_log_class=AccessLogger)
        await runner.setup()
        site = web.TCPSite(runner, 'localhost', 8000)
        await site.start()
        logger.info('Server started')

        while True:
            await asyncio.sleep(3000)


if __name__ == '__main__':
    asyncio.run(main())

# cities = ['Samara', 'Pskov', 'Moscow', 'St. Petersburg', 'Szczecin']
# # cities = ['Samara']
# asyncio.run(main(cities))

t2 = perf_counter()
print(f'Working time: {t2 - t1:.2f} sec')
