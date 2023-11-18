"""
Modify Existing GUI Program
Estimate: 20 minutes
Actual: 25 minutes
"""


from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    """Kivy app for greeting a user with their name."""
    def build(self):
        """Build the kivy GUI from the kv file."""
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """Greet the user."""
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"

    def clear_name(self):
        """Clear users name in the text field."""
        self.root.ids.input_name.text = ''


BoxLayoutDemo().run()
