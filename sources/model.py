import requests
from os.path import exists
import datetime


class Model:

    _API_KEY = '914afb0af72a3e16c31fe7ac6fffe93d'

    def __init__(self):
        if not exists('config.txt'):
            with open('config.txt', 'w') as file:
                file_content = [
                    "city=Kraków\n",
                    "temperature=18.96\n",
                    "conditions=Clouds\n",
                    "description=few clouds\n",
                    "icon=02n\n",
                    "units_format=metric\n,"
                    "time=2022-09-13 23-00-01"
                ]
                for line in file_content:
                    file.write(line)

        self._city = city_conf if (city_conf := self.get_from_config_file('city')) else 'N/A'
        self._temperature = temperature if (temperature := self.get_from_config_file('temperature')) else 'N/A'
        self._conditions = conditions if (conditions := self.get_from_config_file('conditions')) else 'N/A'
        self._description = description if (description := self.get_from_config_file('description')) else 'N/A'
        self._icon = icon if (icon := self.get_from_config_file('icon')) else 'N/A'
        self._units_format = units_format if (units_format := self.get_from_config_file('units_format')) else 'N/A'
        self._time = time if (time := self.get_from_config_file('time')) else 'N/A'

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value
        self.set_to_config_file('city', value)

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        self._temperature = value
        self.set_to_config_file('temperature', value)

    @property
    def conditions(self):
        return self._conditions

    @conditions.setter
    def conditions(self, value):
        self._conditions = value
        self.set_to_config_file('conditions', value)

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
        self.set_to_config_file('description', value)

    @property
    def icon(self):
        return self._icon

    @icon.setter
    def icon(self, value):
        self._icon = value
        self.set_to_config_file('icon', value)

    @property
    def units_format(self):
        return self._units_format

    @units_format.setter
    def units_format(self, value):
        self._units_format = value
        self.set_to_config_file('units_format', value)

    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, value):
        self._time = value
        self.set_to_config_file('time', value)

    def is_time_up_to_date(self):
        last_checked_weather_time = datetime.datetime.strptime(self._time, '%Y-%m-%d %H-%M-%S')
        now_time = datetime.datetime.now()
        # if weather checked less than 2 hours ago return True, else False
        return (now_time - last_checked_weather_time).total_seconds() < 7200

    def check_weather(self):
        try:
            response_geocoding = requests.get(
                f'http://api.openweathermap.org/geo/1.0/direct?q={self._city}&limit=1&appid={self.__class__._API_KEY}'
            )
        except requests.exceptions.ConnectionError:
            return 'ConnectionError'
        else:
            status = response_geocoding.status_code
            if status == 200:
                try:
                    latitude = response_geocoding.json()[0]['lat']
                    longitude = response_geocoding.json()[0]['lon']
                except IndexError:
                    self.city = 'N/A'
                    self.temperature = 'N/A'
                    self.conditions = 'N/A'
                    self.description = 'N/A'
                    self.icon = 'N/A'
                    return 'NotFound'
                response_weather_json = requests.get(
                    f'https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}'
                    f'&appid={self.__class__._API_KEY}&units={self._units_format}'
                ).json()
                self.temperature = response_weather_json['main']['temp']
                self.conditions = response_weather_json['weather'][0]['main']
                self.description = response_weather_json['weather'][0]['description']
                self.icon = response_weather_json['weather'][0]['icon']
                self.time = datetime.datetime.today().strftime('%Y-%m-%d %H-%M-%S')
                return 'OK'
            elif status == 401:
                return 'Unauthorized'

    @staticmethod
    def set_to_config_file(parameter='', value=''):
        # if not parameter or not value:
        #     return False
        with open('config.txt', 'r') as file:
            content = file.readlines()
            # Update existing parameter
            content = [f'{parameter}={value}\n' if parameter in line else line for line in content]
        with open('config.txt', 'w') as file:
            file.writelines(content)
        # return True

    @staticmethod
    def get_from_config_file(parameter=''):
        with open('config.txt', 'r') as file:
            content = file.readlines()
            if not parameter:
                return None
            is_parameter_in_file = False
            for line in content:
                if parameter in line:
                    is_parameter_in_file = True
                    return line.split('=')[1].strip()
            if not is_parameter_in_file:
                return None
