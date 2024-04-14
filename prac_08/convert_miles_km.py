from kivy.app import App
from kivy.lang import Builder


MILES_TO_KM = 1.60934

class MilesConverterApp(App):
    def build(self):
        """Build the Kivy app from the kv file."""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_m_km_solution.kv')
        return self.root


    def handle_calculate(self):
        """Handle the calculation, could be a button press or other call,
        and output the result to the label widget."""
        value = self.get_validated_miles()
        result = value * MILES_TO_KM
        self.root.ids.output_label.text = f"{result:.3f}"  # Format to 3 decimal places

    def handle_increment(self, change):
        """Handle up/down button press, update the text input with a new value,
        and call the calculation function."""
        value = self.get_validated_miles() + change
        self.root.ids.input_miles.text = f"{value:.0f}"  # Format as an integer
        self.handle_calculate()

    def get_validated_miles(self):
        """Get text input from the text entry widget and convert it to float."""
        miles_text = self.root.ids.input_miles.text
        try:
            value = float(miles_text)
        except ValueError:
            value = 0
        return value


if __name__ == '__main__':
    MilesConverterApp().run()
