from kivy.app import App
from kivy.uix.togglebutton import ToggleButton
from kivy_garden.mapview import MapView, MapSource, MapMarker

class MainApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 2