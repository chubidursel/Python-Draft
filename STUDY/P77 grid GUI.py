from tkinter import *
# grid() = geometery manadger that organizes widgets in a table-like structure in a parent


window = Tk()
titleLabel = Label(window, text="Enter your info", font=27).grid(row=0,column=0,columnspan=2)

firstNameLabel = Label(window, text="First name: ", width=20,bg="blue").grid(row=1,column=0)
firstNameEntry = Entry(window).grid(row=1,column=1)

lastNameLabel = Label(window, text="Last name: ", bg="yellow").grid(row=2,column=0)
lastNameEntry = Entry(window).grid(row=2,column=1)

emailLabel = Label(window, text="email: ").grid(row=3,column=0)
emailEntry = Entry(window).grid(row=3,column=1)

submitButton = Button(window, text="SUBMIT this shit!").grid(row=4,column=0,columnspan=2)


window.mainloop()