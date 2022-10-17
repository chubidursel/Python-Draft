from tkinter import *
from tkinter import filedialog

def openFile():
    filepath = filedialog.askopenfilename(initialdir="C:\\Users\\User\\PycharmProjects\\pythonProject",
                                          title='Looking for smth mate?',
                                          filetypes= (("text fiels","*.txt"),
                                                      ("all files","*.*")))


    file = open(filepath, "rt") # "r" >> read
    print(file.read())
    file.close()

window = Tk()

button = Button(text="open",command=openFile)
button.pack()

window.mainloop()