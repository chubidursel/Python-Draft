from tkinter import *
# moving object above the canvas (полотно)

def move_up(event):
    # function .move(image, x, y)
    canvas.move(car,0,-30)
def move_down(event):
    canvas.move(car,0,30)
def move_left(event):
    canvas.move(car,-30,0)
def move_right(event):
    canvas.move(car,30,0)


window = Tk()

window.bind("<w>",move_up)
window.bind("<s>",move_down)
window.bind("<a>",move_left)
window.bind("<d>",move_right)


canvas = Canvas(window,height=500,width=500, bg="#F6F4D8")
canvas.pack()

car_pic = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\pythonProject\\!practice\\supplies\\car.png')
car = canvas.create_image(0,0,image=car_pic,anchor=NW) #anchor>>anchoring our image (NW = north-west)
window.mainloop()
