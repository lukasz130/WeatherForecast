import requests


class Weather:
    _api_key = '914afb0af72a3e16c31fe7ac6fffe93d'

    def __init__(self, city=None, units_format='metric'):
        # TODO: Add units choose: metric or imperial
        # TODO: Add city not known
        # TODO: Error handling for weather API e.g. 404 NOT FOUND
        self._city = 'N/A'
        self._temperature = 'N/A'
        self._conditions = 'N/A'
        self._description = 'N/A'
        self._icon = 'N/A'

        self.check_weather(city, units_format)

    @property
    def city(self):
        return self._city

    @property
    def temperature(self):
        return self._temperature

    @property
    def conditions(self):
        return self._conditions

    @property
    def description(self):
        return self._description

    @property
    def icon(self):
        return self._icon

    def check_weather(self, city, units_format):
        if city:
            response_geocoding = requests.get(
                f'http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={self.__class__._api_key}'
            )
            latitude = response_geocoding.json()[0]['lat']
            longitude = response_geocoding.json()[0]['lon']
            response_weather_json = requests.get(
                f'https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}'
                f'&appid={self.__class__._api_key}&units={units_format}'
            ).json()
            self._city = city
            self._temperature = response_weather_json['main']['temp']
            self._conditions = response_weather_json['weather'][0]['main']
            self._description = response_weather_json['weather'][0]['description']
            self._icon = response_weather_json['weather'][0]['icon']
