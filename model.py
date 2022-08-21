import requests


class Model:
    # TODO: Add to create config.file if doesn't exist and fill with some default parameters
    # TODO: Add error handling for weather API e.g. 404 NOT FOUND
    # TODO: Add error handling if parameter cannon be updated or add
    # TODO: Add method to update/add multiple parameters
    # TODO: Add method to initialize default config file
    # TODO: Add wrong api_kay error handling

    _API_KEY = '914afb0af72a3e16c31fe7ac6fffe93d'

    def __init__(self):
        self._city = city_conf if (city_conf := self.get_from_config_file('city')) else 'N/A'
        self._temperature = temperature if (temperature := self.get_from_config_file('temperature')) else 'N/A'
        self._conditions = conditions if (conditions := self.get_from_config_file('conditions')) else 'N/A'
        self._description = description if (description := self.get_from_config_file('description')) else 'N/A'
        self._icon = icon if (icon := self.get_from_config_file('icon')) else 'N/A'
        self._units_format = units_format if (units_format := self.get_from_config_file('units_format')) else 'N/A'

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

    def check_weather(self):
        response_geocoding = requests.get(
            f'http://api.openweathermap.org/geo/1.0/direct?q={self._city}&limit=1&appid={self.__class__._API_KEY}'
        )
        latitude = response_geocoding.json()[0]['lat']
        longitude = response_geocoding.json()[0]['lon']
        response_weather_json = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}'
            f'&appid={self.__class__._API_KEY}&units={self._units_format}'
        ).json()
        self.temperature = response_weather_json['main']['temp']
        self.conditions = response_weather_json['weather'][0]['main']
        self.description = response_weather_json['weather'][0]['description']
        self.icon = response_weather_json['weather'][0]['icon']

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

    # For future use
    # @staticmethod
    # def add_to_config_file(parameter='', value=''):
    #     with open('config.txt', 'r') as file:
    #         content = file.readlines()
    #         # Add new parameter
    #         is_parameter_in_file = False
    #         for line in content:
    #             if parameter + '=' in line:
    #                 is_parameter_in_file = True
    #                 break
    #         if not is_parameter_in_file:
    #             # To take care of last blank line
    #             if content[-1] == '\n':
    #                 content = content[:-1]
    #             content.append(f'{parameter}={value}\n')
    #             content.append(f'\n')
    #     with open('config.txt', 'w') as file:
    #         file.writelines(content)

    @staticmethod
    def get_from_config_file(parameter=''):
        with open('config.txt', 'r') as file:
            content = file.readlines()
            if not parameter:
                # file.close()
                return None
            is_parameter_in_file = False
            for line in content:
                if parameter in line:
                    is_parameter_in_file = True
                    # file.close()
                    return line.split('=')[1].strip()
            if not is_parameter_in_file:
                # file.close()
                return None


# Example of config file:
# city=Tokio
# temperature=24.72
# conditions=Clouds
# description=broken clouds
# icon=04d
# units_format=metric
# last_weather_check=?
# width=100
# height=300
# spacing=10
