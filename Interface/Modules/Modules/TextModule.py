from tkinter import Label, Text


class TextModule:

    def __init__(self):
        self.txt_input = None
        self.lbl_text = None

    def label(self, master, text):
        self.lbl_text = Label(master=master, text=text)
        self.lbl_text.grid(column=0, row=0)

    def text(self, master, width=40, height=10):
        self.txt_input = Text(master=master, width=width, height=height)
        self.txt_input.grid(column=0, row=1)
