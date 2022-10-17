from tkinter import *
from tkinter import colorchooser #submodule

def click():
    color = colorchooser.askcolor()
    print(color)
    colorHex = color[1] #we extract the Hexadecimal value
    print(colorHex)
    window.config(bg=colorHex) #change background color

window = Tk()

window.geometry("420x420")
button = Button(text="click me bitch!", command=click)
button.pack()

window.mainloop()