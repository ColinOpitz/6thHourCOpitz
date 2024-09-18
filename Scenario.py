#Class: 6th Hour
#Name: Colin Opitz
#Assignment: Scenario 1

# Scenario 1:

# You are a programmer for a fledgling game developer. Your team lead
# has asked you to create a nested dictionary containing five enemy
# creatures (and their properties) for combat testing.

tyranidDict = {
    "enemy1" : {
     "Name" : "Termagant",
    "Combat Type" : "Ranged",
        "Size" : "Small",
        "Damage Per Attack" : 3
    },
    "enemy2": {
        "Name" : "Hormagaunt",
        "Combat Type" : "Melee",
        "Size" : "Small",
        "Damage Per Attack" : 3

    },
    "enemy3" : {
        "Name" : "Hive Tyrant",
        "Combat Type" : "Both",
        "Size" : " Large",
        "Damage Per Attack" : 20

    },
    "enemy4" : {
        "Name" : "Carnifex",
        "Combat Type" : "Melee",
        "Size" : "Large",
        "Damage Per Attack" : 30

    },
    "enemy5" : {
        "Name" : "Zoanthrope",
        "Combat Type" : "Ranged",
        "Size" : "Medium",
        "Damage Per Attack" : 25

    }

}


# Additionally, the testers are asking for a way to input changes to the enemy's
# damage for balancing, as well as having it print those changes to
# confirm they went through.
tyranidDict["enemy1"]["Damage Per Attack"] = int(input("How much damage does a single Termagant do?: "))
tyranidDict["enemy2"]["Damage Per Attack"] = int(input("How much damage does a single Hormagaunt do?: "))
tyranidDict["enemy3"]["Damage Per Attack"] = int(input("How much damage does a single Hive Tyrant do?: "))
tyranidDict["enemy4"]["Damage Per Attack"] = int(input("How much damage does a single Carnifex do?: "))
tyranidDict["enemy5"]["Damage Per Attack"] = int(input("How much damage does a single Zoanthrope do?: "))
print(tyranidDict)
# It is up to you to decide what properties are important and the theme of the game