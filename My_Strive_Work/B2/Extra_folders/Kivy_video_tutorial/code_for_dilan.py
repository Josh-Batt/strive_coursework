from kivy.app import App
from kivy.uix.gridlayout import GridLayout

class GridLayoutExample(GridLayout):
    pass

#_____PRODCUTION .kv_____

'''
GridLayoutExample:

<GridLayoutExample>:

    cols: 2

    Button:
        text: "Exit"           
    Button:
        text: "Train"
    Button:
        text: "Bus"
    Button:
        text: "Car"
    Button:
        text: "Still"
    Button:
        text: "Walking"
'''
#___________________________________________

'''
Can comment out gridlayout class, if you dont want to impliment code inside the class. Instead put this in the .kv:

___NORMAL___
GridLayoutExample:

<GridLayoutExample>:

___CHANGED___
GridLayoutExample:

<GridLayoutExample@GridLayout>:
'''

#___________________________________________

'''
___.kv code w Notes___

GridLayoutExample:

<GridLayoutExample>:
    #rows
    #cols
    ### MUST specify either rows or cols

    cols: 2

    Button:
        text: "Exit"
        size_hint: .5, 1 #-> This is how to resize column. 1st num is horziantal resize, 2nd is vertical resize.
                         #MUST apply to all buttons in that colunm
    Button:
        text: "Train"
    Button:
        text: "Bus"
    Button:
        text: "Car"
    Button:
        text: "Still"
    Button:
        text: "Walking"
'''

#___________________________________________

class WidgetExample(GridLayout):
    def exampleTrain(self, widget):
        print('toggle state' + widget.state) #Prints if buttons pressed or not
        if widget.state == 'normal':
            widget.text = 'Train'
        else:
            widget.text = 'Train Activated'


'''
WidgetsExample:

<WidgetsExample>:

    cols: 2

    Button: # May not work with toggle buttons
        text: "Exit"
        on_state: root.#CLOSE APP Method inside class()        
    ToggleButton:
        text: "Train"
        on_state: root.#TURN ON SENSORS, SAVE DATA UNDER TRAIN FOLDER Method inside class(self)
    ToggleButton:
        text: "Bus"
        on_state: root.#TURN ON SENSORS, SAVE DATA UNDER BUS FOLDER Method inside class()
    ToggleButton:
        text: "Car"
        on_state: root.#TURN ON SENSORS, SAVE DATA UNDER CAR FOLDER Method inside class()
    ToggleButton:
        text: "Still"
        on_state: root.#TURN ON SENSORS, SAVE DATA UNDER STILL FOLDER Method inside class() 
    ToggleButton:
        text: "Walking"
        on_state: root.#TURN ON SENSORS, SAVE DATA UNDER WALKING FOLDER Method inside class() 
'''

#____________________________________

'''
from kivy.uix.togglebuttons import ToggleButtons
from kivy.uix.widget import Widget

class Widget(widget)
    pass

___.kv___

Widget:

<Widget>:
    ToggleButton:
        text: 'GPS toggle'
        on_state: root. # Method that pings GPS spot
'''