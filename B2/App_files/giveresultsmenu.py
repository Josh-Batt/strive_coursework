from kivymd.uix.dialog import MDDialog

class GiveResultsMenu(MDDialog):
    title = 'Results'
    def __init__(self):
        super().__init__()
        self.size_hint = [.9, .3]
