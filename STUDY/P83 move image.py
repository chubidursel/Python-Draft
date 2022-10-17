#------------move widgets on window-------------
from tkinter import *

#The winfo() method is used to retrieve (извлекать) information about windows managed by Tkinter.
# winfo_x() = Returns a decimal string giving the x-coordinate, in windows parent, of the upper-left corner of windows border
def move_up(event):
   label.place(x=label.winfo_x(), y=label.winfo_y()-15)
def move_down(event):
   label.place(x=label.winfo_x(), y=label.winfo_y()+11)
def move_left(event):
   label.place(x=label.winfo_x()-15, y=label.winfo_y())
def move_right(event):
   label.place(x=label.winfo_x()+15, y=label.winfo_y())

window = Tk()
window.geometry("500x500")

window.bind("<w>",move_up)
window.bind("<s>",move_down)
window.bind("<a>",move_left)
window.bind("<d>",move_right)
window.bind("<Up>",move_up)
window.bind("<Down>",move_down)
window.bind("<Left>",move_left)
window.bind("<Right>",move_right)

myimage = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\pythonProject\\!practice\\supplies\\dog.png')
label = Label(window,image=myimage)
label.place(x=0,y=0)

window.mainloop()