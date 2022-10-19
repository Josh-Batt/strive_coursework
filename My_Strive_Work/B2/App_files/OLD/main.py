from kivymd.app import MDApp
from kivy_garden.mapview import MapView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.togglebutton import ToggleButton

from mapview import MyMapView



class MainPage(BoxLayout):
    def __init__(self, **kwargs):
        super(MainPage, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.box()

    def box(self):
        #bt1 = Button(text='Test')
        bt2 = ToggleButton(text='GPS Toggle', size_hint=(0.2, 0.2))
        my_map = MyMapView()
        self.add_widget(bt2)
        self.add_widget(my_map)

class myApp(MDApp):
    def build(self):
        return MainPage()


if __name__ == "__main__":

    myApp().run()