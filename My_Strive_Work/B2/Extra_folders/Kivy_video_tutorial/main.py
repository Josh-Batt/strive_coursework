KV = '''
#<KvLang>
from kivy.app import App
from kivy.uix.behaviors import button
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

# class BoxExample(BoxLayout):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         self.orientation = 'vertical'
#         b1 = Button(text="A")
#         b2 = Button(text="B")
#         self.add_widget(b1)
#         self.add_widget(b2)
#         return b1, b2

#===================================================

class MainWidget(Widget):
        button = Button(
            text = 'Hello')
        return button

# class MainWidget(Widget):
#     def build(self):
#         button = Button(
#             text = 'Hello')
#         return button

# class TheLabApp(App):
#     def build(self):
#         label = Label(
#             text='Hello, world',
#             color=(1, 0, 0, 1))
#         return label

class TheLabApp(App):
    def build(self):
        button = Button(
            text = 'Hello')
        return button


TheLabApp().run()

#</KvLang>
'''