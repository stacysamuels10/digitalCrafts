import OptionsScripts
whatNext = ""
backpackChoice = 0
menuChoice = 0

def puzzle1 ():
    listOfMenuOptions = ["1. Look around the room", "2. Open my backpack", "3. Try the door", "4. Quit the game"]
    print("\n")
    for items in listOfMenuOptions:
        print(items)
    success = False
    whatNext = input("\nWhat do you want to do next? Type the number to select an option\n")
    if whatNext.isnumeric() == False:
        print("\nPlease choose a number\n")
    menuChoice = OptionsScripts.menuOptions(whatNext)
    #if menuChoice == 1:
        #something here
    if menuChoice == 2:
        OptionsScripts.backpack()
    #if menuChoice == 3:
        #something here
    

puzzle1()

# def puzzle2 ():
#     listOfMenuOptions = ["1. Look around the room", "2. Open my backpack", "3. Try the door", "4. Quit the game"]
#     whatNext = ""
#     menuChoice = 0
#     print("\n")
#     for items in listOfMenuOptions:
#         print(items)
#     success = False
#     whatNext = input("\nWhat do you want to do next? Type the number to select an option\n")
#     if whatNext.isnumeric() == False:
#         print("\nPlease choose a number\n")
#     menuChoice = OptionsScripts.menuOptions(whatNext)
#     if menuChoice == 1:
#         #something here
#     if menuChoice == 2:
#         #open backpack function
#     if menuChoice == 3:
#         #something here

# def puzzle3 ():
#     listOfMenuOptions = ["1. Look around the room", "2. Open my backpack", "3. Try the door", "4. Quit the game"]
#     whatNext = ""
#     menuChoice = 0
#     print("\n")
#     for items in listOfMenuOptions:
#         print(items)
#     success = False
#     whatNext = input("\nWhat do you want to do next? Type the number to select an option\n")
#     if whatNext.isnumeric() == False:
#         print("\nPlease choose a number\n")
#     menuChoice = OptionsScripts.menuOptions(whatNext)
#     if menuChoice == 1:
#         #something here
#     if menuChoice == 2:
#         #open backpack function
#     if menuChoice == 3:
#         #something here

# def puzzle4 ():
#     listOfMenuOptions = ["1. Look around the room", "2. Open my backpack", "3. Try the door", "4. Quit the game"]
#     whatNext = ""
#     menuChoice = 0
#     print("\n")
#     for items in listOfMenuOptions:
#         print(items)
#     success = False
#     whatNext = input("\nWhat do you want to do next? Type the number to select an option\n")
#     if whatNext.isnumeric() == False:
#         print("\nPlease choose a number\n")
#     menuChoice = OptionsScripts.menuOptions(whatNext)
#     if menuChoice == 1:
#         #something here
#     if menuChoice == 2:
#         #open backpack function
#     if menuChoice == 3:
#         #something here

class EscapeRoom:
    def __init__(self, name, spellStrength, puzzleCounter):
        self.name = name
        self.spellStrength = spellStrength
        self.puzzleCounter = puzzleCounter 