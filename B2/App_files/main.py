from kivymd.app import MDApp
from mapview import MyMap
from giveresultsmenu import GiveResultsMenu
from gpshelper import GpsHelper


class MainApp(MDApp):
    give_results = None

    def on_start(self):
        self.theme_cls.primary_palette = 'BlueGray'

        GpsHelper().run()

        self.give_results = GiveResultsMenu()


MainApp().run()
