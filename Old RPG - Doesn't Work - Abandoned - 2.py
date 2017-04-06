#Goals
'''
Add the portals to the village in the maze as well as the village (8 / 10)
Add Shards and Affinity [Shards are currency that can buy things, but can be used to improve/decrease the player's affinities that affect spells] (5 / 10)
Make each race start with certain affinities (3 / 10)
Make the tunnels in the beginning important (6.5 / 10)
Add Bosses and special battles (9 / 10)
Story (10 / 10)
'''

import math
import random
import sys
import os

Types = ["Human", "Dwarf", "Elf", "Dragon", "Bird"]
#Class Efficiencies
'''
Elf, Dragon > Human
Human, Bird > Dwarf
Dwarf, Bird > Elf
Elf, Dwarf > Dragon
Human, Dragon > Bird
'''

Spells = ["Attack", "Miscellany", "Defend", "Heal", "Flee", "Blind", "Taunt", "Buff", "Poison", "Bully", "Hammer", "Sing", "Firebreath", "Flight"]
#Spell Effects
'''
Attack     : Regular default attack: does double damage against weaker races, but half damage to stronger races
Miscellany : Figures out random information about the enemy, but also has a chance to explode rapidly healing oneself
Defend     : Triples the user's armor for a turn to reduce incoming damage
Heal       : Heals the user by a small amount, but also removes all poison stacks
Flee       : Sacrifices a major portion of the user's health to escape the battle
Blind      : Turns the enemy's attack to 0 for one turn to reduce incoming damage (won't ever stop the damage completely)
Taunt*     : Increases opponent's attack for the remainder of the battle, but disables their heal for the rest of the battle [MIGHT NEED FIXING: CHECK THIS NOW!!]
Buff       : Does a small boost to the user's armor and damage for the remainder of the battle
Poison     : Adds a stackable debuff that will continuously hurt the enemy for a small amount of damage; stacks don't linearly correlate to damage dealt
Bully      : Does a reduced amount of damage to also remove a stack of poison (because the bullying felt good). If the user is a Human, it also reduces the opponent's armor and damage slightly.
Hammer     : Does normal damage, but it also has the risk (or benefit) of causing a free "Flee" and healing the user to full health. If the user is a Dwarf, it will also increase the EXP that would be gained from the battle if it wasn't fled.
Sing       : Guarantees the kill on the opponent in a random amount of turns, but reduces the user's armor to none, unless the user is an Elf, in which case, the armor will be reduced slightly less than normal
Firebreath : An attack that ignores efficiency of attacks based off of class, but if the user is a Dragon, ignores the effect of class and armor of the spell's damage
Flight     : Cuts the health of the user to gain invulnerability for the next turn; if the user is a Bird, it will cut the health slightly less
Empower    : Can be bought in the village for a huge lump sum of shards. Has the _chance_ to permanently raise one of your stats after the battle
'''

class clear:
    def __call__(self):
        if os.name == ('ce', 'nt', 'dos'):
            os.system('cls')
        elif os.name == 'possix':
            os.system('clear')
        else:
            print ('\n' * 120)
    def __neg__(self):
        self()
    def __repr__(self):
        self();return ''

clear = clear()

class Races:
    def __init__(self, className, good1, good2, bad1, bad2):
        self.Class = className
        self.good1 = good1
        self.good2 = good2
        self.bad1 = bad1
        self.bad2 = bad2
        
Human = Races("Human", "Elf", "Dragon", "Dwarf", "Bird")
Dwarf = Races("Dwarf", "Human", "Bird", "Elf", "Dragon")
Elf = Races("Elf", "Dwarf", "Bird", "Human", "Dragon")
Dragon = Races("Dragon", "Elf", "Dwarf", "Human", "Bird")
Bird = Races("Bird", "Human", "Dragon", "Dwarf", "Elf")

