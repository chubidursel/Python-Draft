from tkinter import *
import time

WIDTH = 700
HEIGHT = 600
xVelocity = 2 #Velocity = speed
yVelocity = 2

window = Tk()

canvas = Canvas(window,width=WIDTH,height=HEIGHT)
canvas.pack()

background_photo = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\pythonProject\\!!!!PRACTICE!\\supplies\\space.png')
background = canvas.create_image(0,0,image=background_photo,anchor=NW)

photo_image = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\pythonProject\\!!!!PRACTICE!\\supplies\\eth.png')
my_image = canvas.create_image(0,0,image=photo_image,anchor=NW)

#here we use function .width() to figure out the width of this pic.
# And leter we subtract width of this image from the whole width,
# so our object can bounce back and it wont cut off.
image_width = photo_image.width()
image_height = photo_image.height()

while True:
    # .coords = function that gets the coordinates of ur pic.
    coordinates = canvas.coords(my_image)
    print(coordinates)
    if(coordinates[0]>=(WIDTH-image_width) or coordinates[0]<0):
        xVelocity = -xVelocity #when the object reaches the right border, its going to bounce back
    if(coordinates[1]>=(HEIGHT-image_height) or coordinates[1]<0):
        yVelocity = -yVelocity
    canvas.move(my_image,xVelocity,yVelocity)
    window.update()
    time.sleep(0.01)

window.mainloop()