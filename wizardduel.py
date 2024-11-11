# Wizard Duel Game
# Author: Austin Boydston
#Description: Two wizards fighting
#The player
class wizard:
    health = 100
    mana = 100

    spells = []

    def __init__(self, health, mana):
        self.health = health
        self.mana = mana

    def getHealth(self):
        return self.health
    
    def setHealth(self, amount):
        self.health = amount
        return 0
    
    def castSpell():
        pass

#The enemy to defeat
class lich:
    health = 300
    mana = 200
    spells = []

    def __init__(self, health, mana):
        self.health = health
        self.mana = mana

    def getHealth(  ):
        return self.health
    
    def setHealth(amount):
        self.health = amount
        return 0


class spell:
    cost = 0
    damage = 0
    damage_over_time = 0
    healamount = 0
    healing_over_time = 0
    cooldown = 0
    name = ""
    type = ""

    def __init__(self, cost, damage, damage_over_time, healamount, healing_over_time, cooldown, name, type):
        self.cost = cost
        self.damage = damage
        self.cooldown = cooldown
        self.name = name

    def effectTarget(self, target):
        target.setHealth(target.getHealth() - self.damage)
        return 0




def getActionInputLetter(letter_list):
    #get input from the user
    userinput = input()
    valid_input_flag = False

    #loop until valid input is given
    while True:
        for i in range(len(letter_list)):
            if userinput == letter_list[i]:
                valid_input_flag = True
        if valid_input_flag:
            break
        else:
            userinput = input()
    return userinput


#Main Game Loop
def MainGameLoop():
    wizard_1 = wizard(50, 20)
    spell_fireball = spell(5, 10, 1, "fireball", )
    spell_ice_spike = spell(5, 10, 1, "ice spike", )

    while True:
        print("Choose what to do")
        print("A: Cast Spell")
        #Print("B: Use Relic")
        print("C: Rest")
        input_letter = getActionInputLetter(["A", "C"])

        if input_letter == "A":
            print("Which Spell?")
            print("A: fireball")
            print("B: ice spike")


MainGameLoop()
#Test damage to player
#spell_fireball.effectTarget(wizard_1)
#print(wizard_1.getHealth())