class Village:
    def __init__(self, playerObject):
        self.shards = 0
        self.enemiesCleared = False
        self.timesVisited = 0
        self.timesVisited += 1
        lineA = list("|||||||||||||||||")
        lineB = list("|               |")
        lineC = list("|               |")
        lineD = list("|               |")
        lineE = list("|       P       |")
        lineF = list("|               |")
        lineG = list("|               |")
        lineH = list("|               |")
        lineI = list("|||||||||||||||||")
        self.lines = [lineA, lineB, lineC, lineD, lineE, lineF, lineG, lineH, lineI]
        for i in range(1, 8, 1):
            for j in range(1, 16, 1):
                if (self.lines[i])[j] == " " and random.randint(1, 10) == 1:
                    (self.lines[i])[j] == "E"

    def returnXY(self):
        self.backwardLines = []
        for i in range(0, len(self.lines), 1):
            self.backwardLines.append(self.lines(len(self.lines) - i))
        self.playerX = 0
        self.playerY = 0
        for y in range(0, 9, 1):
            for x in range(0, 17, 1):
                if (backwardLines[y])[x] == "P":
                    self.playerX = x
                    self.playerY = y
                    return [self.playerX, self.playerY]
        return "I CANT FIND THE PLAYER"

    def goToXY(self, currentXY, desiredXY):
        currentX = currentXY[0]
        currentY = currentXY[1]
        if desiredXY[0] == 0 or desiredXY[0] == 8 or desiredXY[1] == 0 or desiredXY[1] == 16:
            if self.checkForEnemies() == False:
                raw_input("You run into an impenetrable wall that surrounds the village. You start wondering how the villagers appeared in the village. Press enter to continue... ")
            else:
                raw_input("These walls seem impenetrable. You decide it\'s best to kill all the enemies here first. ")

    def checkForEnemies(self):
        enemies = False
        for j in range(0, 9, 1):
            for i in range(0, 17, 1):
                if (lines[j])[i] == "E":
                    enemies = True
        if enemies == False:
            for i in range(1, 16, 7):
                (lines[1])[i] = "V"
                (lines[7])[i] = "V"
            (lines[4])[1] = "V"
            (lines[4])[15] = "V"
        return enemies

    def navigateVillage(self, playerObject):
        choice = "Screw listening to instructions!"
        while choice != "w" and choice != "a" and choice != "s" and choice != "d":
            if self.checkForEnemies():
                choice = raw_input("You notice a recently abandoned village with enemies littered everywhere. All the buildings have been razed to the ground. Using \'WASD\', you can move. ")
            else:
                choice = raw_input("Due to the lack of enemies, the villagers have returned with goods to sell. Using \'WASD\', you decide to move in the direction ")
            if len(choice) >= 1:
                choice = choice[0].lower()
        if choice == "w":
            2 + 2

