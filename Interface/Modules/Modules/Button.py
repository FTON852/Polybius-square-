from tkinter import Button as btn


class Button:
    def __init__(self, master, text, command, column=0, row=0):
        self.button = btn(master=master, text=text, command=command)
        self.button.grid(column=column, row=row)
