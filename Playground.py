#Colin Opitz
#Playground
#6th Hour
#Code Used https://realpython.com/python-rock-paper-scissors/

print("Hello World")
import random
userName = input("What is your name? ")
print("Hello", userName)
input("Would you like to play Rock Paper Scissors?")

def rock_paper_scissors():
    user_action = input("Enter a choice(rock, paper, scissors:"   )
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    print(f"You chose {user_action}, computer chose {computer_action}.")
    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")

rock_paper_scissors()