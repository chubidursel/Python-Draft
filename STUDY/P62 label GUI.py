# label = an area widget that holds text and/or an image within a window

from tkinter import *

window = Tk()

photo = PhotoImage(file="C:\\Users\\User\\PycharmProjects\\pythonProject\\supplies\\BTC.png")

# label(aka widget) = Label ( master, option, ... )
# >>>master − This represents the parent window.
# >>> options − Here is the list of most commonly used options for this widget.
#               These options can be used as key-value pairs separated by commas.

label = Label(window,
              text="Hey mate, How much does 1 BTC cost?",
              font=("Arial", 34, 'bold'),
              fg='#00FF00',
              bg="black",
              relief=RAISED,
              bd=10,
              padx=20,
              pady=21,
              image=photo,
              compound="bottom" ) #combain text and picture
label.pack()
#label.place(x=0,y=0)

window.mainloop()
