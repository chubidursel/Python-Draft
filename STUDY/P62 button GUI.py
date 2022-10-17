from tkinter import *

# button = you click it, then it does stuff.

count = 0
def click():
    global count #Global variables can be used by everyone, both inside of functions and outside.
    count+=1
    print(count)

#def click():    #what my click function does
#    print("You mf clicked the button! u fcked!")

window = Tk()

photo = PhotoImage(file="C:\\Users\\User\\PycharmProjects\\pythonProject\\supplies\\ETH.png")

button = Button(window,
                text="click me bitch!",
                command=click, #callback, send the function to def click()
                font=("Comic Sans", 30),
                fg='red', #hex value or name
                bg="yellow",
                activeforeground="blue", #text when u click on it
                activebackground="pink",
                image=photo,
                compound="top"
                )
button.pack()
#button.pack(expand=True, fill="both")

window.mainloop()