# frame = a rectangular container to group and hold widgets

from tkinter import *

window = Tk()

frame = Frame(window,bg="pink",bd=5,relief=SUNKEN)
#frame.pack(side=LEFT)
frame.place(x=0,y=0)

#All these buttons we r adding to the frame which is adding to window
Button(frame,text="W",font=("Consolas",25),width=3).pack(side=TOP)
Button(frame,text="A",font=("Consolas",25),width=3).pack(side=LEFT)
Button(frame,text="S",font=("Consolas",25),width=3).pack(side=LEFT)
Button(frame,text="D",font=("Consolas",25),width=3).pack(side=LEFT)

window.mainloop()