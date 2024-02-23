from tkinter import Frame, BOTH, TOP
from Modules.Modules.SeedModule import SeedModule as sdm


class FrameSeed:
    def __init__(self, master, command, width=200, height=100):
        self.frame = Frame(master, width=width, height=height)
        self.frame.pack(fill=BOTH, side=TOP, expand=True)
        self.seedModule = sdm()
        self.seedModule.label(master=self.frame, text="Seed:")
        self.seedModule.entry(master=self.frame)
        self.seedModule.button(master=self.frame, text="Generate", command=command)
