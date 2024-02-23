import tkinter as tk
from tkinter import END, Button
from PolybiusSquare.PolybiusSquare import PolybiusSquare as ps
from Modules.Frames.FrameSeed import FrameSeed as fsd
from Modules.Frames.FrameInput import FrameInput as fi
from Modules.Frames.FrameCopy import FrameCopy as fc
from Modules.Frames.FrameSelection import FrameSelection as fs
from Modules.Frames.FrameButtons import FrameButtons as fb
import string


def crypt():
    logic = ps(check_buttons())
    generate()
    frameLeftOut.openText.txt_input.delete('1.0', END)
    frameLeftOut.openText.txt_input.insert("1.0", logic.start(frameLeftInput.openText.txt_input.get("1.0", 'end-1c'),
                                                              frameSeed.seedModule.ent_input.get()))
    window.update()


def decrypt():
    logic = ps(check_buttons())
    generate()
    frameLeftOut.openText.txt_input.delete('1.0', END)
    frameLeftOut.openText.txt_input.insert("1.0", logic.start(frameLeftInput.openText.txt_input.get("1.0", 'end-1c'),
                                                              frameSeed.seedModule.ent_input.get(),
                                                              reverse=True))
    window.update()


def generate():
    alphabet = check_buttons()
    logic = ps(alphabet)
    key = logic.get_key(frameSeed.seedModule.ent_input.get())
    alpha()
    frameRightBot.openText.txt_input.delete('1.0', END)
    frameRightBot.openText.txt_input.insert("1.0", key)

def copyOutput():
    text = frameLeftOut.openText.txt_input.get("1.0", 'end-1c')
    window.clipboard_clear()
    window.clipboard_append(text)
    window.update()

def copyKey():
    text = frameRightBot.openText.txt_input.get("1.0", 'end-1c')
    window.clipboard_clear()
    window.clipboard_append(text)
    window.update()


def alpha():
    frameRightTop.openText.txt_input.delete('1.0', END)
    frameRightTop.openText.txt_input.insert("1.0", str(check_buttons()))
    window.update()

def _onKeyRelease(event):
    ctrl  = (event.state & 0x4) != 0
    if event.keycode==88 and  ctrl and event.keysym.lower() != "x":
        event.widget.event_generate("<<Cut>>")

    if event.keycode==86 and  ctrl and event.keysym.lower() != "v":
        event.widget.event_generate("<<Paste>>")

    if event.keycode==67 and  ctrl and event.keysym.lower() != "c":
        event.widget.event_generate("<<Copy>>")

def check_buttons():
    alphabet = list()
    if frameSelection.checkButtonsModule.buttons["lower"].enabled.get():
        alphabet += list(string.ascii_lowercase)
    if frameSelection.checkButtonsModule.buttons["upper"].enabled.get():
        alphabet += list(string.ascii_uppercase)
    if frameSelection.checkButtonsModule.buttons["numeric"].enabled.get():
        alphabet += list(string.digits)
    if frameSelection.checkButtonsModule.buttons["symbol"].enabled.get():
        alphabet += list(string.punctuation)+list("\n")+list("\t")
    if frameSelection.checkButtonsModule.buttons["space"].enabled.get():
        alphabet += list(" ")
    if frameSelection.checkButtonsModule.buttons["ru"].enabled.get():
        alphabet += list("абвгдеёжзийклмнопрстуфхцчшщъыьэюя")
    if frameSelection.checkButtonsModule.buttons["RU"].enabled.get():
        alphabet += list("АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ")
    return alphabet


window = tk.Tk()
window.title("Polybius Square Crypting")
window.minsize(680, 680)
window.bind_all("<Key>", _onKeyRelease, "+")
window.geometry("680x680")

frameLeft = tk.Frame(master=window, width=200, height=100)
frameLeft.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

frameRight = tk.Frame(master=window, width=200)
frameRight.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

frameLeftInput = fi(frameLeft, "text")
frameLeftButtons = fb(frameLeft, crypt, decrypt)

frameLeftOut = fc(master=frameLeft, text="Output",command=copyOutput)

frameRightTop = fi(frameRight, "Alphabet")
frameSelection = fs(frameRight)

frameSeed = fsd(frameRight, generate)

frameRightBot = fc(master=frameRight, text="Key", command=copyKey)
alpha()
window.mainloop()
