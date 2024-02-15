import sys
import os
import random
import pickle

weapons = {"Greatsword":40, "Bow":30, "Potion":20}


class Player:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 100
        self.health = self.maxhealth
        self.base_attack = 10
        self.gold = 0
        self.pots = 2
        self.weap = ["Rusty Sword"]
        self.currweap = "Rusty Sword"
        self.currpos = "Field"

#enemies
class Goblin:
    def __init__(self,name):
        self.name = name
        self.maxhealth = 50
        self.health = self.maxhealth
        self.attack = 4
        self.goldgain =10
GoblinIG = Goblin("Goblin")

class Zombie:
    def __init__(self,name):
        self.name = name
        self.maxhealth = 70
        self.health = self.maxhealth
        self.attack = 6
        self.goldgain = 14
ZombieIG = Zombie("Zombie")

class Crab:
    def __init__(self,name):
        self.name = name
        self.maxhealth = 20
        self.health = self.maxhealth
        self.attack = 2
        self.goldgain = 2
CrabIG = Crab("Crab")
class Wolf:
    def __init__(self,name):
        self.name = name
        self.maxhealth = 60
        self.health = self.maxhealth
        self.attack = 10
        self.goldgain = 20
WolfIG = Wolf("Wolf")
class Vampire:
    def __init__(self,name):
        self.name = name
        self.maxhealth = 110
        self.health = self.maxhealth
        self.attack = 12
        self.goldgain = 30
VampireIG = Vampire("Vampire")
def main():
    os.system('clear')
    print("Welcome to the Game!\n")
    print("1.) Start")
    print("2.) Load")
    print("3.) Exit")
    option = input("-> ")
    if option == ("1"):
        start()
    elif option == ("2"):
        if os.path.exists("savefile") == True:
            os.system("clear")
            with open("savefile", "rb") as f:
                global PlayerIG
                PlayerIG = pickle.load(f)
            print("Loaded save data")
            option = input("")
            start1()
        else:
            os.system("clear")
            print("You have no save data for this game...")
            option = input("")
            main()
    elif option == ("3"):
        sys.exit()
    else:
        main()
#Asking for name        
def start():
    os.system('clear')
    print ("Hello, what is yout name?")
    option = input("--> ")
    global PlayerIG
    PlayerIG = Player(option)
    start1()
    
#Start    
def start1():
    os.system('clear')
    if PlayerIG.currweap == "Rusty Sword":
        PlayerIG.base_attack = 10
    elif PlayerIG.currweap == "Greatsword":
        PlayerIG.base_attack = 20
    elif PlayerIG.currweap == "Bow":
        PlayerIG.base_attack = 14
    print(f"Name: {PlayerIG.name}")
    print(f"Attack: {PlayerIG.base_attack}")
    print(f"Gold: {PlayerIG.gold}")
    print(f"Current weapons: {PlayerIG.currweap}") 
    print(f"Potions: {PlayerIG.pots}")
    print(f"Health: {PlayerIG.health}/{PlayerIG.maxhealth}")
    print("------------------------")
    print(f"Location: {PlayerIG.currpos}")
    if PlayerIG.currpos == "Field":
        print("It's just a field. Safe from any harm. But theres nothing else here")
    elif PlayerIG.currpos == "Beach":
        print("You're at the beach. Did your mother bring you here as a kid? Probably not. But there are crabs here to fight!")
    elif PlayerIG.currpos == "Mountain":
        print("You're in a mountain pass. Very Rocky. Other than the Goblins here, its relatively uninteresting....")
        print("Wait...GOBLINS?!")
    elif PlayerIG.currpos == "Cave":
        print("You're in a cave. Its pretty dark in here so you think you're alone.")
        print("You think you could settle down here. That moss could make a great bed if there werent a pack of wolves on it.")
        print("If you think you can tame the wolves, go back to Minecraft! They will bite!")
    elif PlayerIG.currpos == "Forest":
        print("You're in the creepy looking forest. Much spooky")
        print("Did you know that there are zombies all around you?")
        print("Like a comical amount of zombies")
    elif PlayerIG.currpos == "Castle":
        print("Here you are! The castle that you might have been looking for! Or...maybe you just found it by dumb luck")
        print("This place gives you huge vampire-final-boss type vibes.")
        print(f"Be Prepared, {PlayerIG.name}")
    print("------------------------")
    print("1.) Travel")
    print("2.) Fight")
    print("3.) Shop")
    print("4.) Inventory")
    print("5.) Save")
    print("6.) Exit\n")
    option = input("-> ")
    if option == ("1") or option.lower() == "travel":
        travel()    
    elif option == ("2") or option.lower() == "attack":
        prefight()
    elif option == ("3") or option.lower() == "shop":
        store()
    elif option == ("4") or option.lower() == "inventory":
        inventory()
    elif option == ("5") or option.lower() == "save":
        os.system("clear")
        with open('savefile', 'wb') as f:
            pickle.dump(PlayerIG, f)
            print("\nGame has been saved")
        option = input()
        start1()
    elif option == ("6") or option.lower() == "exit":
        exit()
    else:
        start1()

