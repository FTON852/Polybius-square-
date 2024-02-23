from tkinter import IntVar, Checkbutton, ACTIVE


class CheckButton:
    def __init__(self):
        self.enabled = IntVar(value=1)
        self.check = None

    def check_button(self,master, text, column=0, row=0):
        self.check = Checkbutton(master=master, text=text, variable=self.enabled)
        self.check.grid(column=column, row=row)
