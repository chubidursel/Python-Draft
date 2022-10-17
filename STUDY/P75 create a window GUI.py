# How to create(open) a new window
from tkinter import *

def x():
    print("Does it work?")
def create_window():
    new_window = Tk()       #Toplevel() = new window 'on top' of other windows, linked to a 'bottom' window
                            #Tk() = new independent window

    Button(new_window, text="click this shit", font=("Consolas", 21), width=23, command=x).pack(side=TOP)
    window.destroy()   #close out of old window

window = Tk()

Button(window, text="create new window", font=21, command=create_window).pack()

window.mainloop()