def travel():
    os.system("clear")
    print(f"Current Location: {PlayerIG.currpos}")
    if PlayerIG.currpos == "Field":
        print("You are standing in a field. \nTo the north you can see a dense forest where not much light can be seen.\nTo the west you can hear waves splashing against the shore.\nTo the east you see mountains towering above you.\nTheres a river blocking you from going south")
        print("What direction would you like to go?")
        print("North")
        print("South")
        print("East")
        print("West")
        print("1.) Back")
        option = input("")
        if option == "n" or option == "north" or option == "North":
            PlayerIG.currpos = "Forest"
            start1()
        elif option == "w" or option == "west" or option == "West":
            PlayerIG.currpos = "Beach"
            start1()
        elif option == "s" or option == "south" or option == "South":
            print("You are unable to go that way...")
            option = input("")
            travel()
        elif option == "e" or option == "east" or option == "East":
            PlayerIG.currpos = "Mountain"
            start1()
        else:
            os.system("clear")
            print("That isnt a place you can go...")
            option = input("")
            travel()
    elif PlayerIG.currpos == "Beach":
        print("You're on a sandy beach.\nTheres nothing worth going north or south that you can see.\nTo the west is a beautiful sunset and a blanket of ocean.")
        print("What direction would you like to go?")
        print("North")
        print("South")
        print("East")
        print("West")
        print("1.) Back")
        option = input("")
        if option == "n" or option == "north" or option == "North" or option == "w" or option == "west" or option == "West" or option == "s" or option == "south" or option == "South":
            os.system("clear")
            print("You are unable to go that way...")
            option = input("")
            travel()
        elif option == "e" or option == "east" or option == "East":
            PlayerIG.currpos = "Field"
            start1()
        else:
            os.system("clear")
            print("That isnt a place you can go...")
            option = input("")
            travel()
           
    elif PlayerIG.currpos == "Forest":
        print("You're in a dense forest.\nYou can only see a stone brick building to the north.")
        print("What direction would you like to go?")
        print("North")
        print("South")
        print("East")
        print("West")
        print("1.) Back")
        option = input("")
        if option == "e" or option == "east" or option == "East" or option == "w" or option == "west" or option == "West":
            os.system("clear")
            print("You are unable to go that way...")
            option = input("")
            travel()
        elif option == "s" or option == "south" or option == "South":
            PlayerIG.currpos = "Field"
            start1()
        elif option == "n" or option == "north" or option == "North":
            PlayerIG.currpos = "Castle"
            start1()
        else:
            os.system("clear")
            print("That isnt a place you can go...")
            option = input("")
            travel()
            
    elif PlayerIG.currpos == "Mountain":
        print("You're in a jagged mountain pass.\nThere seems to be a cave enterence to the east.\nYou can see the field off to the west.")
        print("What direction would you like to go?")
        print("North")
        print("South")
        print("East")
        print("West")
        print("1.) Back")
        option = input("")
        if option == "n" or option == "north" or option == "North" or option == "s" or option == "south" or option == "South":
            os.system("clear")
            print("You are unable to go that way...")
            option = input("")
            travel()
        elif option == "w" or option == "west" or option == "West":
            PlayerIG.currpos = "Field"
            start1()
        elif option == "e" or option == "east" or option == "East":
            PlayerIG.currpos = "Cave"
            start1()
        else:
            os.system("clear")
            print("That isnt a place you can go...")
            option = input("")
            travel()
        
    elif PlayerIG.currpos == "Cave":
        print("You're in a dimly lit cave.\nYou see light coming from the enterence to the west.")
        print("What direction would you like to go?")
        print("North")
        print("South")
        print("East")
        print("West")
        print("1.) Back")
        option = input("")
        if option == "n" or option == "north" or option == "North" or option == "s" or option == "south" or option == "South" or option == "e" or option == "east" or option == "East":
            os.system("clear")
            print("You are unable to go that way...")
            option = input("")
            travel()
        elif option == "w" or option == "west" or option == "West":
            PlayerIG.currpos = "Mountain"
            start1()
        else:
            os.system("clear")
            print("That isnt a place you can go...")
            option = input("")
            travel()
        
    elif PlayerIG.currpos == "Castle":
        print("You're in an old stone brick castle.\nThe door to the south would lead you out of the castle.")
        print("What direction would you like to go?")
        print("North")
        print("South")
        print("East")
        print("West")
        print("1.) Back")
        option = input("")
        if option == "n" or option == "north" or option == "North" or option == "w" or option == "west" or option == "West" or option == "e" or option == "east" or option == "East":
            os.system("clear")
            print("You are unable to go that way...")
            option = input("")
            travel()
        elif option == "s" or option.lower == "south" or option == "South":
            PlayerIG.currpos = "Forest"
            start1()
        else:
            os.system("clear")
            print("That isnt a place you can go...")
            option = input("")
            travel()

