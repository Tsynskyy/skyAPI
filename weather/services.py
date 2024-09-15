import requests
from django.conf import settings


class WeatherHandler:
    def __init__(self):
        self.api_key_main = settings.OPENWEATHER_API_KEY
        self.api_key_backup = settings.WEATHERAPI_KEY

    def get_weather_main(self, city):
        url = 'http://api.openweathermap.org/data/2.5/weather'
        params = {'q': city, 'appid': self.api_key_main}
        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()
        return response.json()

    def get_weather_backup(self, city):
        url = 'http://api.weatherapi.com/v1/current.json'
        params = {'q': city, 'key': self.api_key_backup}
        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()
        return response.json()
