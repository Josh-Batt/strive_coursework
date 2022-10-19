from kivymd.app import MDApp #App DOESNT WORK, NEEDS MDApp
from kivy.lang import Builder
from kivy.core.window import  Window
from kivy.uix.screenmanager import ScreenManager, Screen

from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

Window.size = (300,500) 

#kv = Builder.load_file('main.kv') #DOESNT WORK

class MainWindow(Screen):
	pass

class ProfileWindow(Screen):
	pass

class RequestWindow(Screen):
	pass

class FindingWindow(Screen):
	pass

class ResultsWindow(Screen):
	pass

class WindowManager(ScreenManager):
	pass

#-----

class BoxLayoutExample(BoxLayout):
	pass

class GridLayoutExample(GridLayout):
	pass

class MainWidget(Widget):
	pass

class DatingApp(MDApp):
	def build(self):
		self.theme_cls.theme_style='Light'
		return Builder.load_file('main.kv') #RUN EACH PAGE HERE BEFORE LINKED

DatingApp().run()