def exit():
    os.system("clear")
    print("Are you sure?")
    print("1.) Yes, Exit")
    print("2.) No, Go Back")
    option = input("-> ")
    if  option == ("1") or option.lower() == "yes":
        os.system("clear")
        print("Thanks for playing!")
        option = input("")
        sys.exit()
    elif option == ("2") or option.lower() == "no":
        start1()
    else:
        exit()
def inventory():
    os.system("clear")
    print("What woulf you like to do?")
    print("1.) Equip Weapon")
    print("2.) Go Back")
    option = input("")
    if option == "1" or option.lower() == "equip":
        equip()
    elif option == "2" or option.lower() == " go back" or option.lower() == "back":
        start1()
    else:
        inventory()
    
def equip():
    os.system("clear")
    print("What would you like to equip?")
    for weapon in PlayerIG.weap:
        print(weapon)
    print("1.) Go Back")
    print("")
    option = input("")
    if option == PlayerIG.currweap:
        os.system("clear")
        print("You already have that weapon equipped")
        option = input("")
        equip()
    elif option == "1":
        inventory()
    elif option in PlayerIG.weap:
        os.system("clear")
        PlayerIG.currweap = option
        print(f"You have equipped {option}")
        option = input("")
        start1()
    else:
        print("That option isn't in your inventory")
        option = input("")
        equip()

def prefight():
    global enemy
    if PlayerIG.currpos == "Field":
        os.system("clear")
        print("There are no enemies to fight")
        option = input("")
        start1()
    elif PlayerIG.currpos == "Beach":
        enemy = CrabIG
    elif PlayerIG.currpos == "Forest":
        enemy = ZombieIG
    elif PlayerIG.currpos == "Mountain":
        enemy = GoblinIG
    elif PlayerIG.currpos == "Cave":
        enemy = WolfIG
    elif PlayerIG.currpos == "Castle":
        enemy = VampireIG
    fight()

