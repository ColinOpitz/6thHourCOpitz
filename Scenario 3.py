#Name: Colin Opitz
#Class: 6th Hour
#Assignment: Scenario 3
#Scenario 3:
#Now that the game development team has a dictionary for enemies
#(see Scenario 1) and the dictionary for the party is fixed
#(see Scenario 2), they want to start making a full prototype for the
#combat system. The team lead is a big Dungeons & Dragons fan and
#wants to make the combat similar to that. Because of this, the
#dictionaries need to be reworked slightly to be like that.

#Each enemy and party member in both dictionaries needs:
# - health points (somewhere between 6 and 25)
# - an attack modifier (somewhere between 3 and 7)
# - a damage roll (a number that varies based on weapon/spell)
# - and an Armor Class (somewhere between 10 and 17).

#Once both dictionaries are updated, create a combat
#prototype that has a party member attack first, then an enemy
#attacks back right after.

#To determine if a creature hits another creature, you roll a
#20-sided die (d20) and add the attack modifier to the roll.
#If that number is the same as or higher than the enemy's Armor Class
#(AC), the attack hits and you roll for damage. If it is lower, the
#attack misses. If an enemy or party member hits zero (0) health
#points, they die.

#To make things easier, here is a reference list for party damage rolls.
#(Feel free to use similar numbers for your enemy dictionary.)

# - Lae'Zel uses a greatsword: 2d6 + 3
# - Shadowheart uses a mace: 1d6 + 2
# - Gale uses the firebolt spell: 1d10
# - Astarion uses a shortbow: 1d6 + 4


import random

#Party Dictionary Goes Here
partyDictionary = {
    "LaeZel" : {
        "Race" : "Githyanki",
        "Class" : "Fighter",
        "Background" : "Soldier",
        "Health" : 12,
        "AC" : 17,
        "Damage" : random.randint(1, 6) * 2 + 3,
        "ATCKMOD" : 3
    },
    "Shadowheart" : {
        "Race" : "Half-Elf",
        "Class" : "Cleric",
        "Background" : "Acolyte",
        "Health" : 10,
        "AC" : 14,
        "Damage" : random.randint(1, 6,) + 3,
        "ATCKMOD" : 3,

    },
    "Gale" : {
        "Race" : "Human",
        "Class" : "Wizard",
        "Background" : "Sage",
        "Health" : 8,
        "AC" : 14,
        "Damage" : random.randint(1, 10) + 4,
        "ATCKMOD" : 4
    },
    "Astarion" : {
        "Race" : "High Elf",
        "Class" : "Rogue",
        "Background" : "Charlatan",
        "Health" : 10,
        "AC" : 14,
        "Damage" : random.randint(1, 6) + 3,
        "ATCKMOD" : 3
    }
}

#Enemy Dictionary goes here
tyranidDict = {
    "enemy1" : {
     "Name" : "Termagant",
    "Combat Type" : "Ranged",
        "Size" : "Small",
        "Damage" : random.randint(1, 6) + 3,
        "Health" : 8,
        "AC" : 10,
        "ATCKMOD" : 3
    },
    "enemy2": {
        "Name" : "Hormagaunt",
        "Combat Type" : "Melee",
        "Size" : "Small",
        "Damage" : random.randint(1, 5) + 3,
        "Health" : 10,
        "AC" : 10,
        "ATCKMOD" : 3
    },
    "enemy3" : {
        "Name" : "Hive Tyrant",
        "Combat Type" : "Both",
        "Size" : " Large",
        "Damage" : random.randint(1, 6) * 3 + 7,
        "Health" : 25,
        "AC" : 15,
        "ATCKMOD" : 7

    },
    "enemy4" : {
        "Name" : "Carnifex",
        "Combat Type" : "Melee",
        "Size" : "Large",
        "Damage" : random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6),
        "Health" : 25,
        "AC" : 17,
        "ATCKMOD" : 6

    },
    "enemy5" : {
        "Name" : "Zoanthrope",
        "Combat Type" : "Ranged",
        "Size" : "Medium",
        "Damage" : random.randint(1, 6) + 4,
        "Health" : 20,
        "AC" : 12,
        "ATCKMOD" : 4

    }
}
#To determine if a creature hits another creature, you roll a
#20-sided die (d20) and add the attack modifier to the roll.
#If that number is the same as or higher than the enemy's Armor Class
#(AC), the attack hits and you roll for damage. If it is lower, the
#attack misses. If an enemy or party member hits zero (0) health
#points, they die.
#Combat Code Goes Here

#Step 7: Roll the attack roll for party member (d20 + Attack Modifier)

#Step 8: Check to see if the party member hits the enemy
if random.randint(1, 20) + (tyranidDict["enemy4"]["ATCKMOD"]) >= (partyDictionary["LaeZel"]["AC"]):
    print("Carnifex hit LaeZel!")
    partyDictionary["LaeZel"]["Health"] -= tyranidDict["enemy4"]["Damage"]
    if (partyDictionary["LaeZel"]["Health"]) >= 0:
        print("LaeZel is still alive.")
    else:
        print("LaeZel is dead!")
        exit()
else:
    print("Carnifex missed LaeZel!")
    # Step 9: Roll the damage if it hits, subtract from enemy health

#Step 10: Check to see if the enemy is still alive


#Step 11: If the enemy is alive, repeat steps 7 through 10 but with the enemy attacking
if random.randint(1, 20) + (partyDictionary["LaeZel"]["ATCKMOD"]) >= (tyranidDict["enemy4"]["AC"]):
    print("LaeZel hit Carnifex!")
    tyranidDict["enemy4"]["Health"] -= partyDictionary["LaeZel"]["Damage"]
    if (tyranidDict["enemy4"]["Health"]) >= 0:
        print("Carnifex is still alive.")
    else:
        print("Carnifex is dead!")
        exit()
else:
    print("LaeZel missed Carnifex!")