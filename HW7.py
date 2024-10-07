#Name: Colin Opitz
#Class: 6th Hour
#Assignment: HW7

#1. Print Hello World!
print("Hello World!")
#2. Create three different boolean variables named wifi, login, and admin.
wifi = True
login = True
admin = True
#3. Create a separate integer variable that denotes the number of times
#someone with admin credentials has logged in.
adminlogincredentials = 0
#4. Create a nested if statement that checks to see if wifi is true,
#login is true, and admin is true. If they are all true, print a
#welcome message and increase the integer variable by one. If one of them
#is false, print an error message telling them which one they are "missing".
if wifi:
    if login:
        if admin:
            print("Welcome!")
            adminlogincredentials += 1
            print(f"Admin login count increased: {adminlogincredentials} ")
        else:
            print("Error admin not detected.")
    else:
        print("Error login info incorrect.")
else:
    print("Error no wifi connection.")
