from tkinter import *

def display():
    if(x.get()==1):
        print("Hahaha, too late")
    else:
        print("It goes to the moon budyy, veryyy soon!")

window = Tk()

x = IntVar() # or u can choose: BooleanVar() or StringVar()

sol_photo = PhotoImage(file="C:\\Users\\User\\PycharmProjects\\pythonProject\\supplies\\SOL.png")
check_button = Checkbutton(window,
                           text="Do you wanna buy it? jut 80$?",
                           variable=x,
                           onvalue=1,
                           offvalue=0,
                           command=display,
                           font=("Monaco",21),
                           fg="purple",
                           bg="pink",
                           padx=25,
                           pady=21,
                           image=sol_photo,
                           compound='top'
                           )
check_button.pack()
window.mainloop()