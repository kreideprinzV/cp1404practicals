
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
class BoxLayoutDemo(App):
    def build(self):
        return BoxLayout()

    def handle_clear(self):
        """Clear the text input field and output label"""
        self.root.ids.input_name.text = ''
        self.root.ids.output_label.text = 'Enter your name'

    def handle_greet(self):
        """Change the output label's text to greet the user by name"""
        name = self.root.ids.input_name.text
        self.root.ids.output_label.text = f"Hello {name}"


if __name__ == '__main__':
    BoxLayoutDemo().run()
