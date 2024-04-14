from kivy.app import App
from kivy.uix.label import Label
from kivy.lang import Builder

class DynamicLabelsApp(App):
    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.names = ["Angelo", "Bob", "Charlie", "Dave", "Elice", "Frank", "Ginny"]
        self.create_labels()
        return self.root

    def create_labels(self):
        for name in self.names:
            label = Label(text=name, font_size=24)
            self.root.ids.main.add_widget(label)


if __name__ == '__main__':
    DynamicLabelsApp().run()