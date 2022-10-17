from tkinter import *
# .bind function >>  bind (связывать) key and window. And perform some sort of task

def doSomething(event):
    print("You pressed: " + event.keysym)
    label.config(text=event.keysym)

window = Tk()
#     .bind("<name of the button>", funcion)
window.bind("<Key>",doSomething)

label = Label(window,font=("Helvetica",100))
label.pack()

window.mainloop()