class Character:
    def __init__(self, name, health, armor, damage, tipo, label, startingLevel):
        self.name = name
        self.label = label
        self.totalPossibleHealth = health
        self.health = self.totalPossibleHealth
        self.armor = int(math.sqrt(armor))
        self.damage = damage
        self.race = tipo.Class
        self.good1 = tipo.good1
        self.good2 = tipo.good2
        self.bad1 = tipo.bad1
        self.bad2 = tipo.bad2
        self.spells = []
        self.enemiesKilled = 0
        if startingLevel <= 1:
            self.experience = 2
        else:
            self.experience = 0.02 * startingLevel ** 2
        self.poison = 0
        self.killed = False
        self.extraxp = 1
        self.turnsToDie = 999999999
        self.invuln = 0
        self.choice = ""
        self.inBattle = 0

    def getLevel(self):
        return math.floor(math.sqrt(50 * self.experience))
        
    def takeDamage(self, damageTaken, opposingType):
        if self.invuln <= 0:
            damageTaken = damageTaken - random.randint(int(self.armor - self.armor / 30), int(self.armor + self.armor / 30))
            if damageTaken < 1:
                damageTaken = 1
            if opposingType == self.good1 or opposingType == self.good2:
                self.health -= damageTaken * 2
                raw_input("In a supereffective hit, " + self.label + " took " + str(damageTaken * 2) + " damage and has an hp value that is now " + str(self.health) + " remaining health. Press enter to continue... ")
            elif opposingType == self.bad1 or opposingType == self.bad2:
                self.health -= damageTaken * (0.8)
                raw_input("In a not very effective strike, " + str(damageTaken * 0.8) + " damage was taken by " + self.label + ", and their remaining health is " + str(self.health) + "hp. Press enter to continue... ")
            else:
                self.health -= damageTaken
                raw_input("In a normal strike, " + self.label + " took " + str(damageTaken) + " damage and the hp value has changed to " + str(self.health) + "hp left. Press enter to continue... ")
            if self.health <= 0:
                self.killed = True
        
    def attack(self, opposingClass):
        if random.randint(1, 10) == 1:
            opposingClass.takeDamage(self.damage + self.damage / 15, self.race)
        else:
            self.whatWillBeDealt = random.randint(int(self.damage - self.damage / 30), int(self.damage + self.damage / 30))
            opposingClass.takeDamage(self.whatWillBeDealt, self.race)

    def miscellany(self, opposingClass):
        self.reveal = random.randint(1, 5)
        if self.reveal == 1:
            raw_input("The opponent's name is " + opposingClass.name + ". That's very useful. Press enter to continue... ")
        elif self.reveal == 2:
            raw_input("The opponent's armor rating is " + str(opposingClass.armor) + ". Press enter to continue... ")
        elif self.reveal == 3:
            raw_input("The opponent's damage rating is " + str(opposingClass.damage) + ". Press enter to continue... ")
        elif self.reveal == 4:
            raw_input("The opponent's race is " + str(opposingClass.race) + ". Press enter to continue... ")
        elif self.reveal == 5:
            raw_input("Your miscellany exploded and repeatedly healed you for free. Press enter to continue... ")
            for i in range(1, random.randint(3, 5), 1):
                self.heal()

    def defend(self):
        raw_input("Armor was tripled for " + self.label + " for a turn. Press enter to continue... ")
        self.armor = self.armor * 3

    def heal(self):
        self.health += random.randint(self.totalPossibleHealth / 25 - self.totalPossibleHealth / 30, self.totalPossibleHealth / 25 + self.totalPossibleHealth / 30)
        self.poison = 0
        if self.health > self.totalPossibleHealth:
            self.health = self.totalPossibleHealth
        raw_input("After healing, " + self.label + " changed the hp value to " + str(self.health) + "hp. Press enter to continue... ")

    def flee(self, opposingClass):
        self.health -= (0.9) * self.totalPossibleHealth
        if self.health <= 0:
            self.health = 1
        opposingClass.health = -1

    def blind(self, opposingClass):
        if opposingClass.damage > 0:
            self.temp = opposingClass.damage
        opposingClass.damage = 0
        raw_input("The blind temporarily changed damage rating to 0 for " + opposingClass.label + ". Press enter to continue... ")

    def taunt(self, opposingClass):
        if len(opposingClass.spells) > 0:
            if opposingClass.spells[3] == "Heal":
                opposingClass.spells.pop(3)
        opposingClass.damage = opposingClass.damage * 3
        raw_input("The option to heal was removed from " + opposingClass.label + " at the cost of greatly increasing damage rating. Press enter to continue... ")

    def buff(self):
        self.armor = 1.1 * self.armor
        self.damage = 1.1 * self.damage
        raw_input("For the remainder of the battle, you slightly improved armor and damage rating. Press enter to continue... ")

    def Poison(self, opposingClass):
        opposingClass.poison += 1
        raw_input("A stack of poison was added to " + opposingClass.label + ". Press enter to continue... ")

    def bully(self, opposingClass):
        if self.poison >= 1:
            self.poison -= 1
        self.damage = int(0.75 * self.damage)
        self.attack(opposingClass)
        self.damage = int((4.0 / 3) * self.damage)
        if self.race == "Human":
            opposingClass.damage = opposingClass.damage * 0.95
            opposingClass.armor = opposingClass.armor * 0.95
            raw_input("For a turn of reduced damage, a stack of poison was removed from " + self.label + " while also reducing the armor and damage rating of " + opposingClass.label + ". Press enter to continue... ")
        else:
            raw_input("For a turn of reduced damage, a stack of poison was removed from " + self.label + ". Press enter to continue... ")

    def hammer(self, opposingClass):
        self.attack(opposingClass)
        if random.randint(1, 10) == 1:
            self.flee(opposingClass)
            self.health = self.totalPossibleHealth
            raw_input("At the cost of losing all exp for this battle, the battle was fled, and you have been healed to full. Press enter to continue... ")
        elif self.race == "Dwarf":
            self.extraxp += 2
            raw_input("You have successfully increased the amount of exp you will get at the end of this battle. Press enter to continue... ")
        else:
            raw_input("A normal attack was performed at the risk of causing an automatic flee, but also automatic full health. Press enter to continue... ")

    def sing(self, opposingClass):
        opposingClass.turnsToDie = random.randint(10, 35)
        if self.armor > 0:
            self.temp2 = self.armor
        if self.race == "Elf":
            self.armor = 0.25 * self.armor
            raw_input("You guaranteed the death of your opponent, but you also drastically reduced your armor. Can you outlive your opponent? Press enter to continue... ")
        else:
            self.armor = 0
            raw_input("You never thought singing lessons were important, but you wish you had taken some, as you have now lost all of your armor in exchange for the guaranteed death of your opponent in a random amount of turns. Can you outlive them? Press enter to continue... ")

    def firebreath(self, opposingClass):
        if self.race == "Dragon":
            opposingClass.takeDamage(self.damage + opposingClass.armor, "The Dragon who Was, and Who Shall Try to Be")
            raw_input("You attacked your opponent while ignoring race biases and also ignoring armor. Press enter to continue... ")
        else:
            opposingClass.takeDamage(self.damage, "The Un-Cool Not-Dragon :(")
            raw_input("You attacked your opponent while ignoring race biases. Press enter to continue... ")

    def flight(self):
        if self.race == "Bird":
            self.health = 0.66 * self.health
            raw_input(self.label + " changed their health so it has been reduced to 2/3rds of its value, but all for temporary invulnerability. Worth it? Press enter to continue... ")
        else:
            self.health = 0.5 * self.health
            raw_input(self.label + " changed their health so it has been reduced to 1/2 of its value, but all for temporary invulnerability. Worth it? Press enter to continue... ")
        self.invuln = 2

    def killPlayer(self, playerObject):
        if self.inBattle == 1:
            self.spells = []
            self.level = math.floor(math.sqrt(50 * self.experience))
            if self.level >= 0:
                self.spells.append("Attack")
                self.spells.append("Miscellany")
                self.spells.append("Defend")
                self.spells.append("Heal")
                self.spells.append("Flee")
            if self.level >= 10:
                self.spells.append("Blind")
            if self.level >= 25:
                self.spells.append("Taunt")
            if self.level >= 50:
                self.spells.append("Buff")
            if self.level >= 100:
                self.spells.append("Poison")
            if self.level >= 175:
                self.spells.append("Bully")
                self.spells.append("Hammer")
                self.spells.append("Sing")
                self.spells.append("Firebreath")
                self.spells.append("Flight")
        if self.health < 0.5 * self.totalPossibleHealth:
            self.choice = random.randint(1, 5)
            if self.choice == 1:
                self.heal()
            elif self.choice == 2:
                self.defend()
            elif self.choice == 3 and "Blind" in self.spells:
                self.blind(playerObject)
            elif self.choice == 4 and "Flight" in self.spells:
                self.flight()
            else:
                if "Firebreath" in self.spells and (playerObject.race == self.good1 or playerObject.race == self.good2):
                    self.firebreath(playerObject)
                else:
                    self.attack(playerObject)
        elif playerObject.health > 0.5 * playerObject.totalPossibleHealth:
            self.choice = random.randint(6, 8)
            if self.choice == 6:
                if "Firebreath" in self.spells and (playerObject.race == self.good1 or playerObject.race == self.good2):
                    self.firebreath(playerObject)
                else:
                    self.attack(playerObject)
            elif self.choice == 7 and "Poison" in self.spells:
                self.Poison(playerObject)
            elif self.choice == 8 and "Taunt" in self.spells and self.health >= 0.5 * self.totalPossibleHealth:
                self.taunt(playerObject)
            else:
                if "Firebreath" in self.spells and (playerObject.race == self.good1 or playerObject.race == self.good2):
                    self.firebreath(playerObject)
                else:
                    self.attack(playerObject)
        else:
            if "Firebreath" in self.spells and (playerObject.race == self.good1 or playerObject.race == self.good2):
                self.firebreath(playerObject)
            else:
                self.attack(playerObject)
        return self.choice

    def castSpell(self, opposingClass):
        if self.inBattle == 1:
            self.spells = []
            self.level = math.floor(math.sqrt(50 * self.experience))
            if self.level >= 0:
                self.spells.append("Attack")
                self.spells.append("Miscellany")
                self.spells.append("Defend")
                self.spells.append("Heal")
                self.spells.append("Flee")
            if self.level >= 10:
                self.spells.append("Blind")
            if self.level >= 25:
                self.spells.append("Taunt")
            if self.level >= 50:
                self.spells.append("Buff")
            if self.level >= 100:
                self.spells.append("Poison")
            if self.level >= 175:
                self.spells.append("Bully")
                self.spells.append("Hammer")
                self.spells.append("Sing")
                self.spells.append("Firebreath")
                self.spells.append("Flight")
        self.choice = raw_input("\nYou can cast any of the following spells: " + repr(self.spells) + ". You decide to choose the obvious choice of ")
        while not self.choice in self.spells:
            self.choice = raw_input("You remember your days as the class clown, but then realize that you need to find her and are in a battle and need to cast a spell. You can cast any of the following spells: " + repr(self.spells) + ". You know the obvious spell to cast is ")
        if self.choice == "Attack":
            self.attack(opposingClass)
        elif self.choice == "Miscellany":
            self.miscellany(opposingClass)
        elif self.choice == "Defend":
            self.defend()
        elif self.choice == "Heal":
            self.heal()
        elif self.choice == "Flee":
            self.flee(opposingClass)
        elif self.choice == "Blind":
            self.blind(opposingClass)
        elif self.choice == "Taunt":
            self.taunt(opposingClass)
        elif self.choice == "Buff":
            self.buff()
        elif self.choice == "Poison":
            self.Poison(opposingClass)
        elif self.choice == "Bully":
            self.bully(opposingClass)
        elif self.choice == "Hammer":
            self.hammer(opposingClass)
        elif self.choice == "Sing":
            self.sing(opposingClass)
        elif self.choice == "Firebreath":
            self.firebreath(opposingClass)
        elif self.choice == "Flight":
            self.flight()
        else:
            self.attack(opposingClass)
        return self.choice

