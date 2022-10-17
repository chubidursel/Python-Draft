from tkinter import *
from Ball import *
import time

window = Tk()

WIDTH = 500
HEIGHT = 500

canvas = Canvas(window,width=WIDTH,height=HEIGHT, bg="#F6F4D8")
canvas.pack()
# I have created all characteristic for a bal in another .py file (from Ball import *)
#To add a new ball u just need  to name it, and descrude the characteristic  =Ball(...)
volley_ball = Ball(canvas,0,0,100,1,1,"white")
tennis_ball = Ball(canvas,0,0,50,4,3,"yellow")
basket_ball = Ball(canvas,0,0,125,3,5,"orange")
bowling_ball = Ball(canvas,0,0,75,2,1,"black")

while True:
    volley_ball.move()
    tennis_ball.move()
    basket_ball.move()
    bowling_ball.move()
    window.update()
    time.sleep(0.01)

window.mainloop()
