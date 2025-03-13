#Name: Colin Opitz
#Class: 6th Hour
#Assignment: Scenario8
import random

#Scenario 8:
#With a fresh perspective, the team lead wants you to look back and refactor the old combat code to
#be streamlined with classes so the character and enemy stats won't be built in bulky dictionaries anymore.
class Party:
    def __init__(self, health, AC, atkMod, damage):
        self.health = health
        self.AC = AC
        self.atkMod = atkMod
        self.damage = damage

theLaezel = Party(12, 17, 5, random.randint(1,6) + random.randint(1,6) + 3)
theShadowheart = Party(10, 14, 3, random.randint(1,6) + 3)
theGale = Party(8, 14, 5, random.randint(1,10))
theAstarion = Party(10, 14, 5, random.randint(1,6) + 4)
theGoblin = Party(6, 12, 5, random.randint(1,6) + 4)
theOrc = Party(14, 14, 5, random.randint(1,6) + 4)
theTroll = Party(22, 13, 5, random.randint(1,6) + 4)
theDragon = Party(56, 17, 5, random.randint(1,6) + 4)
theMindflayer = Party(110, 16, 5, random.randint(1,6) + 4)
#(Translation: Rebuild Scenario 3 using classes instead of dictionaries, include the combat test code
#below as well.)
if random.randint(1,20) + theShadowheart.atkMod >= theGoblin.AC:
#   We hit! Deal Damage (subtract Party Damage Roll from HP)
    theGoblin.health -= theShadowheart.damage
    #Check to see if enemy is dead
    if theGoblin.health <= 0:
        print("Gobbo was hit! Gobbo is dead!")
        exit()
    #else, go to enemy turn
    else:
        print("Gobbo was hit! Gobbo is still alive!")
#else, we miss
else:
    print("Shadowheart Missed!")

if random.randint(1,20) + theGoblin.atkMod >= theShadowheart.AC:
    theShadowheart.health -= theGoblin.damage
    if theShadowheart.health <= 0:
        print("Gobbo hit! Shadowheart is down!")
        exit()
    else:
        print("Gobbo hit! Shadowheart is alive!")
else:
    print("No one hit!")