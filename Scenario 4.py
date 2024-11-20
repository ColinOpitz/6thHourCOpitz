#Name: Colin Opitz
#Class: 6th Hour
#Assignment: Scenario 4

#Scenario 4:
#Due to scope creep leading to high development costs, the RPG you were working on has been
#shelved for the time being. You have been transferred to a new team working on a mobile game
#that allows you to dress up a model and rate other models in a "Project Runway" style competition.

#They want to start prototyping the rating system and are asking you to make it.
#This prototype needs to allow the user to input the number of players, let each player rate
#a single model from 1 to 5, and then give the average score of all of the ratings.

# Step 1. Establish Variables
Players = int(input("How many players are there? "))
RatingTotal = 0
# Step 2. Make a loop
for i in range (1, Players+1):

# Step 2a. Ask for a rating number
    Rating = int(input("Rate these models 1-5! "))

# Step 2b. Check if rating number is between 1 and 5
    if Rating < 1 or Rating > 5:
        print("Error rate 1- 5.")
# Step 2c. If rating number is valid, add to total
    else:
        RatingTotal += Rating
# Step 3. Find and print the average
print(RatingTotal/Players)