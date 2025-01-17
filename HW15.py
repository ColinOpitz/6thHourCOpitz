#Name: Colin Opitz
#Class: 6th Hour
#Assignment: HW15

#1. Create a def function that prints out "Hello World!"
def hello_world():
    print("Hello World!")

#2. Create a def function that calculates the average of three numbers.
def average_of_three(num1, num2, num3):
    return (num1 + num2 + num3) / 3
a = 10
b = 20
c = 30
result = average_of_three(a, b, c)
print("The average is:", result)
#3. Create a def function with the names of 5 animals as arguments, treats it like a list, and
#prints the name of the third animal.
def animal_name(*animal):
    print("The third animal's name is", animal[2])

animal_name("Badger", "Lion", "Snake", "Raven", "Dog")

#4. Create a def function that loops from 1 to the number put in the argument.
numInput = int(input("Pick a number: "))
def number_game(numInput):
    for i in range(1, numInput + 1):
        print(i)

number_game(numInput)
if number_game == numInput:
    number_game(numInput)
else:
    exit()

number_game(numInput)
#5. Call all of the functions created in 1 - 4 with relevant arguments.
hello_world()
average_of_three()
animal_name()
number_game()

