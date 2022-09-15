import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf


class View(Gtk.Window):
    # TODO: Add to generate dialogs when wrong name and also when city not chosen
    # TODO: Make GUI prettier - low priority
    # TODO: Change metric to *C and imperial to *F
    def __init__(self):
        super().__init__(title='Weather Forecast')

        self._box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(self._box)

        self._enter_city = Gtk.Entry()
        self._enter_city.set_text('Enter city')
        self._box.add(self._enter_city)

        self._search_button = Gtk.Button('Search')
        self._box.add(self._search_button)

        self._units_format_combo = Gtk.ComboBoxText()
        self._units_format_combo.append('metric', 'metric')
        self._units_format_combo.append('imperial', 'imperial')
        self._box.add(self._units_format_combo)

        self._weather_image = Gtk.Image()

        self._box.add(self._weather_image)

        self._city_label = Gtk.Label()
        self._box.add(self._city_label)

        self._temperature_label = Gtk.Label()
        self._box.add(self._temperature_label)

        self._conditions_label = Gtk.Label()
        self._box.add(self._conditions_label)

        self._description_label = Gtk.Label()
        self._box.add(self._description_label)

        self._up_to_date_label = Gtk.Label()
        self._box.add(self._up_to_date_label)

        self.connect('destroy', Gtk.main_quit)

    @staticmethod
    def run():
        Gtk.main()

    def set_weather_icon(self, icon):
        weather_icon_path = f'./icons/{self._get__weather_image_icon(icon)}.svg'
        pixbuf = GdkPixbuf.Pixbuf().new_from_file(weather_icon_path)
        self._weather_image.set_from_pixbuf(pixbuf=pixbuf)

    def set_city(self, city):
        self._city_label.set_label(city)

    def set_temperature(self, temperature, units_format):
        units_format_display = 'C' if units_format == 'metric' else 'F'
        self._temperature_label.set_label(f'{temperature}\u00B0{units_format_display}')

    def set_conditions(self, conditions):
        self._conditions_label.set_label(conditions)

    def set_description(self, description):
        self._description_label.set_label(description)

    def on_search(self, callback):
        self._search_button.connect('clicked', lambda widget: callback(self._enter_city.get_text()
                                    if self._enter_city.get_text() != 'Enter city' else ''))

    def set_units_format(self, unit_format):
        self._units_format_combo.set_active_id(unit_format)

    def on_units_format_changed(self, callback):
        self._units_format_combo.connect('changed', lambda widget: callback(self._units_format_combo.get_active_id()))

    def set_up_to_date_message(self, is_weather_up_to_date=False):
        color = 'green' if is_weather_up_to_date else 'red'
        up_to_date_message = 'Less then 2 hours ago' if is_weather_up_to_date else 'More than 2 hours ago'
        self._up_to_date_label.set_markup(f'<span color="{color}">Last update:\n{up_to_date_message}</span>')

    def show_dialog(self, status):
        if status == 'Unauthorized':
            dialog_title = 'Authorization problem'
            dialog_text = 'Wrong API key'
        elif status == 'ConnectionError':
            dialog_title = 'Connection problem'
            dialog_text = 'Check internet connection'
        elif status == 'NotFound':
            dialog_title = 'City not found'
            dialog_text = 'Try another city'
        else:
            dialog_title = 'Unknown problem'
            dialog_text = 'Problem not known'
        dialog = Gtk.MessageDialog(
                                    transient_for=self,
                                    flags=0,
                                    message_type=Gtk.MessageType.ERROR,
                                    buttons=Gtk.ButtonsType.OK,
                                    text=dialog_title
                                    )
        dialog.format_secondary_text(dialog_text)
        dialog.run()
        dialog.destroy()

    @staticmethod
    def _get__weather_image_icon(icon_from_api):
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
