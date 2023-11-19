"""
CP1404/CP5632 Practical
Kivy GUI program to create a label for each string name
Dynamic Labels Program
Estimate: 45 minutes
Actual: 51 minutes
"""


from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabels(App):
    """ MilesToKilometresApp is a Kivy App for converting miles to km. """

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        # basic data (model) example - dictionary of names: phone numbers
        self.names = {"Billy Banerk, Alfonzo Gonzalez, Chris Kale"}

    def build(self):
        """ build the Kivy app from the kv file. """
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        for name in self.names:
            label = Label(text=name)
            self.root.ids.main.add_widget(label)
        return self.root


DynamicLabels().run()
