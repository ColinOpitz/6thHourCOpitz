#Name: Colin Opitz
#Class: 6th Hour
#Assignment: Scenario 7

#Import all of Scenario 6 here
from Scenario6 import roll_four_dice, repeat, finalList

listAverage = 0

def final_average():
    global listAverage
    listAverage = sum(finalList) / len(finalList)
    return listAverage

final_average()

print(listAverage)