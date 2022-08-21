import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class View(Gtk.Window):
    # TODO: Add to memorize and show on start last chosen city with weather conditions
    # TODO: Add weather check time
    # TODO: Add units choose: metric or imperial
    # TODO: Add to generate dialogs when wrong name and also when city not chosen
    # TODO: Make GUI prettier - low priority
    def __init__(self):
        super().__init__(title='Weather Forecast')

        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(self.box)

        self.enter_city = Gtk.Entry()
        self.box.add(self.enter_city)

        self.search_button = Gtk.Button('Search')
        self.box.add(self.search_button)

        self.units_format_combo = Gtk.ComboBoxText()
        self.units_format_combo.append('metric', 'metric')
        self.units_format_combo.append('imperial', 'imperial')
        self.box.add(self.units_format_combo)

        self.weather_image = Gtk.Image()
        self.box.add(self.weather_image)

        self.city_label = Gtk.Label()
        self.box.add(self.city_label)

        self.temperature_label = Gtk.Label()
        self.box.add(self.temperature_label)

        self.conditions_label = Gtk.Label()
        self.box.add(self.conditions_label)

        self.description_label = Gtk.Label()
        self.box.add(self.description_label)
