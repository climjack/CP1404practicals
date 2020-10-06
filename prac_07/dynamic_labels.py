from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
NAMES = ["joidjoid", "qwjeoiwqjdo"]


class DisplayNames(App):
    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        for name in NAMES:
            temp_label = Label(text=name, id=name)
            self.root.ids.dynamic_labels_container.add_widget(temp_label)


DisplayNames().run()
