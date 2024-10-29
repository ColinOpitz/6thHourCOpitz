#Name: Colin Opitz
#Class: 6th Hour
#Assignment: HW10

#1. Create a while loop with variable i that counts down from 5 to 0
#and then prints "Hello World!" at the end.
i = 5
while i >= 0:
    print(i)
    i -= 1
else:
    print("Hello World!")
#2. Create a while loop that prints only even numbers
#between 1 and 30.
p = 0
limit = 30

while p <= limit:
    if p % 2 == 0:
        print(p)
        p += 2
#3. Create a while loop that repeats until the user
#inputs the number 0.
k = 0
while True:
    number = int(input("Enter a number: "))
    if number == 0:
        print("You entered the target number!")
        break
    else:
            print("You entered the wrong number.")
            break