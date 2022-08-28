from model import Model
from view import View


class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View()

        self.view.on_search(self.on_search)
        self.view.set_units_format(self.model.get_from_config_file('units_format'))
        self.view.on_units_format_changed(self.on_units_format_changed)

        self.view.set_weather_icon(self.model.icon)
        self.view.set_city(self.model.city)

        units_format = self.model.get_from_config_file('units_format')
        self.view.set_temperature(self.model.temperature, units_format)

        self.view.set_conditions(self.model.conditions)
        self.view.set_description(self.model.description)

        self.view.show_all()
        self.view.run()

    def on_search(self, requested_city):
        self.model.city = requested_city if not requested_city == ''\
                          else self.model.get_from_config_file('city')
        self.model.check_weather()

        self.view.set_city(self.model.city)
        # unit_format = 'C' if self.model.get_from_config_file('units_format') == 'metric' else 'F'
        units_format = self.model.get_from_config_file('units_format')
        self.view.set_temperature(self.model.temperature, units_format)
        self.view.set_conditions(self.model.conditions)
        self.view.set_description(self.model.description)
        self.view.set_weather_icon(self.model.icon)

    def on_units_format_changed(self, units_format):
        self.model.units_format = units_format


if __name__ == '__main__':
    controller = Controller()
