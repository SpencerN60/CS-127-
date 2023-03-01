import random

def initialChoice():
    choice = input("Choice? [p]lay, [i]nstructions, [q]uit: ")
    while choice != "p" and choice != "i" and choice != "q":
        print("ERROR: Please enter 'p', 'i', or 'q'...")
        choice = input("Choice? [p]lay, [i]nstructions, [q]uit: ")
    return choice

def chooseNumPlayers():
    numPlayers = input("Choose number of players: 1 or 2 ->")
    while numPlayers != "1" and numPlayers != "2":
        numPlayers = input("Choose number of players: 1 or 2 ->")
    
    #       If the user chooses '1,' then they play against the computer
    #       If the user chooses '2,' then they play agianst another human
    return numPlayers

def wait():
    input("Press [Enter] To Continue...")
    print()

def printBanner():
    print("#######################################################################")
    print()
    print("~~ Starting New Round ~~")
    print()

def printPoints(playerNum, points):
    print("* Player {0} has {1} Points!".format(playerNum, points))
    print()

def wagerPointsHuman(playerNum, points):
    wager = int(input("How many points would you like to wager: "))
    print()
    while wager not in range(1, points + 1):
        wager = int(input("Choose number within the range from 1 to {} ".format(points)))
        print()
    print("Player {}  (HUMAN) decides to wager {} points".format(playerNum, wager))
    print()
    return wager

def wagerPointsAI(playerNum, points):
    wager = random.randint(1,points)
    print("Player {} (AI) decides to wager {} points".format(playerNum, wager))
    print()
    # TODO: Generate a random integer from 1 to (points + 1), non-inclusive, which will be the number of points for the computer to wager
    # NOTE: Try to have the AI version match the look of the output of the human version above 
    return wager

def generateTargetValue(numSpinners, spinnerLow, spinnerHigh): # finished
    target = 0
    numberSpinners = random.randrange(1,numSpinners + 1)
    for i in range(0,numberSpinners):
        target += random.randrange(spinnerLow, spinnerHigh + 1)
    return target

def getSpinnerChoiceHuman(playerNum, target, numSpinners, spinnerLow, spinnerHigh):
    print("Player {}, each spinner can spin a number between {} and {}".format(playerNum, spinnerLow, spinnerHigh))
    spinnerChoice = int(input("To get to a target number of {}, how many spinners would you like to spin (1-{}): ".format(target,numSpinners)))
    while spinnerChoice not in range(1,numSpinners + 1):
        spinnerChoice = int(input("Player {}, input a number between 1 and {}: ".format(playerNum,numSpinners)))
    # TODO: Use the 'do-while' pattern to take in input from the user for how many spinners they would like to spin
    # Ex: if numSpinners is 3, then the user can pick between 1-3
    # NOTE: Use the spinnerLow and spinnerHigh values to output data about what the player could spin
    return spinnerChoice

def getSpinnerChoiceAI(playerNum, target, numSpinners, spinnerLow, spinnerHigh):
    print("Player {}, each spinner can spin a number between {} and {}".format(playerNum, spinnerLow, spinnerHigh))
    print("To get to a target number of {}, how many spinners would you like to spin (1-{}): ".format(target,numSpinners))
    spinnerChoice = random.randrange(1, numSpinners + 1)
    return spinnerChoice

def spinSpinners(playerNum, spinnerChoice, target, spinnerLow, spinnerHigh):
    print("Player {} spins: ".format(playerNum))
    spinTotal = 0
    for i in range(1, spinnerChoice + 1):
        addition = random.randrange(spinnerLow, spinnerHigh + 1)
        print("Player {} has spun a {}".format(playerNum, addition))
        spinTotal += addition
    return spinTotal

def resetGameOptions():
    player1Points = 10
    player2Points = 10
    return player1Points, player2Points

