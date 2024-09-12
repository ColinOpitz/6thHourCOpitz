# 1. Print Hello World!
print("Hello World!")

# 2. Create a dictionary with 3 keys and a value for each key.One of the keys must have a value with a list containing
# three numbers inside.
eveeDict = {
    "Type" : "Fire",
    "Name" : "Flareon",
"Number" : [1,3,6]
}
# One of the keys must have a value with a list containing

# three numbers inside.


# 3. Print one of the three numbers by itself
print(eveeDict["Number"][0])

# 4. Using the update function, add a fourth key to the dictionary and give it a value.
eveeDict.update({"Male": 1})



# 5. Print the entire dictionary
print(eveeDict)

# 6. Clear all of the data inside of the dictionary and print it.
eveeDict.clear()
print(eveeDict)
# 7. Make a nested dictionary with three entries containing the name of another classmate and two other pieces of information within each entry.
sixthHour = {
    "student1" : {
        "Pokemon Type" : "Grass",
        "Name" : "Ryan",
        "Male" : False,
    },
    "student2":{
        "Type" : "Electric",
        "Name" : "Kyle",
        "Male" : True,
    },
    "student3": {
        "Type" : "Flying",
        "Name" : "Logan Bond",
        "Male" : True,
    }
}



# 8. Print the names of all three classmates on the same line.
print(sixthHour["student1"]["Name"],sixthHour["student2"]["Name"],sixthHour["student3"]["Name"])