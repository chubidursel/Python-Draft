from tkinter import *
# Drag and Drop refers to moving widget while holding left click pressed.
# One can drag the widget or object in the x-axis or y-axis.

def drag_start(event):
    # = event.widget >>> this is going to get the widget of the event that we'r dealing with
    # (so if u drag particular label"widget" another will stay at the same place as before)
    widget = event.widget
    widget.startX = event.x
    widget.startY = event.y

def drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget.startX + event.x
    y = widget.winfo_y() - widget.startY + event.y
    widget.place(x=x,y=y)

window = Tk()
window.geometry("420x420")
window.configure(bg="#CE98E5") #change colour of the background

label = Label(window,bg="yellow",width=35,height=7)
label.place(x=7,y=7)

label2 = Label(window,bg="blue",width=35,height=7)
label2.place(x=100,y=100)

# name of the widget >> label
# function (which can take 2 arguments)  >>> .bind
# (event, function) |||| event = left mouse click / function = look above
# <B1-Motion> is holding left click
label.bind("<Button-1>",drag_start)
label.bind("<B1-Motion>",drag_motion)

label2.bind("<Button-1>",drag_start)
label2.bind("<B1-Motion>",drag_motion)

window.mainloop()