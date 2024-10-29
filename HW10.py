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
p = 1
while p <= 30:
    p += 1
    if p % 2 == 0:
        print(p)
#3. Create a while loop that repeats until the user
#inputs the number 0.

l = int(input("Enter a number: "))
while l!= 0:
    print(l)
    l = int(input("Enter a number: "))