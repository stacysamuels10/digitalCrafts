def menuOptions (whatNext): #test and works    
    menuChoice = 0
    if whatNext == "1":
        menuChoice = 1
        return menuChoice
    if whatNext == "2":
        menuChoice = 2
        return menuChoice
    if whatNext =="3":
        menuChoice = 3
        return menuChoice
    if whatNext == "4":
        print("\nThank you for playing! Bye\n")


def puzzleCounter (): #tested and works, need to append
    puzzle = 0 #at the end of each puzzle
    completedPuzzles = [0,1]
    for puzzle in completedPuzzles:
        puzzle+=1
