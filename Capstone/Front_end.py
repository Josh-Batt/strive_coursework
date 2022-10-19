from re import match
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen

from Back_end import matching_algo, verify, full_match

import os

Window.clearcolor = (1, 1, 1, 1)

class MainWindow(Screen):
    pass
class ProfileWindow(Screen):
    pass
class RequestWindow(Screen):
    pass
class FindingWindow(Screen):
    pass
class WindowManager(ScreenManager):
    pass

kv = Builder.load_file('Front_end_Kivy.kv')

class MyMainApp(App):
    def build(self):
        return kv
    
    def load_face2face(self):
        #os.system('Back_end.py')
        request_paths, pic_paths = matching_algo()
        half = None

        for j in request_paths:
            # show j on screen
            for k in pic_paths:
                # show k on screen
                result = verify(j, k)
                
                if result == True:
                    half = True

        if half == True:
            print('Half Match!')
            full_match(1, 2)
        else:
            print('No Half-Match')
            

if __name__ == '__main__':
    MyMainApp().run()