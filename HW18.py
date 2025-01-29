#Name: Colin Opitz
#Class: 6th Hour
#Assignment: HW18
import random

#1. Import the "random" library and create a def function that prints "Hello World!"
def hello_world():
    print("Hello World!")
#2. Create a list called beanBag and add at least 5 different colored beans to the list as strings.
beanBag = ["Red", "Blue", "Green", "Purple", "Brown"]
#3. Create a def function that pulls a random bean out of the beanBag list, prints which bean you pulled, and then removes it from the list.
def bean_pull():
    if not beanBag:
        print("The bag is empty")
    else:
        selectedbean = random.choice(beanBag)
        print(selectedbean)
        beanBag.remove(selectedbean)
        repeat_game()
#4. Create a def function that asks if you want to pull another bean out of the bag and, if yes, repeats the #3 def function
def repeat_game():
    userInput = input("Would you like to pick again? Y/N ")
    if userInput == "Y" or userInput == "y":
        bean_pull()
    elif userInput == "N" or userInput == "n":
        exit()
#5. Call the #3 function at the bottom.
bean_pull()