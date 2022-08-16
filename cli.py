# To weather class testing purposes only
import weather


class CLI:

    def __init__(self, city, units_format='metric'):
        self._weather = weather.Weather(city, units_format)
        self._city = city

    def display_weather(self):
        print(self._city)
        print(self._weather.temperature)
        print(self._weather.conditions)
        print(self._weather.description)
