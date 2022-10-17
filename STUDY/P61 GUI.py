# GUI = graphical user interface

# widgets = GUI elements: buttons, textboxes, labels, images
# window = serves as a container to hold or contain these widgets

from tkinter import *

window = Tk() #instantiate an instance of a window (создать экземпляр окна)
window.geometry("420x420") #change the size
window.title("The best GUI program ever") #change the name

icon = PhotoImage(file="LOGO.png")#add logo to GUI
window.iconphoto(True,icon) #convert

window.config(background="black")
# config = configuration
window.mainloop() #display window on computer screen, listen for events.