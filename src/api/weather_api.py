import aiohttp
import yaml

class WeatherAPI:
    def _init_(self):
        with open('config.yaml', 'r') as file:
            config = yaml.safe_load(file)
        self.api_key = config['openweathermap_api_key']
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"

    async def get_weather(self, city):
        params = {
            'q': city,
            'appid': self.api_key,
            'units': 'metric'
        }
        async with aiohttp.ClientSession() as session:
            async with session.get(self.base_url, params=params) as response:
                return await response.json()
