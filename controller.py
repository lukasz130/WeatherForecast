import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf

from model import Model
from view import View


class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View()

        self.view.enter_city.set_text('Enter city')
        self.view.search_button.connect('clicked', self.on_search_button_clicked)
        self.view.units_format_combo.set_active_id(self.model.get_from_config_file('units_format'))
        self.view.units_format_combo.connect('changed', self.on_units_format_combo_changed)

        weather_icon_path = f'./icons/{self.get_weather_image_icon(self.model.icon)}.svg'
        self.pixbuf = GdkPixbuf.Pixbuf().new_from_file(weather_icon_path)
        self.view.weather_image.set_from_pixbuf(pixbuf=self.pixbuf)

        self.view.city_label.set_label(self.model.city)
        unit_sign = 'C' if self.model.get_from_config_file('units_format') == 'metric' else 'F'
        self.view.temperature_label.set_label(f'{self.model.temperature}\u00B0{unit_sign}')
        self.view.conditions_label.set_label(self.model.conditions)
        self.view.description_label.set_label(self.model.description)

        self.view.show_all()
        self.view.connect('destroy', Gtk.main_quit)
        Gtk.main()

    # TODO: Maybe change name to weather_icon_mapping
    @staticmethod
    def get_weather_image_icon(icon_from_api):
        icons_mapping = {
            '01d': 'weather-clear',
            '01n': 'weather-clear-night',
            '02d': 'weather-few-clouds',
            '02n': 'weather-clouds-night',
            '03d': 'weather-clouds',
            '03n': 'weather-few-clouds-night',
            '04d': 'weather-overcast',
            '04n': 'weather-overcast',
            '09d': 'weather-showers-scattered',
            '09n': 'weather-showers-scattered',
            '10d': 'weather-showers',
            '10n': 'weather-showers',
            '11d': 'weather-storm',
            '11n': 'weather-storm',
            '13d': 'weather-snow',
            '13n': 'weather-snow',
            '50d': 'weather-fog',
            '50n': 'weather-fog',
            'N/A': 'weather-none'
        }
        return icons_mapping[icon_from_api]

    def on_search_button_clicked(self, widget):
        self.model.city = city if not (city := self.view.enter_city.get_text()) ==\
                           'Enter city' else self.model.get_from_config_file('city')
        self.model.check_weather()

        self.view.city_label.set_label(self.model.city)
        # print(self.weather.city)
        unit_sign = 'C' if self.model.get_from_config_file('units_format') == 'metric' else 'F'
        self.view.temperature_label.set_label(f'{self.model.temperature}\u00b0{unit_sign}')
        self.view.conditions_label.set_label(self.model.conditions)
        self.view.description_label.set_label(self.model.description)

        weather_icon_path = f'./icons/{self.get_weather_image_icon(self.model.icon)}.svg'
        self.pixbuf = self.pixbuf.new_from_file(weather_icon_path)
        self.view.weather_image.set_from_pixbuf(pixbuf=self.pixbuf)

    def on_units_format_combo_changed(self, widget):
        units_format = self.view.units_format_combo.get_active_id()
        self.model.units_format = units_format


if __name__ == '__main__':
    controller = Controller()
