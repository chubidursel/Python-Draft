from tkinter import *

def doSomething(event):
    print("Mouse coordinates: " + str(event.x)+","+str(event.y))

def doSomething1(event):
    print("You just pressed scroll wheel")

def doSomething2(event):
    print("How dare you to press right mouse click?!")

window = Tk()

window.bind("<Button-1>",doSomething) #left mouse click
window.bind("<Button-2>",doSomething1) #scroll wheel
window.bind("<Button-3>",doSomething2) #right mouse click
#window.bind("<ButtonRelease>",doSomething)#mousebutton release
#window.bind("<Enter>",doSomething) #enter the window
#window.bind("<Leave>",doSomething) #leave the window
#window.bind("<Motion>",doSomething) #Where the mouse moved

window.mainloop()
