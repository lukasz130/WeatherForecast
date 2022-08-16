import gi
import weather

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GdkPixbuf

# TODO: Make GUI prettier - low priority
# TODO: Add to memorize and show on start last chosen city with weather conditions
# TODO: Add weather check time
# TODO: Add to generate dialogs when wrong name and also when city not chosen


class Window(Gtk.Window):

    def __init__(self):
        super().__init__(title='Weather Forecast')

        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(self.box)

        self.enter_city = Gtk.Entry()
        self.enter_city.set_text('Enter city')
        self.box.add(self.enter_city)

        self.search_button = Gtk.Button('Search')
        self.search_button.connect('clicked', self.on_search_button_clicked)
        self.box.add(self.search_button)

        self.weather = weather.Weather()
        self.pixbuf = GdkPixbuf.Pixbuf().new_from_file('./icons/weather-none.svg')
        self.weather_image = Gtk.Image()
        self.weather_image.set_from_pixbuf(pixbuf=self.pixbuf)
        self.box.add(self.weather_image)

        self.city_label = Gtk.Label(self.weather.city)
        self.box.add(self.city_label)

        self.temperature_label = Gtk.Label(f'{self.weather.temperature}\u00B0C')
        self.box.add(self.temperature_label)

        self.conditions_label = Gtk.Label(self.weather.conditions)
        self.box.add(self.conditions_label)

        self.description_label = Gtk.Label(self.weather.description)
        self.box.add(self.description_label)

    def on_search_button_clicked(self, widget):
        city = self.enter_city.get_text()
        self.weather.check_weather(city, 'metric')

        self.city_label.set_label(city)
        self.temperature_label.set_label(f'{self.weather.temperature}\u00b0C')
        self.conditions_label.set_label(self.weather.conditions)
        self.description_label.set_label(self.weather.description)

        weather_icon_path = f'./icons/{self.get_weather_image_icon(self.weather.icon)}.svg'
        self.pixbuf = self.pixbuf.new_from_file(weather_icon_path)
        self.weather_image.set_from_pixbuf(pixbuf=self.pixbuf)

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
            '50n': 'weather-fog'
        }
        return icons_mapping[icon_from_api]
