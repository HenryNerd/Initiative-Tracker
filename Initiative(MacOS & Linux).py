import os
playercount = 0
active = 1
nothing = 1
Round = 0

print("New Round")
playercount = input("How many players (1-6 (+1 for monster) ) ")

if (int(playercount)) == 1:
    print("")
    playerOne = input("Player 1 Name ")
    
    while (int(active)) == 1:
        os.system('clear')
        Round = Round + 1
        print("Round",Round)
        print()
        nothing = input(playerOne)
elif (int(playercount)) == 2:
    print("")
    playerOne = input("Player 1 Name ")
    print("")
    playerTwo = input("Player 2 Name ")
    
    while (int(active)) == 1:
        os.system('clear')
        Round = Round + 1
        print("Round",Round)
        print()
        nothing = input(playerOne)
        nothing = input(playerTwo)
elif (int(playercount)) == 3:
    print("")
    playerOne = input("Player 1 Name ")
    print("")
    playerTwo = input("Player 2 Name ")
    print("")
    playerThree = input("Player 3 Name ")
    
    while (int(active)) == 1:
        os.system('clear')
        Round = Round + 1
        print("Round",Round)
        print()
        nothing = input(playerOne)
        nothing = input(playerTwo)
        nothing = input(playerThree)
elif (int(playercount)) == 4:
    print("")
    playerOne = input("Player 1 Name ")
    print("")
    playerTwo = input("Player 2 Name ")
    print("")
    playerThree = input("Player 3 Name ")
    print("")
    playerFour = input("Player 4 Name ")
    
    while (int(active)) == 1:
        os.system('clear')
        Round = Round + 1
        print("Round",Round)
        print()
        nothing = input(playerOne)
        nothing = input(playerTwo)
        nothing = input(playerThree)
        nothing = input(playerFour)
elif (int(playercount)) == 5:
    print("")
    playerOne = input("Player 1 Name ")
    print("")
    playerTwo = input("Player 2 Name ")
    print("")
    playerThree = input("Player 3 Name ")
    print("")
    playerFour = input("Player 4 Name ")
    print("")
    playerFive = input("Player 5 Name ")
    
    while (int(active)) == 1:
        os.system('clear')
        Round = Round + 1
        print("Round",Round)
        print()
        nothing = input(playerOne)
        nothing = input(playerTwo)
        nothing = input(playerThree)
        nothing = input(playerFour)
        nothing = input(playerFive)
elif (int(playercount)) == 6:
    print("")
    playerOne = input("Player 1 Name ")
    print("")
    playerTwo = input("Player 2 Name ")
    print("")
    playerThree = input("Player 3 Name ")
    print("")
    playerFour = input("Player 4 Name ")
    print("")
    playerFive = input("Player 5 Name ")
    print("")
    playerSix = input("Player 6 Name ")
    
    while (int(active)) == 1:
        os.system('clear')
        Round = Round + 1
        print("Round",Round)
        print()
        nothing = input(playerOne)
        nothing = input(playerTwo)
        nothing = input(playerThree)
        nothing = input(playerFour)
        nothing = input(playerFive)
        nothing = input(playerSix)
elif (int(playercount)) == 7:
    print("")
    playerOne = input("Player 1 Name ")
    print("")
    playerTwo = input("Player 2 Name ")
    print("")
    playerThree = input("Player 3 Name ")
    print("")
    playerFour = input("Player 4 Name ")
    print("")
    playerFive = input("Player 5 Name ")
    print("")
    playerSix = input("Player 6 Name ")
    print("")
    playerSeven = input("Player 7 Name ")
    
    while (int(active)) == 1:
        os.system('clear')
        Round = Round + 1
        print("Round",Round)
        print()
        nothing = input(playerOne)
        nothing = input(playerTwo)
        nothing = input(playerThree)
        nothing = input(playerFour)
        nothing = input(playerFive)
        nothing = input(playerSix)
        nothing = input(playerSeven)
else:
    print("Invalid Input")
    exit(1)