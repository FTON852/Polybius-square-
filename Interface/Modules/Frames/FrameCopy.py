from tkinter import Frame, BOTH, TOP
from Modules.Modules.TextModule import TextModule as txtm
from Modules.Modules.Button import Button as btn


class FrameCopy:
    def __init__(self, master, text,command, width=200, height=100):
        self.frame = Frame(master, width=width, height=height)
        self.frame.pack(fill=BOTH, side=TOP, expand=True)
        self.openText = txtm()
        self.openText.label(self.frame, text)
        self.openText.text(self.frame, width=40, height=15)
        self.btn_copy = btn(self.frame, text="Copy", command=command, row=3)
