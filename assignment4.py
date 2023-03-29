
def printTitleMaterial():
    print("Spencer Ness, Section B2, ")
    print("Four in Sequence!")

def initialChoice():
    choice = input("Choice? [p]lay, [i]nstructions, [q]uit: ")
    while choice != "p" and "i" and "q":
        print("Invalid Choice, please enter either p, i, or q!")
        choice = input("Choice? [p]lay, [i]nstructions, [q]uit: ")
    return choice

def chooseNumPlayers():
    players = int(input("Will you be playing with 1 or 2 players?"))
    while players != 1 and 2:
        print("Invalid number, must choose either 1 or 2 players!")
        players = int(input("Will you be playing with 1 or 2 players?"))
    return players

def printBanner():
    print("#######################################################################")
    print()
    print("~~ Starting New Round ~~")
    print()

def getPlayerPiece(playerNumber):
    piece = ""
    if playerNumber == 0:
        piece = "."
    elif playerNumber == 1:
        piece = "X"
    elif playerNumber == 2:
        piece = "O"
    return piece

def createBoard(width, height):

    empty = getPlayerPiece(0)
    board = []
    for i in range(0, height):
        board.append([])
        for j in range(0, width):
            board[i].append(empty)
    return board

def printBoard(board):
    for row in board:
        for column in row:
            print(column, end="")
        print()
    for i in range(0, len(board[0])):
        print(i, end="")
    print()
    print()

def getColumnInt(board, playerNumber):
    getInt = int(input("Player {0}, select a column number from (0-{1})".format(playerNumber, len(board[0]) - 1)))
    while getInt not in range(0, len(board[0]) - 1):
        print("ERROR: Must select a column in the range fo 0-{}".format(len(board[0]) - 1))
        getInt = int(input("Player {0}, select a column number from (0-{1})".format(playerNumber, len(board[0]) - 1)))
    return getInt



    

