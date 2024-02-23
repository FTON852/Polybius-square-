from tkinter import Frame, BOTH, TOP
from Modules.Modules.CheckButtonsModules import CheckButtonsModules as cbtnm


class FrameSelection:
    def __init__(self, master, width=200, height=100):
        self.checkButtonsModule = cbtnm()
        self.frame = Frame(master, width=width, height=height)
        self.frame.pack(fill=BOTH, side=TOP, expand=True)
        self.checkButtonsModule.master = self.frame
        self.checkButtonsModule.add("lower", "en")
        self.checkButtonsModule.add("upper", "EN")
        self.checkButtonsModule.add("numeric", "012")
        self.checkButtonsModule.add("symbol", "!@#")
        self.checkButtonsModule.add("space", "space")
        self.checkButtonsModule.add("ru", "ru")
        self.checkButtonsModule.add("RU", "RU")
