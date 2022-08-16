# import cli

# print('Weather for now')
# city = input('Choose city: ')
# cli = cli.CLI('Krakow')
# cli.display_weather()

# TODO: Make configuration file

import gui
from gi.repository import Gtk


window = gui.Window()
window.show_all()
window.connect("destroy", Gtk.main_quit)
Gtk.main()
