#Name: Colin Opitz
#Class: 6th Hour
#Assignment: HW24

import random, time

#1. Copy over your class from HW23 and all the functions inside of it, and alter any functions to use self if applicable.
class Character:
    def __init__(self, health, damage, speed, max_health, name):
        self.health = health
        self.damage = damage
        self.speed = speed
        self.max_health = max_health
        self.name = name
    def damage_party_member(self):
        for i in range(10):
            time.sleep(1)
            self.health -= random.randint(1, 6)
            print(f"The {randomChoice.name} damaged health: {randomChoice.health}")

    def super_heal(self):
        self.health += 30
        if self.health > 100:
            self.health = 100

#2. Create a fourth attribute in the class called max_health that has the same values as health

#3. Copy the warrior and healer objects from HW23, and then make two more character objects with the following attribute values: thief (health/max: 50, damage: 30, speed: 40) and mage (health/max: 45, damage:35, speed: 25)
theWarrior = Character(100, 20, 30, 100, "Warrior")
theHealer = Character(60, 10, 30, 60, "Healer")
theThief = Character(50, 30, 40, 50, "Thief")
theMage = Character(45, 35, 25, 45, "Mage")
#4. Randomly choose one of the four character objects to take the damage over time function and call the function to them
partyChoice = (theWarrior, theHealer, theThief, theMage)
randomChoice = random.choice(partyChoice)

print(f"{randomChoice.name} got hit.")

randomChoice.damage_party_member()
#5. Determine who lost health by comparing the current health to the max_health and heal that character object by calling your healing function to that object and then print their health afterwards.
randomChoice.super_heal()

print(f"{randomChoice.name} healed health:{randomChoice.health}")