def main():
    # main script running control variable
    running = True
    
    # gameplay variables
    SPINNER_LOW = 1
    SPINNER_HIGH = 3
    NUM_SPINNERS = 3
    player1Points = 10
    player2Points = 10

    # Print title material here
    while running:
        choice = initialChoice() # Asks for input to play, instructions, or quit
        if choice == "p":
            numPlayers = chooseNumPlayers()

            # main game loop
            while player1Points != 0 and player2Points != 0:
                printBanner()
                print("Player 1 has {} points".format(player1Points))
                print("Player 2 has {} points".format(player2Points))
                print()
                # get a target value
                targetValue = generateTargetValue(NUM_SPINNERS, SPINNER_LOW, SPINNER_HIGH)
                print("Your target value is: {}".format(targetValue))
                dummy = input("Press any button to continue: ")

                # Play against AI
                if numPlayers == "1":
                    # Human wager
                    printPoints(1,player1Points)
                    humanWager = wagerPointsHuman(1,player1Points)
                    # AI wager
                    printPoints(2,player2Points)
                    aiWager = wagerPointsAI(2,player2Points)
                    # Print stuff for user
                    wait()
                    print()
                    print("The target value is {}".format(targetValue))
                    print()
                    # Player 1 choose number of spinners
                    numSpinners1 = getSpinnerChoiceHuman(1,targetValue,NUM_SPINNERS,SPINNER_LOW,SPINNER_HIGH)
                    # Spin for player 1
                    player1Spin = spinSpinners(1,numSpinners1,targetValue,SPINNER_LOW,SPINNER_HIGH)
                    playerOneDiff = abs(player1Spin - targetValue)
                    print("The total value of the spinners was: {}, and the target value was: {}".format(player1Spin,targetValue))
                    print()
                    wait()
                    print()
                    print("The target value is {}".format(targetValue))
                    print()
                    # Player AI choose number of spinners
                    numSpinners2 = getSpinnerChoiceAI(2, targetValue, NUM_SPINNERS, SPINNER_LOW, SPINNER_HIGH)
                    # Spin for player 2
                    player2Spin = spinSpinners(2, numSpinners2, targetValue, SPINNER_LOW, SPINNER_HIGH)
                    playerTwoDiff = abs(player2Spin - targetValue)
                    print("The total value of the spinners was: {}, and the target value was: {}".format(player2Spin,targetValue))
                    print()
                    wait()
                    if playerOneDiff > playerTwoDiff:
                        print("Player 2 won!")
                        player1Points -= humanWager
                        player2Points += aiWager
                    elif playerOneDiff < playerTwoDiff:
                        print("Player 1 won!")
                        player1Points += humanWager
                        player2Points -= aiWager
                    else:
                        print("Draw")
                    print()
                    print("--End of Round--")

                elif numPlayers == "2":
                    # Human wager
                    printPoints(1,player1Points)
                    p1wager = wagerPointsHuman(1,player1Points)
                    # AI wager
                    printPoints(2,player2Points)
                    p2wager = wagerPointsHuman(2,player2Points)
                    # Print stuff for user
                    wait()
                    print()
                    print("The target value is {}".format(targetValue))
                    print()
                    # Player 1 choose number of spinners
                    numSpinners1 = getSpinnerChoiceHuman(1,targetValue,NUM_SPINNERS,SPINNER_LOW,SPINNER_HIGH)
                    # Spin for player 1
                    player1Spin = spinSpinners(1,numSpinners1,targetValue,SPINNER_LOW,SPINNER_HIGH)
                    playerOneDiff = abs(player1Spin - targetValue)
                    print("The total value of the spinners was: {}, and the target value was: {}".format(player1Spin,targetValue))
                    print()
                    wait()
                    print()
                    print("The target value is {}".format(targetValue))
                    print()
                    # Player AI choose number of spinners
                    numSpinners2 = getSpinnerChoiceHuman(2, targetValue, NUM_SPINNERS, SPINNER_LOW, SPINNER_HIGH)
                    # Spin for player 2
                    player2Spin = spinSpinners(2, numSpinners2, targetValue, SPINNER_LOW, SPINNER_HIGH)
                    playerTwoDiff = abs(player2Spin - targetValue)
                    print("The total value of the spinners was: {}, and the target value was: {}".format(player2Spin,targetValue))
                    print()
                    print("Press any button to continue")
                    if playerOneDiff > playerTwoDiff:
                        print("Player 2 won!")
                        player1Points -= p1wager
                        player2Points += p2wager
                    elif playerOneDiff < playerTwoDiff:
                        print("Player 1 won!")
                        player1Points += p1wager
                        player2Points -= p2wager
                    else:
                        print("Draw")
                    print()
                    print("--End of Round--")
            
            if player1Points == 0:
                print("Player 1 wins!")


                        

                     
                    




                    
                    




                    



main()                  





                




