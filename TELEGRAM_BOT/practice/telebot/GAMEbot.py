import random

def xxx():
    while True:
        choices = ['rock', 'paper', "scissors"]
        computer = random.choice(choices)
        player = None

        while player not in choices: #while loop - if player does not put something from choices
            player = input('rock , paper or scissors?: ').lower()

        if player == computer:
            print("computer: ",computer)
            print("player: ", player)
            print("Tie!")
        elif player == "rock":
            if computer == "paper":
                print("computer: ", computer)
                print("player: ",player)
                print("You lose!")
            if computer == "scissors":
                print("computer: ", computer)
                print("player: ",player)
                print("You win!")
        elif player == "scissors":
            if computer == "rock":
                print("computer: ", computer)
                print("player: ",player)
                print("You lose!")
            if computer == "paper":
                print("computer: ", computer)
                print("player: ",player)
                print("You win!")
        elif player == "paper":
            if computer == "scissors":
                print("computer: ", computer)
                print("player: ",player)
                print("You lose!")
            if computer == "rock":
                print("computer: ", computer)
                print("player: ",player)
                print("You win!")
        play_again = input("Play again? (yes/no): ")
        if play_again == "no":
            break
    print("Bye sweety!")
