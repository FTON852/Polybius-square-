from tkinter import Frame, BOTH, TOP, END
from Modules.Modules.Button import Button as btn


class FrameButtons:
    def __init__(self, master, crypt,decrypt, width=200, height=100):
        self.frame = Frame(master, width=width, height=height)
        self.frame.pack(fill=BOTH, side=TOP, expand=True)
        self.btn_encryption = btn(self.frame, "Encrypt", crypt)
        self.btn_decryption = btn(self.frame, "Decrypt", decrypt, column=1)

