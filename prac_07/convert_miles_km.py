from kivy.app import App
from kivy.lang import Builder

MILES_TO_KM_CONVERSION = 1.60934


class ConvertMilesKm(App):
    """Convert Miles to Kilometres Kivy App for squaring a number"""
    def build(self):
        """Build the kivy app from the kv file"""
        self.title = "Converter"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self):
        value = self.get_validated_miles()
        result = value * MILES_TO_KM_CONVERSION
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, increment):
        value = self.get_validated_miles() + increment
        self.root.ids.input_miles.text = str(value)
        self.handle_calculate()

    def get_validated_miles(self):
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0


ConvertMilesKm().run()