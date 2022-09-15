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
        self.view.set_up_to_date_message(self.model.is_time_up_to_date())

        self.view.show_all()
        self.view.run()

    def on_search(self, requested_city):
        self.model.city = requested_city if not requested_city == ''\
                          else self.model.get_from_config_file('city')
        status = self.model.check_weather()
        if status == 'OK':
            self.view.set_city(self.model.city)
            units_format = self.model.get_from_config_file('units_format')
            self.view.set_temperature(self.model.temperature, units_format)
            self.view.set_conditions(self.model.conditions)
            self.view.set_description(self.model.description)
            self.view.set_weather_icon(self.model.icon)
            self.view.set_up_to_date_message(self.model.is_time_up_to_date())
        else:
            self.view.show_dialog(status)

    def on_units_format_changed(self, units_format):
        self.model.units_format = units_format


if __name__ == '__main__':
    controller = Controller()