def battle(playerObject, enemyObject):
    enemyObject.spells = [0, 0, 0, "Heal"]
    playerObject.inBattle = 0
    enemyObject.inBattle = 0
    armorBeforeBattle = playerObject.armor
    dmgBeforeBattle = playerObject.damage
    playerObject.poison = 0
    enemyObject.poison = 0
    levelBeforeBattle = math.floor(math.sqrt(50 * playerObject.experience))
    while playerObject.health > 0 and enemyObject.health > 0:
        playerObject.inBattle += 1
        enemyObject.inBattle += 1
        if playerObject.invuln > 0:
            playerObject.invuln -= 1
        if enemyObject.invuln > 0:
            enemyObject.invuln -= 1
        if playerObject.poison >= 1:
            playerObject.takeDamage(enemyObject.health * (0.15) * math.sqrt(enemyObject.poison) + enemyObject.armor, "Poison")
        if enemyObject.poison >= 1:
            enemyObject.takeDamage(playerObject.health * (0.15) * math.sqrt(playerObject.poison) + playerObject.armor, "Poison")
        enemyObject.turnsToDie -= 1
        if enemyObject.turnsToDie == 0:
            enemyObject.takeDamage(999999999999999, enemyObject.good1)

        playerObject.castSpell(enemyObject)

        if enemyObject.choice == 2:
            enemyObject.armor = (1.0/3) * enemyObject.armor
        if enemyObject.choice == 3:
            playerObject.damage = enemyObject.temp

        if enemyObject.health > 0:
            enemyObject.killPlayer(playerObject)

        if playerObject.choice == "Defend":
            playerObject.armor = (1.0/3) * playerObject.armor
        if playerObject.choice == "Blind":
            enemyObject.damage = playerObject.temp

    playerObject.armor = armorBeforeBattle
    playerObject.damage = dmgBeforeBattle
    if enemyObject.killed == True:
        playerObject.experience += random.randint(3, 7) * playerObject.extraxp
        playerObject.extraxp = 1
        raw_input("Congratulations, the enemy was vanquished! Press enter to continue... ")
        levelAfterBattle = math.floor(math.sqrt(50 * playerObject.experience))
        for i in range(int(levelBeforeBattle), int(levelAfterBattle), 1):
            print "\nLevel Up!!"
            playerObject.totalPossibleHealth += random.randint(5, 10)
            playerObject.damage += random.randint(3, 15)
            playerObject.armor += random.randint(3, 15)
    elif enemyObject.health <= 0:
        raw_input("The battle was fled by a really cowardly idiot. Press enter to continue... ")
        playerObject.extraxp = 1
    elif playerObject.health <= 0:
        raw_input("You have died. You realize you can't catch her, and you die screaming. Press enter to continue... ")
        sys.exit()

