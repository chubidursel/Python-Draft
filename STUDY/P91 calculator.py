from tkinter import *

def button_press(num):

    global equation_text

    equation_text = equation_text + str(num)

    equation_label.set(equation_text)


def equals():
    global equation_text
    try:

        total = str(eval(equation_text)) # eval>> will parse (анализировать) the expression that we pass in
        equation_label.set(total)
        equation_text = total

    except ZeroDivisionError:

        equation_label.set("Are u idiot?\n U can't divide by 0!")

        equation_text = ""
    except SyntaxError:
        equation_label.set("Fck off!\n U can't type such shit!")

        equation_text = ""


def clear():
    global equation_text

    equation_label.set("")

    equation_text = ""

window = Tk()
window.title("best fck CANCULATOR!")
window.geometry("435x510")
window.config(bg="#FFF9A9")

# (уравнение)
equation_text = ""

equation_label = StringVar()

label = Label(window, textvariable=equation_label, font=("consolas", 21), bg="white", width=29, height=3 , relief=GROOVE)
label.pack()

frame = Frame(window)
frame.pack()

button1 = Button(frame, text=1, height=3, width=9, font=35,
                 command=lambda: button_press(1))
button1.grid(row=0, column=0)

button2 = Button(frame, text=2, height=3, width=9, font=35,
                 command=lambda: button_press(2))
button2.grid(row=0, column=1)

button3 = Button(frame, text=3, height=3, width=9, font=35,
                 command=lambda: button_press(3))
button3.grid(row=0, column=2)

button4 = Button(frame, text=4, height=3, width=9, font=35,
                 command=lambda: button_press(4))
button4.grid(row=1, column=0)

button5 = Button(frame, text=5, height=3, width=9, font=35,
                 command=lambda: button_press(5))
button5.grid(row=1, column=1)

button6 = Button(frame, text=6, height=3, width=9, font=35,
                 command=lambda: button_press(6))
button6.grid(row=1, column=2)

button7 = Button(frame, text=7, height=3, width=9, font=35,
                 command=lambda: button_press(7))
button7.grid(row=2, column=0)

button8 = Button(frame, text=8, height=3, width=9, font=35,
                 command=lambda: button_press(8))
button8.grid(row=2, column=1)

button9 = Button(frame, text=9, height=3, width=9, font=35,
                 command=lambda: button_press(9))
button9.grid(row=2, column=2)

button0 = Button(frame, text=0, height=3, width=9, font=35,
                 command=lambda: button_press(0))
button0.grid(row=3, column=0)

plus = Button(frame, text="+", bg="#F6A9FF", height=3, width=9, font=35,
                 command=lambda: button_press("+"))
plus.grid(row=0, column=3)

minus = Button(frame, text="-", bg="#95FFF8", height=3, width=9, font=35,
                 command=lambda: button_press("-"))
minus.grid(row=1, column=3)

multiply = Button(frame, text="*",bg="#FF856A", height=3, width=9, font=35,
                 command=lambda: button_press("*"))
multiply.grid(row=2, column=3)

devide = Button(frame, text="/",bg="#4B88FF", height=3, width=9, font=35,
                 command=lambda: button_press("/"))
devide.grid(row=3, column=3)

equal = Button(frame, text="=", height=3, width=9, font=35, command=equals)
equal.grid(row=3, column=2)

decimal = Button(frame, text=".", height=3, width=9, font=35,
                 command=lambda: button_press("."))
decimal.grid(row=3, column=1)

clear = Button(window, text="WIPE THIS SHIT\n \U0001F4A3", height=3, width=38, font=35,
                 command=clear)
clear.pack()



window.mainloop()