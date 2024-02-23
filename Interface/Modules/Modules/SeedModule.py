from tkinter import Label, Entry, Button


class SeedModule:
    def __init__(self):
        self.lbl = None
        self.ent_input = None
        self.btn = None

    def label(self, master, text):
        self.lbl = Label(master=master, text=text)
        self.lbl.grid(column=0, row=0)

    def entry(self, master, ):
        self.ent_input = Entry(master=master, width=40)
        self.ent_input.grid(column=1, row=0)

    def button(self,master,text, command):
        self.btn = Button(master=master, text=text, command=command)
        self.btn.grid(column=2, row=0)