def randName(amtSyllables):
    vowels = ["a", "e", "i", "o", "u", "y"]
    consonants = ["b", "c", "d", "f", "g", "h", "i", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "z"]
    finalString = ""
    for i in range(0, amtSyllables, 1):
        for j in range(0, random.randint(2, 4), 1):
            finalString += vowels[random.randint(0, 5)]
        for j in range(0, random.randint(1, 2), 1):
            finalString += consonants[random.randint(0, 20)]
    finalString = finalString[0] + finalString[1:]
    return finalString
    
name = raw_input('You wake up. You are lost. Your memories are jambled, however, you can recall that your name is ')

race = raw_input('\nYou look around. Then you look down at yourself. You can now also recall that your race is that of a(n) ')
while race != "Human" and race != "Dwarf" and race != "Elf" and race != "Dragon" and race != "Bird":
    race = raw_input('\nYou suddenly recall that you are silly, and that the only possibilities of a race you could be are a \'Human\', a \'Dwarf\', an \'Elf\', a \'Dragon\', or a \'Bird\', and that you must be a(n) ').lower()
    if len(race) >= 2:
        race = race[0].upper() + race[1:].lower()

tunnelNo = raw_input('\nYou feel a drop of moisture on your shoulder. You are in a cave. You are surrounded by 3 gated tunnels. You remember why you are here. You MUST get her. You see the first tunnel has strong magic armor, but no weapons. The second tunnel has decent cloth armor and a bow. The third tunnel also has something: a big deadly sword, but no armor. You choose to go down tunnel number ')
while tunnelNo != "1" and tunnelNo != "2" and tunnelNo != "3":
    tunnelNo = raw_input('\nYou realize that ' + str(tunnelNo) + ' wasn\'t a valid tunnel option to go through. The first tunnel offers a strong defense, the second tunnel offers mixed defensive and offensive capabilities, and the last tunnel offers a strong offense. You choose to go down the tunnel number ')
