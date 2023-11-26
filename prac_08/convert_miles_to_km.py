"""
CP1404/CP5632 Practical
Kivy GUI program to convert miles to kilometres
Miles To Kilometres Program
Estimate: 90 minutes
Actual: 112 minutes
"""


from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty

__author__ = 'Aaron Bailey'

MILES_TO_KILOMETRES_FACTOR = 1.609


class MilesToKilometres(App):
    """ MilesToKilometresApp is a Kivy App for converting miles to km. """

    result = StringProperty()
    input_value = StringProperty()

    def build(self):
        """ build the Kivy app from the kv file. """
        Window.size = (700, 500)
        self.title = "Convert Miles To Kilometres"
        self.root = Builder.load_file('convert_miles_to_km.kv')
        return self.root

    def update_value(self):
        """ update view model with latest value."""
        try:
            self.result = self.convert_miles_to_km()
        except ValueError:
            self.input_value = '0.0'

    def convert_miles_to_km(self):
        """convert and return miles to km."""
        kilometres = str(float(self.root.ids.user_input.text) * MILES_TO_KILOMETRES_FACTOR)
        return kilometres

    def increment_value(self, increment):
        """Handle the increment and set user value up or down."""
        try:
            self.input_value = str(float(self.root.ids.user_input.text) + increment)
            self.update_value()
        except ValueError:
            self.input_value = str(increment)
            self.update_value()


MilesToKilometres().run()
