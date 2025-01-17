#Name: Colin Opitz
#Class: 6th Hour
#Assignment: HW16

#1. Create a def function that plays a single round of rock, paper, scissors where the user inputs
#1 for rock, 2 for paper, or 3 for scissors and compares it to a random number generated to serve
#as the "opponent's hand".
import random


def rock_paper_scissors():
    playerchoice = input("Choose Rock, Paper, or Scissors: ")
    optionschoice = ["Rock", "Paper", "Scissors"]
    opponentchoice = random.choice(optionschoice)

    print("You chose: ", playerchoice)

    print("Computer chose: ", opponentchoice)

    if playerchoice == opponentchoice:

        print("It's a tie!")

    elif playerchoice == "Rock" and opponentchoice == "Scissors":

        print("You win!")

    elif playerchoice == "Paper" and opponentchoice == "Rock":

        print("You win!")

    elif playerchoice == "Scissors" and opponentchoice == "Paper":

        print("You win!")

    else:

        print("Computer wins!")


replayinput = input("Would like to play again? Y/N ")
if replayinput == "Y":
    rock_paper_scissors()
else:
    exit()

rock_paper_scissors()
#2. Create a def function that prompts the user to input if they want to play another round, and
#repeats the RPS def function if they do or exits the code if they don't.