tunnelNo = int(tunnelNo)

totalHealth = 150
armor = random.randint(30, 45)
damage = random.randint(30, 45)

if race == "Human":
    race = Human
elif race == "Dwarf":
    race = Dwarf
elif race == "Elf":
    race = Elf
elif race == "Dragon":
    race = Dragon
elif race == "Bird":
    race = Bird

if tunnelNo == 1:
    armor += random.randint(10, 20)
elif tunnelNo == 2:
    armor += random.randint(5, 10)
    damage += random.randint(5, 10)
elif tunnelNo == 3:
    damage += random.randint(10, 20)

Player = Character(name, totalHealth, armor, damage, race, "you", 0)

raw_input("\n\n\nYou, " + name + ", have chosen to go into tunnel " + str(tunnelNo) + "! You have 150hp, " + str(armor) + " armor, " + str(damage) + " damage, and are of the race " + str(race.Class) + "!\nPress enter to continue... ")

raw_input('\n\n\nYou encounter \'Saurabh Totey\', a friendly human who is suffering within the caves. However, he seems to carry vital information to where she is! You decide to attack the poor helpless human (this is a tutorial battle) >:)\nPress enter to continue... ')
SaurabhTotey = Character("Saurabh Totey", 500, 15, 10, Human, "the friendliest human", 100)
battle(Player, SaurabhTotey)

'''
P : Player
E : Enemy
O : Portal to Village (not yet implemented)
S : Shard (not yet implemented)
'''
lineA = list("||||||||||| |||||||||||")
lineB = list("|||||||||||||||||||||||")
lineC = list("|||||||||||||||||||||||")
lineD = list("|||||||||||||||||||||||")
lineE = list("|||||||||||||||||||||||")
lineF = list("||||||||||| |||||||||||")
lineG = list(" ||||||||| P ||||||||| ")
lineH = list("||||||||||| |||||||||||")
lineI = list("|||||||||||||||||||||||")
lineJ = list("|||||||||||||||||||||||")
lineK = list("|||||||||||||||||||||||")
lineL = list("|||||||||||||||||||||||")
lineM = list("||||||||||| |||||||||||")
for i in range(1, 22, 1):
    if lineM[i - 1] != " ":
        cutWall = random.randint(1, 2)
        if cutWall == 1:
            lineM[i] = " "
lines = [lineM, lineL, lineK, lineJ, lineI, lineH, lineG, lineF, lineE, lineD, lineC, lineB, lineA]
#        0      1      2      3      4      5      6      7      8      9      10     11     12
for j in range(1, len(lines), 1):
    for i in range(1, 21, 1):
        if (lines[j - 1])[i] == " " and not ((lines[j - 1])[i-1] == " " and (lines[j - 1])[i + 1] == " "):
            (lines[j])[i] = " "
            if not (lines[j - 1])[i - 1] == " ":
                left = random.randint(1, 2)
            else:
                left = 0
            if not (lines[j - 1])[i + 1] == " ":
                right = random.randint(1, 2)
            else:
                right = 0
            if right == 1:
                (lines[j])[i + 1] = " "
            elif left == 1:
                (lines[j])[i - 1] = " "
