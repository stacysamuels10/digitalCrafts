import OptionsScripts
import backpackScripts
class EscapeRoom:
    def __init__(self, name, spellStrength, completedPuzzles, incorrectGuesses):
        self.name = name
        self.spellStrength = spellStrength
        self.completedPuzzles = completedPuzzles
        self.incorrectGuesses = incorrectGuesses



def mainMenu ():
    print("""
    1. Look around the room
    2. Open my backpack
    3. Try the door
    4. Quit the game
    """)
    choice = input("Which number do you want?")
    return choice

user = EscapeRoom("", 100, 0, 0)

def gameLoop ():
    # introLetter()
    # introToGame()
    while True:
        choice = mainMenu()
        while user.completedPuzzles == 0:
            if choice == "1":
                outcomePuzzle1 = OptionsScripts.puzzle1(user.completedPuzzles, user.incorrectGuesses)   
                if outcomePuzzle1 == True:
                    user.completedPuzzles +=1
                    break
                else:
                    user.incorrectGuesses+=1
                choice = mainMenu()
                print("story 1 is gonna run yaaaaaay")
                print(user.incorrectGuesses)
                # user.completedPuzzles = [1]
            if choice == "2":
                backpackScripts.backpack1and2()
                choice = mainMenu()
            if choice == "3":
                print(user.spellStrength)
            if choice == "4":
                print("Thank you for playing. Bye!")
                break
        while user.completedPuzzles == 1:
            choice = mainMenu()
            if choice == "1":  
                print("story 2 is gonna run yaaaaaay")
                user.completedPuzzles = [1, 2]
            if choice == "2":
                print("this is where we check the backpack")
            if choice == "3":
                print(user.spellStrength)
            if choice == "4":
                print("Thank you for playing. Bye!")
                break
# WINNER CASE -- modify to number of puzzles you want
        while user.completedPuzzles == 2:
            print("you win!!!!! ")
            break
        break

gameLoop()