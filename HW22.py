#Name: Colin Opitz
#Class: 6th Hour
#Assignment: HW22

#1. Create a class containing a def function that inits self and 3 other attributes for store items (stock, cost, and weight).
class Items:
    def __init__(self, stock, cost, weight):
        self.stock = stock
        self.cost = cost
        self.weight = weight
    def double_cost(self):
        self.cost *= 2
#2. Make 3 objects to serve as your store items and give them values to those 3 attributes defined in the class.
theBanana = Items(40, 8, 5)
theCookie = Items(60, 9.99, 10)
haloReach = Items(20, 29.99, 0.5)
#3. Print the stock of all three objects and the cost of the second store item.
print(f"The stock of Bananas are: {theBanana.stock}")
print(f"The stock of Cookies are: {theCookie.stock}")
print(f"The stock of Halo Reach is: {haloReach.stock}")
print(f"The price of the Cookies are: {theCookie.cost}")

#4. Make a def function within the class that doubles the cost an item, double the cost of the second store item, and print the new cost below the original cost print statement.
theCookie.double_cost()
print(f"The Cookies new price is: {theCookie.cost}")
#5. Directly change the stock of the third store item to approx. 1/4th the original stock and then print the new stock amount.
haloReach.stock = 5
print(f"The new stock of Halo Reach is: {haloReach.stock}")
#6. Delete the first store item and then attempt to print the weight of the first store item. Create a try/except catch to fix the error.
del theBanana
try:
    print(f"The weight of the Bananas are: {theBanana.weight}")
except:
    print("Bananas don't exist :(")