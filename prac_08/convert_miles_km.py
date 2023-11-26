"""
CP1404/CP5632 Practical
Kivy GUI program to convert miles to km
Quinn Stocker
Started 8/11/2023
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty

__author__ = 'Quinn Stocker'

CONVERSION = 1.609


class DistanceConverterApp(App):
    output_value = StringProperty()
    input_value = StringProperty()

    def build(self):
        Window.size = (800, 400)
        self.title = "Miles to km"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_increment(self, value, increment):
        try:
            result = float(value) + increment
            self.input_value = str(result)
        except ValueError:
            result = 0.0 + increment
            self.input_value = str(result)

    def handle_conversion(self, value):
        try:
            result = float(value) * CONVERSION
            self.output_value = str(result)
        except ValueError:
            self.output_value = str(0.0)


DistanceConverterApp().run()
