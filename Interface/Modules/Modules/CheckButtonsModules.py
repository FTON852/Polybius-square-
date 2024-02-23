from Modules.Modules.CheckButton import CheckButton

class CheckButtonsModules:
    def __init__(self):
        self.master = None
        self.count = 0
        self.buttons = dict()

    def add(self, name, text):
        button = CheckButton()
        button.check_button(self.master, text, column=self.count,)
        self.buttons[name] = button
        self.count += 1
