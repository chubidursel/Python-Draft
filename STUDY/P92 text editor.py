import os
from tkinter import *
from tkinter import filedialog, colorchooser, font
from tkinter.messagebox import *
from tkinter.filedialog import *


def change_color():
    color = colorchooser.askcolor(title="pick a color bitch!")
    text_area.config(fg=color[1])

def change_font(*args):
    text_area.config(font=(font_name.get(), size_box.get()))

def new_file():
    window.title("Untitled")
    text_area.delete(1.0, END)

def open_file():
    file = askopenfilename(defaultextension=".txt", file=[("All Files", "*.*"),
                                                          ("Text Documents", "*.txt")])
    try:
        window.title(os.path.basename(file))
        text_area.delete(1.0, END)

        file = open(file, "r")
        text_area.insert(1.0, file.read())

    except Exception:
        print("I can't read this shit!")

    finally:
        file.close()

def save_file():
    file = filedialog.asksaveasfilename(initialfile='new_file.txt',
                                        defaultextension=".txt",
                                        filetypes=[("All Files", "*.*"),
                                                   ("Text Documents", "*.txt")])

    if file is None:
        return

    else:
        try:
            window.title(os.path.basename(file))
            file = open(file, "w")

            file.write(text_area.get(1.0, END))

        except Exception:
            print("couldn't save file")

        finally:
            file.close()

def cut():
    text_area.event_generate("<<Cut>>")

def copy():
    text_area.event_generate("<<Copy>>")

def paste():
    text_area.event_generate("<<Paste>>")

def about():
    showinfo("About this beautiful program", "Does it work good? u like it? I made this fck app! \n (stole the code tbh, but wrote by myelf) \n If u have any comments go fck urself! i dont give a shit")

#------my shit----
def mybutton():
    showinfo("hahhaaha loser!", "What did u expect?!")
def myfun():
    new_window = Tk()
    new_window.geometry("420x300")
    new_window.config(bg="light green")
    button1 = Button(new_window, text="CLICK!",bg="light yellow", font=("Impact", 70),command=mybutton).pack()

def drag_start(event):
    widget = event.widget
    widget.startX = event.x
    widget.startY = event.y
def drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget.startX + event.x
    y = widget.winfo_y() - widget.startY + event.y
    widget.place(x=x,y=y)
def game():
    new_window1 = Tk()
    new_window1.geometry("420x420")
    new_window1.config(bg="light gray")
    label = Label(new_window1, bg="yellow", width=35, height=7)
    label.place(x=7, y=7)

    label2 = Label(new_window1, bg="blue", width=35, height=7)
    label2.place(x=100, y=100)

    label.bind("<Button-1>", drag_start)
    label.bind("<B1-Motion>", drag_motion)

    label2.bind("<Button-1>", drag_start)
    label2.bind("<B1-Motion>", drag_motion)

def quit():
    window.destroy()
#----------------------------------main body--------------------------------------------
window = Tk()
window.title("word microsoft killer!")
file = None

window_width = 900
window_height = 600
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

window.geometry("{}x{}+{}+{}".format(window_width, window_height, x, y))

font_name = StringVar(window)
font_name.set("Arial")
font_size = StringVar(window)
font_size.set("25")

text_area = Text(window, font=(font_name.get(), font_size.get()))

scroll_bar = Scrollbar(text_area)
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
text_area.grid(sticky= N + E + S + W)

scroll_bar.pack(side=RIGHT, fill=Y)
text_area.config(yscrollcommand=scroll_bar.set)

frame = Frame(window)
frame.grid()

color_button = Button(frame, text="color", command=change_color)
color_button.grid(row=0, column=0)

font_box = OptionMenu(frame, font_name, *font.families(), command=change_font)
font_box.grid(row=0, column= 1)

#A Spinbox widget allows you to select a value from a set of values.
size_box = Spinbox(frame, from_=1, to=100, textvariable=font_size, command=change_font)
size_box.grid(row=0,column = 2)

menu_bar = Menu(window)
window.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File",menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=quit)

edit_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=cut)
edit_menu.add_command(label="Copy", command=copy)
edit_menu.add_command(label="Paste", command=paste)

help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=about)
help_menu.add_command(label="smth interesting", command=myfun)
help_menu.add_command(label="game", command=game)

window.mainloop()