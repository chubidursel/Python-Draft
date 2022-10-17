# radio button = similar to checkbox, but you can only select one from a group
from tkinter import *

crypto = ["BTC","ETH","SOL"]

def order():
    if(x.get()==0):
        print("BTC = 39,567$")
    elif(x.get()==1):
        print("ETH = 2,604$")
    elif(x.get()==2):
        print("SOL = 82.5$")
    else:
        print("Or u wanna buy DOGE?")

window = Tk()

BTC = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\pythonProject\\supplies\\BTC.png')
ETH = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\pythonProject\\supplies\\ETH.png')
SOL = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\pythonProject\\supplies\\SOL.png')
crypto_pic = [BTC,ETH,SOL]

x = IntVar()

for index in range(len(crypto)): #we can iterate (перебирать) through all of items within our list
    radiobutton = Radiobutton(window,
                              text=crypto[index], #adds text to radio buttons
                              variable=x, #groups radiobuttons together if they share the same variable
                              value=index, #assigns each radiobutton a different value (selecet only 1)
                              padx = 25, #adds padding on x-axis
                              font=("Impact",50),
                              image = crypto_pic[index], #adds image to radiobutton
                              compound = 'left', #adds image & text (left-side)
                              indicatoron=0, #eliminate circle indicators
                              width = 375, #sets width of radio buttons
                              command=order #set command of radiobutton to function
                              )
    radiobutton.pack(anchor=W)
window.mainloop()