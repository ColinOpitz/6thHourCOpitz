#Name: Colin Opitz
#Class: 6th Hour
#Assignment: Scenario 2

#The programmer in charge of the player character party stats is having some issues with their code.
# Despite rigorous testing, they are inexperienced and can't seem to figure out why the damage testing isn't working.
# Your team lead has asked you to help by fixing the party dictionary, insert an enemy into the code below,
# and testing to see if a player character can damage the enemy with a printed test that shows the enemy health has changed.
partyDictionary = {
    "LaeZel" : {
        "Race" : "Githyanki",
        "Class" : "Fighter",
        "Background" : "Soldier",
        "Health" : 12,
        "AC" : 17,
        "Damage" : 10,
    },
    "Shadowheart" : {
        "Race" : "Half-Elf",
        "Class" : "Cleric",
        "Background" : "Acolyte",
        "Health" : 10,
        "AC" : 14,
        "Damage" : 5,
    },
    "Gale" : {
        "Race" : "Human",
        "Class" : "Wizard",
        "Background" : "Sage",
        "Health" : 8,
        "AC" : 14,
        "Damage" : 17,
    },
    "Astarion" : {
        "Race" : "High Elf",
        "Class" : "Rogue",
        "Background" : "Charlatan",
        "Health" : 10,
        "AC" : 14,
        "Damage" : 12,
    }
}

#Enemy Dictionary goes here
tyranidDict = {
    "enemy1" : {
     "Name" : "Termagant",
    "Combat Type" : "Ranged",
        "Size" : "Small",
        "Damage Per Attack" : 3,
        "Health" : 8
    },
    "enemy2": {
        "Name" : "Hormagaunt",
        "Combat Type" : "Melee",
        "Size" : "Small",
        "Damage Per Attack" : 3,
        "Health" : 10

    },
    "enemy3" : {
        "Name" : "Hive Tyrant",
        "Combat Type" : "Both",
        "Size" : " Large",
        "Damage Per Attack" : 20,
        "Health" : 100

    },
    "enemy4" : {
        "Name" : "Carnifex",
        "Combat Type" : "Melee",
        "Size" : "Large",
        "Damage Per Attack" : 30,
        "Health" : 140

    },
    "enemy5" : {
        "Name" : "Zoanthrope",
        "Combat Type" : "Ranged",
        "Size" : "Medium",
        "Damage Per Attack" : 25,
        "Health" : 40,

    }

}

#Test the damage here by subtracting a party member's damage from the enemy's health.
print("Shadowheart vs. Termagaunt =", tyranidDict["enemy1"]["Health"]-partyDictionary["Shadowheart"]["Damage"])
print("LaeZel vs. Hormogaunt =", tyranidDict["enemy2"]["Health"]-partyDictionary["LaeZel"]["Damage"])
print("Gale vs. Hive Tyrant =", tyranidDict["enemy3"]["Health"]-partyDictionary["Gale"]["Damage"])
print("Astarion vs. Carnifex =", tyranidDict["enemy4"]["Health"]-partyDictionary["Astarion"]["Damage"])
print("Shadowheart vs. Zoanthrope =", tyranidDict["enemy5"]["Health"]-partyDictionary["Shadowheart"]["Damage"])