def fight():
    os.system("clear")
    if PlayerIG.health > PlayerIG.maxhealth:
        PlayerIG.health == 100
    print(f"{PlayerIG.name}     vs     {enemy.name}")
    print(f"{PlayerIG.name}'s Health: {PlayerIG.health}/{PlayerIG.maxhealth}            {enemy.name}'s Health: {enemy.health}/{enemy.maxhealth}")
    print(f"Potions: {PlayerIG.pots}")
    print("1.) Fight")
    print("2.) Drink Potion")
    print("3.) Run")
    option = input(' ')
    if option == ("1"):
        attack()
    elif option == ("2"):
        drinkpot()
    elif option == ("3"):
        run()
    else:
        fight()

def attack():
    os.system("clear")
    PAttack = random.randint(PlayerIG.base_attack / 2, PlayerIG.base_attack)
    EAttack = random.randint(enemy.attack / 2, enemy.attack)
    if PAttack == PlayerIG.base_attack / 2:
        print("You Miss!")
    else:
        enemy.health -= PAttack
        print(f"The {enemy.name} takes {PAttack} damage!")
    option = input("")
    if enemy.health <= 0:
        win()
    os.system("clear")
    if EAttack == enemy.attack / 2:
        print(f"The {enemy.name} missed their attack!")
    else:
        PlayerIG.health -= EAttack
        print(f"The enemy deals {EAttack} damage!")
    option = input("")
    if PlayerIG.health <= 0:
        dead()
    else:
        fight()
    
def drinkpot():
    if PlayerIG.pots == 0:
        print("You don' have any Potions!")
    else:
        PlayerIG.health += 30
        print("You drank a potion!")
    option = input("")
    fight()
    
def run():
    os.system("clear")
    runnumber = random.randint(1,3)
    if runnumber == 1:
        print(f"You successfully ran away from the {enemy.name}!")
        start1()
    else:
        print("You failed to get away!")
        option = input("")
        os.system("clear")
        EAttack = random.randint(enemy.attack / 2, enemy.attack)
        if EAttack == enemy.attack / 2:
            print(f"The {enemy.name} missed their attack!")
        else:
            PlayerIG.health -+ EAttack
            print(f"The enemy deals {EAttack} damage!")
    option = input("")
    if PlayerIG.health <= 0:
        dead()
    else:
        fight()


def win():
    os.system("clear")
    if enemy.name == "Vampire":
        print(f"Huzza! You have defeated the Vampire!")
        print(f"You've saved this land from...the vampire who was probably minding their own buisness...")
        print(f"Thanks for playing,{PlayerIG.name}!")
        option = input("")
        sys.exit()
    PlayerIG.gold += enemy.goldgain
    print(f"You have defeated the {enemy.name}!")
    print(f"You collect {enemy.goldgain} gold!")
    option = input("")
    start1()

def dead():
    os.system("clear")
    print("You have perished in battle")
    print("You will forever be known as:")
    print(f"{PlayerIG.name}, the person who died fighting a {enemy.name}")
    print("Thank you for playing!")
    

def store():
    os.system("clear")
    print("Welcome to the shop!")
    print(f"You have {PlayerIG.gold} Gold!")
    print("\nWhat would you like to buy?\n(Cap Sensitive)\n")
    print("    Greatsword (40 Gold)")
    print("    Bow (30 Gold)")
    print("    Potion (20 Gold)")
    print("1.) Go Back")
    option = input(" ")
    if option in weapons:
        
        if PlayerIG.gold >=  weapons[option]:
            if option.lower() == "potion":
                PlayerIG.gold -= 20
                PlayerIG.pots += 1
                print(f"You have bought 1 potion!")
                print(f"You have {PlayerIG.pots} Potions!")
                option = input("")
                start1()
            PlayerIG.gold -= weapons[option]
            PlayerIG.weap.append(option)
            os.system("clear")
            print(f"You have bought {option}")
            option = input(" ")
            start1()
        else:
            os.system("clear")
            print("Sorry, you don't have enough gold...")
            option = input(" ")
            store()
    elif option == "1":
        start1()
    else:
        os.system("clear")
        print("That item does not exist(Check Spelling)")
        option = input(" ")
        store()

main()









