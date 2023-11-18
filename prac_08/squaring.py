"""
CP1404/CP5632 Practical
Kivy GUI program to square a number
Modify Existing GUI Program
Estimate: 40 minutes
Actual: 48 minutes
"""


from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

__author__ = 'Aaron Bailey'


class SquareNumberApp(App):
    """ SquareNumberApp is a Kivy App for squaring a number. """
    def build(self):
        """ build the Kivy app from the kv file. """
        Window.size = (400, 200)
        self.title = "Square Number Better"
        self.root = Builder.load_file('squaring.kv')
        return self.root

    def handle_calculate(self, value):
        """ handle calculation (could be button press or other call), output result to label widget. """
        try:
            result = float(value) ** 2
            self.root.ids.output_label.text = str(result)
        except ValueError:
            pass


SquareNumberApp().run()
