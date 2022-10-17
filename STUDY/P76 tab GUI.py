from tkinter import *
from tkinter import ttk

window = Tk()

notebook = ttk.Notebook(window) #widget that manages a collection of windows/displays

tab1 = Frame(notebook) #new frame for tab 1
tab2 = Frame(notebook)

notebook.add(tab1, text="TAB 1")
notebook.add(tab2, text="TAB 2")
notebook.pack(expand=True, fill="both") #!!!! EXPAND and FILL the space!!!!

Label(tab1, text="Hey mate, this is 1sr TAB", font=25, width=50, height=25).pack()
Label(tab2, text="Yo dudeee, this is 2nd TAB", width=50, font=55, height=25).pack()

window.mainloop()