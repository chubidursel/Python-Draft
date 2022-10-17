from tkinter import *
import random

def next_turn(row, column):

    global player

    if buttons[row][column]['text'] == "" and check_winner() is False:

        if player == players[0]:

            buttons[row][column]['text'] = player

            # if there is no winner we will swap player
            if check_winner() is False:
                player = players[1]
                label.config(text=(player[1]+" turn"))

            elif check_winner() is True:
                label.config(text=(player[0]+" wins"))

            elif check_winner() == "Tie":
                label.config(text=("TIE MF!"))
        else:
            buttons[row][column]['text'] = player

            # if there is no winner we will swap player
            if check_winner() is False:
                player = players[0]
                label.config(text=(player[0]+" turn"))

            elif check_winner() is True:
                label.config(text=(player[1]+" wins"))

            elif check_winner() == "Tie":
                label.config(text=("TIE MF!"))

def check_winner():
    # Checking Horizontal win conditions (clicked by the same player)
    for row in range(3):
        if buttons[row][0]["text"] == buttons[row][1]['text'] == buttons[row][2]["text"] != "":
            #change the color for buttons in case one player won!
            buttons[row][0].config(bg="#0040FF")
            buttons[row][1].config(bg="#0040FF")
            buttons[row][2].config(bg="#0040FF")
            return True

    # Checking Vertical win conditions
    for column in range(3):
        if buttons[0][column]["text"] == buttons[1][column]['text'] == buttons[2][column]["text"] != "":
            buttons[0][column].config(bg="#0040FF")
            buttons[1][column].config(bg="#0040FF")
            buttons[2][column].config(bg="#0040FF")
            return True

    # Checking DIAGONAL win conditions
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        buttons[0][0].config(bg="#0040FF")
        buttons[1][1].config(bg="#0040FF")
        buttons[2][2].config(bg="#0040FF")
        return True

    elif buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        buttons[0][2].config(bg="#0040FF")
        buttons[1][1].config(bg="#0040FF")
        buttons[2][0].config(bg="#0040FF")
        return True

    elif empty_spaces() is False:
        # TIE >> change all buttons in yellow
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="yellow")

        return "Tie"
    else:
        return False

def empty_spaces():

    spaces = 9

    for row in range(3):
        for column in range(3):
            if buttons[row][column]["text"] !="":
                spaces -=1

    if spaces == 0:
        return False
    else:
        return True

def new_game():

     global player

     player = random.choice(players)

     label.config(text=player+" turn")

     for row in range(3):
         for column in range(3):
             buttons[row][column].config(text="", bg="#F0F0F0")

window = Tk()
window.title("Tic-Tac-Toe")
players = ["X","0"]
player = random.choice(players)
buttons = [[0,0,0],
           [0,0,0],
           [0,0,0]]
label = Label(text= player + " turn", font=("Impact", 40))
label.pack(side='top')

reset_button = Button(text='restart', font=("Impact", 21), command=new_game)
reset_button.pack(side='top')

frame = Frame(window)
frame.pack()

#nested for loop to pack with buttons
for row in range(3):
    for column in range(3): #inner for loop
        buttons[row][column] = Button(frame, text="",font=("Impact", 40), width=5,height=2,
                                      command= lambda row=row, column=column: next_turn(row, column))
        buttons[row][column].grid(row=row, column=column)



window.mainloop()