for j in range(0, len(lines), 1):
    for i in range(0, len(lines[j]), 1):
        if (lines[j])[i] == " " and random.randint(1, 20) == 1:
            (lines[j])[i] = "E"
        elif (lines[j])[i] == " " and random.randint(1, 750) == 1:
            (lines[j])[i] = "O"
        elif (lines[j])[i] == " " and random.randint(1, 10000) == 1:
            (lines[j])[i] = "S"
while True:
    steppedOn = " "
    (lines[6])[11] = "P"
    clear()
    finalString = ""
    for line in lines:
        for string in line:
            finalString += string
        finalString += "\n"

    print finalString
    
    desiredDirection = ""
    while desiredDirection != "w" and desiredDirection != "a" and desiredDirection != "s" and desiredDirection != "d":
        desiredDirection = raw_input("You notice the evershifting maze surrounding you, and decide to move in [with 'WASD'] direction ")
        if len(desiredDirection) >= 1:
            desiredDirection = desiredDirection[0].lower()
    if desiredDirection == "w":
        if (lines[5])[11] != "|":
            steppedOn = (lines[5])[11]
            for i in range(0, 12, 1):
                lines[12 - i] = lines[11 - i]
            lines[0] = list("|||||||||||||||||||||||")
            for i in range(1, len(lines[0]) - 1, 1):
                if (lines[1])[i] != "|" and not ((lines[1])[i-1] != "|" and (lines[1])[i+1] != "|"):
                    if random.randint(1, 20) == 1:
                        (lines[0])[i] = "E"
                    elif random.randint(1, 750) == 1:
                        (lines[0])[i] = "O"
                    elif random.randint(1, 10000) == 1:
                        (lines[0])[i] = "S"
                    else:
                        (lines[0])[i] = " "
                    if (lines[1])[i - 1] == "|":
                        left = random.randint(1, 2)
                    else:
                        left = 0
                    if (lines[1])[i + 1] == "|":
                        right = random.randint(1, 2)
                    else:
                        right = 0
                    if right == 1:
                        if random.randint(1, 20) == 1:
                            (lines[0])[i + 1] = "E"
                        elif random.randint(1, 750) == 1:
                            (lines[0])[i + 1] = "O"
                        elif random.randint(1, 10000) == 1:
                            (lines[0])[i + 1] = "S"
                        else:
                            (lines[0])[i + 1] = " "
                    elif left == 1:
                        if random.randint(1, 20) == 1:
                            (lines[0])[i - 1] = "E"
                        elif random.randint(1, 750) == 1:
                            (lines[0])[i - 1] = "O"
                        elif random.randint(1, 10000) == 1:
                            (lines[0])[i - 1] = "S"
                        else:
                            (lines[0])[i - 1] = " "
            (lines[7])[11] = " "
        else:
            raw_input("Oops, that direction was invalid. You bonk your head and lose 1hp. Press enter to continue... ")
            Player.health -= 1
    if desiredDirection == "a":
        if (lines[6])[10] != "|":
            steppedOn = (lines[6])[10]
            for j in range(0, 13, 1):
                for i in range(0, 22, 1):
                    (lines[j])[22 - i] = (lines[j])[21 - i]
            for i in range(0, 13, 1):
                (lines[i])[0] = "|"
            for i in range(1, 11, 1):
                if (lines[i])[1] != "|" and not ((lines[i - 1])[1] != "|" and (lines[i + 1])[1] != "|"):
                    if random.randint(1, 20) == 1:
                        (lines[i])[0] == "E"
                    elif random.randint(1, 750) == 1:
                        (lines[i])[0] == "O"
                    elif random.randint(1, 10000) == 1:
                        (lines[i])[0] == "S"
                    else:
                        (lines[i])[0] == " "
                    if (lines[i - 1])[1] == "|":
                        up = random.randint(1, 2)
                    else:
                        up = 0
                    if (lines[i + 1])[1] == "|":
                        down = random.randint(1, 2)
                    else:
                        down = 0
                    if down == 1:
                        if random.randint(1, 20) == 1:
                            (lines[i - 1])[0] = "E"
                        elif random.randint(1, 750) == 1:
                            (lines[i - 1])[0] = "O"
                        elif random.randint(1, 10000) == 1:
                            (lines[i - 1])[0] = "S"
                        else:
                            (lines[i - 1])[0] = " "
                    elif up == 1:
                        if random.randint(1, 20) == 1:
                            (lines[i + 1])[0] = "E"
                        elif random.randint(1, 750) == 1:
                            (lines[i + 1])[0] = "O"
                        elif random.randint(1, 10000) == 1:
                            (lines[i + 1])[0] = "S"
                        else:
                            (lines[i + 1])[0] = " "
            (lines[6])[12] = " "
        else:
            raw_input("Oops, that direction was invalid. You bonk your head and lose 1hp. Press enter to continue... ")
            Player.health -= 1
    if desiredDirection == "s":
        if (lines[7][11]) != "|":
            steppedOn = (lines[7])[11]
            for i in range(0, 12, 1):
                lines[i] = lines[i + 1]
            lines[12] = list("|||||||||||||||||||||||")
            for i in range(1, len(lines[12]) - 1, 1):
                if (lines[11])[i] != "|" and not ((lines[11])[i - 1] != "|" and (lines[11])[i + 1] != "|"):
                    if random.randint(1, 20) == 1:
                        (lines[12])[i] = "E"
                    elif random.randint(1, 750) == 1:
                        (lines[12])[i] = "O"
                    elif random.randint(1, 10000) == 1:
                        (lines[12])[i] = "S"
                    else:
                        (lines[12])[i] = " "
                    if (lines[11])[i - 1] == "|":
                        left = random.randint(1, 2)
                    else:
                        left = 0
                    if (lines[11])[i + 1] == "|":
                        right = random.randint(1, 2)
                    else:
                        right = 0
                    if right == 1:
                        if random.randint(1, 20) == 1:
                            (lines[12])[i + 1] = "E"
                        elif random.randint(1, 750) == 1:
                            (lines[12])[i + 1] = "O"
                        elif random.randint(1, 10000) == 1:
                            (lines[12])[i + 1] = "S"
                        else:
                            (lines[12])[i + 1] = " "
                    elif left == 1:
                        if random.randint(1, 20) == 1:
                            (lines[12])[i - 1] = "E"
                        elif random.randint(1, 750) == 1:
                            (lines[12])[i - 1] = "O"
                        elif random.randint(1, 10000) == 1:
                            (lines[12])[i - 1] = "S"
                        else:
                            (lines[12])[i - 1] = " "
            (lines[5])[11] = " "
        else:
            raw_input("Oops, that direction was invalid. You bonk your head and lose 1hp. Press enter to continue... ")
            Player.health -= 1
    if desiredDirection == "d":
        if (lines[6])[12] != "|":
            steppedOn = (lines[6])[12]
            for j in range(0, 13, 1):
                for i in range(0, 22, 1):
                    (lines[j])[i] = (lines[j])[i + 1]
            for i in range(0, 13, 1):
                (lines[i])[22] = "|"
            for i in range(1, 11, 1):
                if (lines[i])[21] != "|" and not ((lines[i - 1])[21] != "|" and (lines[i + 1])[21] != "|"):
                    if random.randint(1, 20) == 1:
                        (lines[i])[22] = "E"
                    elif random.randint(1, 750) == 1:
                        (lines[i])[22] = "O"
                    elif random.randint(1, 10000) == 1:
                        (lines[i])[22] = "S"
                    else:
                        (lines[i])[22] = " "
                    if (lines[i - 1])[21] == "|":
                        up = random.randint(1, 2)
                    else:
                        up = 0
                    if (lines[i + 1])[21] == "|":
                        down = random.randint(1, 2)
                    else:
                        down = 0
                    if down == 1:
                        if random.randint(1, 20) == 1:
                            (lines[i + 1])[22] = "E"
                        elif random.randint(1, 750) == 1:
                            (lines[i + 1])[22] = "O"
                        elif random.randint(1, 10000) == 1:
                            (lines[i + 1])[22] = "S"
                        else:
                            (lines[i + 1])[22] = " "
                    elif up == 1:
                        if random.randint(1, 20) == 1:
                            (lines[i - 1])[22] = "E"
                        elif random.randint(1, 750) == 1:
                            (lines[i - 1])[22] = "O"
                        elif random.randint(1, 10000) == 1:
                            (lines[i - 1])[22] = "S"
                        else:
                            (lines[i - 1])[22] = " "
            (lines[6])[10] = " "
        else:
            raw_input("Oops, that direction was invalid. You bonk your head and lose 1hp. Press enter to continue... ")
            Player.health -= 1
    if steppedOn == "E":
        raw_input("You encountered an enemy. He appears to be hostile. Press enter to continue... ")
        battle(Player, Character(randName(random.randint(1, 3)), random.randint(50, 80 + 2 * Player.getLevel()), random.randint(30, 100 + 2 * Player.getLevel()), random.randint(30, 100 + Player.getLevel()), random.choice([Human, Dwarf, Elf, Dragon, Bird]) ,"the enemy", 25))
        
