#Name: Colin Opitz
#Class: 6th Hour
#Assingment: HW5

#1. Print "Hello World!"
print("Hello World!")
#2. Create a list that contains 3 integers
numList = [1,2,76]
#3. Create an if statement that prints out whichever of the three numbers is the highest

if numList[0] > numList[1] and numList[0] > numList[2]:
    print("A is the biggest number.")
elif numList[2] > numList[0] and numList[2] > numList[1]:
        print("C is the biggest number.")
elif  numList[1] > numList[0] and numList[1] > numList[2]:
    print("B is the biggest number.")
else:
        print("All equal.")


