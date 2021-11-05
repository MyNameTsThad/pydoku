import random
import time

version = "1.0"
needsTutorial = True

debugOutput = False
advancedDebugOutput = False

gameBoard = [[" ", " ", " ", " ", " ", " ", " ", " ", " "],
             [" ", " ", " ", " ", " ", " ", " ", " ", " "],
             [" ", " ", " ", " ", " ", " ", " ", " ", " "],
             [" ", " ", " ", " ", " ", " ", " ", " ", " "],
             [" ", " ", " ", " ", " ", " ", " ", " ", " "],
             [" ", " ", " ", " ", " ", " ", " ", " ", " "],
             [" ", " ", " ", " ", " ", " ", " ", " ", " "],
             [" ", " ", " ", " ", " ", " ", " ", " ", " "],
             [" ", " ", " ", " ", " ", " ", " ", " ", " "]]

playerTurnsPos = []
playerTurnsCount = 0
playerScore = 0

_currentTime = 0
_responseTime = 0


def mainMenu(callback=False):
    if debugOutput:
        print("mainMenu()")
    # main menu
    if not callback:
        print("\033[34m██████╗ \033[33m██╗   ██╗\033[32m██████╗  ██████╗ ██╗  ██╗██╗   ██╗ \033[0m")
        print("\033[34m██╔══██╗\033[33m╚██╗ ██╔╝\033[32m██╔══██╗██╔═══██╗██║ ██╔╝██║   ██║ \033[0m")
        print("\033[34m██████╔╝ \033[33m╚████╔╝ \033[32m██║  ██║██║   ██║█████╔╝ ██║   ██║ \033[0m")
        print("\033[34m██╔═══╝   \033[33m╚██╔╝  \033[32m██║  ██║██║   ██║██╔═██╗ ██║   ██║ \033[0m")
        print("\033[34m██║        \033[33m██║   \033[32m██████╔╝╚██████╔╝██║  ██╗╚██████╔╝ \033[0m")
        print("\033[34m╚═╝        \033[33m╚═╝   \033[32m╚═════╝  ╚═════ ╚═╝  ╚═╝ ╚═════╝╝  \033[0m")
        print("")
    print("Select one of the options:")
    print("    [\033[31m1\033[0m] Start the game.")
    print("    [\033[34m2\033[0m] View Credits.")
    print("    [\033[32m3\033[0m] Exit.")
    option = input("Option: ")

    # read options
    if option == "1":
        prepareGame()
    elif option == "2":
        displayCredits()
    elif option == "3":
        return
    else:
        print("\033[31mInvalid option! Please try again.\033[0m")
        mainMenu(True)


def displayCredits():
    if debugOutput:
        print("displayCredits()")
    print("\033[34m██████  \033[33m██    ██ \033[32m██████   ██████  ██   ██ ██    ██ \033[0m")
    print("\033[34m██   ██  \033[33m██  ██  \033[32m██   ██ ██    ██ ██  ██  ██    ██ \033[0m")
    print("\033[34m██████    \033[33m████   \033[32m██   ██ ██    ██ █████   ██    ██ \033[0m")
    print("\033[34m██         \033[33m██    \033[32m██   ██ ██    ██ ██  ██  ██    ██ \033[0m")
    print("\033[34m██         \033[33m██    \033[32m██████   ██████  ██   ██  ██████  \033[0m      Version " + version)
    print("")
    print("A version of the classic puzzle game Sudoku made in Python! (Made in 3 days)")
    print("by IWant2TryHard (https://github.com/MyNameTsThad)")
    print("for his 8th grade Computer Science class (i guess???)")

    input("Continue: ")
    mainMenu()


def prepareGame():
    global needsTutorial
    if debugOutput:
        print("prepareGame()")
    if needsTutorial:
        print("Do you want to read the tutorial? (how to play the game) (This option will persist throughout the "
              "session)")
        tut = input("> ")
        if tut.lower() == "yes" or tut.lower() == "true" or tut.lower() == "y" or tut.lower() == "t":
            print("───────────────────────────────────────────────────────────────────────────\n"
                  "│-------------------------* How to play Sudoku *--------------------------│ \n"
                  "│Sudoku is a logic game played on a 9x9 grid using the digits 1 through 9.│\n│This grid is further "
                  "subdivided into nine 3x3 boxes.                     │\n│The goal is to fill in the grid with digits "
                  "such that one and only       │"
                  "\n│one "
                  "of each digit 1 through 9 appear in every row, column, and box.      │\n"
                  "│For more information for the extended tutorial visit here:               │\n"
                  "│https://www.logicgamesonline.com/sudoku/tutorial.html                    │\n"
                  "───────────────────────────────────────────────────────────────────────────")
            input("Continue (Enter)")
            print("")
            print("")
            print("What difficulty do you want?")
            print("    [\033[31m1\033[0m] Easy")
            print("    [\033[34m2\033[0m] Normal")
            print("    [\033[32m3\033[0m] Hard")
            print("    [\033[33m4\033[0m] Random difficulty")
            difficulty = input("Option: ")
            try:
                diffNum = int(difficulty)
                if diffNum > 4 or diffNum < 1:
                    print("\033[31mInvalid option! Please try again.\033[0m")
                    prepareGame()
                else:
                    startGame(diffNum)
            except ValueError:
                print("\033[31mInvalid option! Please try again.\033[0m")
                prepareGame()
            except TypeError:
                print("\033[31mInvalid option! Please try again.\033[0m")
                prepareGame()

        elif tut.lower() == "no" or tut.lower() == "false" or tut.lower() == "n" or tut.lower() == "f":
            needsTutorial = False
            print("")
            print("")
            print("What difficulty do you want?")
            print("    [\033[31m1\033[0m] Easy")
            print("    [\033[34m2\033[0m] Normal")
            print("    [\033[32m3\033[0m] Hard")
            print("    [\033[33m4\033[0m] Random difficulty")
            print("    [\033[36m5\033[0m] Back")
            difficulty = input("Option: ")

            try:
                diffNum = int(difficulty)
                if diffNum > 5 or diffNum < 1:
                    print("\033[31mInvalid option! Please try again.\033[0m")
                    prepareGame()
                else:
                    startGame(diffNum)
            except ValueError:
                print("\033[31mInvalid option! Please try again.\033[0m")
                prepareGame()
            except TypeError:
                print("\033[31mInvalid option! Please try again.\033[0m")
                prepareGame()
        else:
            print("\033[31mInput a valid option! Options are 'yes', 'true' or 'no', 'false'\033[0m")
            prepareGame()
    else:
        print("")
        print("")
        print("What difficulty do you want?")
        print("    [\033[31m1\033[0m] Easy")
        print("    [\033[34m2\033[0m] Normal")
        print("    [\033[32m3\033[0m] Hard")
        print("    [\033[33m4\033[0m] Random difficulty")
        print("    [\033[36m5\033[0m] Back")
        difficulty = input("Option: ")

        try:
            diffNum = int(difficulty)
            if diffNum > 5 or diffNum < 1:
                print("\033[31mInvalid option! Please try again.\033[0m")
                prepareGame()
            else:
                startGame(diffNum)
        except ValueError:
            print("\033[31mInvalid option! Please try again.\033[0m")
            prepareGame()
        except TypeError:
            print("\033[31mInvalid option! Please try again.\033[0m")
            prepareGame()


def startGame(difficulty):
    if debugOutput:
        print("startGame()")
    createBoard(difficulty)
    printBoard()
    mainGameLoop()


def mainGameLoop(isCallback=False):
    global playerTurnsCount
    global _currentTime

    _currentTime = round(time.time() * 100)

    if debugOutput:
        print("mainGameLoop()")

    # win condition
    if checkBoardIntegrity(gameBoard) == 1 and isBoardFilled():
        winGame()
        return

    if not isCallback:
        playerTurnsCount += 1
        print("")
        print("Turn: " + str(playerTurnsCount))

    rawInput = askInput()
    # check command integrity
    inputArr = list(rawInput)
    while not (inputArr[0] == '[' and inputArr[2] == ',' and inputArr[4] == ']' and inputArr[6] == '-'
               and inputArr[7] == '>' and inputArr[1].isnumeric() and inputArr[3].isnumeric()
               and inputArr[9].isnumeric()):
        inputArr = list(rawInput)
        if debugOutput:
            print(inputArr[0] == '[')
            print(inputArr[2] == ',')
            print(inputArr[4] == ']')
            print(inputArr[6] == '-')
            print(inputArr[7] == '>')
            print(inputArr[1].isnumeric())
            print(inputArr[3].isnumeric())
            print(inputArr[9].isnumeric())
        print("\033[31mInvalid Command! Please try again.\033[0m")
        rawInput = askInput()

    posX = int(inputArr[1])
    posY = int(inputArr[3])
    num = int(inputArr[9])

    if isAvailable(posX, posY):
        insertIntoBoard(posX, posY, num)
    else:
        print("\033[31mYou can't insert a number into that slot!\033[0m")
        mainGameLoop(True)

    printBoard()
    mainGameLoop()


def askInput():
    if debugOutput:
        print("askInput()")
    return input("Please input command (format: [x,y] -> num (0 is empty) Ex. [1,1] -> 3): ")


def winGame():
    global gameBoard
    global playerTurnsPos
    global playerTurnsCount
    global playerScore
    global _currentTime
    global _responseTime
    print("\033[5m\033[32m╔═╗┌─┐┌┐┌┌─┐┬─┐┌─┐┌┬┐┬ ┬┬  ┌─┐┌┬┐┬┌─┐┌┐┌┌─┐┬\n"
                         "║  │ │││││ ┬├┬┘├─┤ │ │ ││  ├─┤ │ ││ ││││└─┐│\n"
                         "╚═╝└─┘┘└┘└─┘┴└─┴ ┴ ┴ └─┘┴─┘┴ ┴ ┴ ┴└─┘┘└┘└─┘o\033[0m")
    print("\033[32mYou won!\033[0m")
    print(f"\033[33mIn {playerTurnsCount} turns\033[0m, \033[32mYou have achieved a score of {playerScore}!\033[0m")

    # reset stats
    gameBoard = [[" ", " ", " ", " ", " ", " ", " ", " ", " "],
                 [" ", " ", " ", " ", " ", " ", " ", " ", " "],
                 [" ", " ", " ", " ", " ", " ", " ", " ", " "],
                 [" ", " ", " ", " ", " ", " ", " ", " ", " "],
                 [" ", " ", " ", " ", " ", " ", " ", " ", " "],
                 [" ", " ", " ", " ", " ", " ", " ", " ", " "],
                 [" ", " ", " ", " ", " ", " ", " ", " ", " "],
                 [" ", " ", " ", " ", " ", " ", " ", " ", " "],
                 [" ", " ", " ", " ", " ", " ", " ", " ", " "]]

    playerTurnsPos = []
    playerTurnsCount = 0
    playerScore = 0

    _currentTime = 0
    _responseTime = 0

    print("")
    print("What do you want to do now?")
    print("    [\033[31m1\033[0m] Start a new game.")
    print("    [\033[34m2\033[0m] Go back to the Main menu.")
    print("    [\033[32m3\033[0m] Quit the game.")
    option = input("Option: ")
    if option == "1":
        prepareGame()
    elif option == "2":
        mainMenu()
    elif option == "3":
        print("Thanks for playing!")
        return
    else:
        print("\033[31mInvalid option! Please try again.\033[0m")


def insertIntoBoard(x, y, num):
    global gameBoard
    global playerTurnsPos
    global _responseTime
    global playerScore

    if debugOutput:
        print("insertIntoBoard()")
    if gameBoard[y - 1][x - 1] == " ":
        if checkIntegrity(gameBoard, x, y, num):
            if num == 0:
                forceInsertIntoBoard(x, y, " ")
                if isBoardFilled():
                    if checkBoardIntegrity(gameBoard) == 2 or checkBoardIntegrity(gameBoard) == 3:
                        print("\033[31mInvalid Board!\033[0m")

                _responseTime = round(time.time() * 100)
                scoreSubtract = _responseTime - _currentTime
                playerScore -= scoreSubtract
            else:
                forceInsertIntoBoard(x, y, num)
                if isBoardFilled():
                    if checkBoardIntegrity(gameBoard) == 2 or checkBoardIntegrity(gameBoard) == 3:
                        print("\033[31mInvalid Board!\033[0m")

                _responseTime = round(time.time() * 100)
                scoreSubtract = _responseTime - _currentTime
                playerScore -= scoreSubtract
        else:
            print("\033[31mInvalid Location! Please try again.\033[0m")
            mainGameLoop(True)
    else:
        isPlayerPlaced = False
        for i in playerTurnsPos:
            thisX = i[0]
            thisY = i[1]
            if thisX == x and thisY == y:
                isPlayerPlaced = True
        if isPlayerPlaced:
            if checkIntegrity(gameBoard, x, y, num):
                if num == 0:
                    forceInsertIntoBoard(x, y, " ")
                    if isBoardFilled():
                        if checkBoardIntegrity(gameBoard) == 2 or checkBoardIntegrity(gameBoard) == 3:
                            print("\033[31mInvalid Board!\033[0m")

                    _responseTime = round(time.time() * 100)
                    scoreSubtract = _responseTime - _currentTime
                    playerScore -= scoreSubtract
                else:
                    forceInsertIntoBoard(x, y, num)
                    if isBoardFilled():
                        if checkBoardIntegrity(gameBoard) == 2 or checkBoardIntegrity(gameBoard) == 3:
                            print("\033[31mInvalid Board!\033[0m")

                    _responseTime = round(time.time() * 100)
                    scoreSubtract = _responseTime - _currentTime
                    playerScore -= scoreSubtract
            else:
                print("\033[31mInvalid Location! Please try again.\033[0m")
                mainGameLoop(True)


def isAvailable(x, y):
    global gameBoard
    global playerTurnsPos

    if debugOutput:
        print("isAvailable()")
    if gameBoard[y - 1][x - 1] == " ":
        return True
    else:
        isPlayerPlaced = False
        for i in playerTurnsPos:
            thisX = i[0]
            thisY = i[1]
            if thisX == x and thisY == y:
                isPlayerPlaced = True
        if isPlayerPlaced:
            return True
        else:
            return False


def isBoardFilled():
    global gameBoard
    if debugOutput:
        print("isBoardFilled()")
    isFilled = True
    for y in range(len(gameBoard)):
        for x in range(len(gameBoard[y])):
            if gameBoard[y][x] == " ":
                isFilled = False

    return isFilled


def checkIntegrity(board, x, y, num):
    global advancedDebugOutput
    if debugOutput:
        print("checkIntegrity()")
        if advancedDebugOutput:
            print(f"===========-+ Advanced Debug Output (checkIntegrity({board}, {x}, {y}, {num})) +-===========")
        else:
            print(f"===========-+ Debug Output (checkIntegrity()) +-===========")
    newBoard = board
    newBoard[y - 1][x - 1] = num
    repeats = 0
    # x axis (horizontal)
    for aItem in range(len(newBoard[y - 1])):
        a = newBoard[y - 1][aItem]
        if debugOutput:
            if advancedDebugOutput:
                print(
                    f"checking item with coordinates [{aItem},{y - 1}] with {newBoard[y - 1][x - 1]} [{x - 1},{y - 1}]")

        if a == newBoard[y - 1][x - 1]:
            repeats += 1
            if debugOutput:
                print(f"item with coordinates [{aItem},{y - 1}] is a repeat, repeats is now {repeats}")

    # y axis (vertical)
    for bItem in range(len(newBoard)):
        b = newBoard[bItem]
        if debugOutput:
            if advancedDebugOutput:
                print(
                    f"checking item with coordinates [{x - 1},{bItem}] with {newBoard[y - 1][x - 1]} [{x - 1},{y - 1}]")

        if b[x - 1] == newBoard[y - 1][x - 1]:
            repeats += 1
            if debugOutput:
                print(f"item with coordinates [{x - 1},{bItem}] is a repeat, repeats is now {repeats}")

    # cell block check
    if x == 1 or x == 4 or x == 7:
        if y == 1 or y == 4 or y == 7:
            cellBlock = [newBoard[y - 1][x - 1], newBoard[y - 1][x], newBoard[y - 1][x + 1],
                         newBoard[y][x - 1], newBoard[y][x], newBoard[y][x + 1],
                         newBoard[y + 1][x - 1], newBoard[y + 1][x], newBoard[y + 1][x + 1]]
            for cItem in range(len(cellBlock)):
                c = cellBlock[cItem]
                if debugOutput:
                    if advancedDebugOutput:
                        print(
                            f"checking item {cItem} within cellgroup with {newBoard[y - 1][x - 1]} [{x - 1},{y - 1}]")

                if c == newBoard[y - 1][x - 1]:
                    repeats += 1
                    if debugOutput:
                        print(f"item {cItem} within cellgroup is a repeat, repeats is now {repeats}")
        elif y == 2 or y == 5 or y == 8:
            cellBlock = [newBoard[y - 2][x - 1], newBoard[y - 2][x], newBoard[y - 2][x + 1],
                         newBoard[y - 1][x - 1], newBoard[y - 1][x], newBoard[y - 1][x + 1],
                         newBoard[y][x - 1], newBoard[y][x], newBoard[y][x + 1]]
            for cItem in range(len(cellBlock)):
                c = cellBlock[cItem]
                if debugOutput:
                    if advancedDebugOutput:
                        print(
                            f"checking item {cItem} within cellgroup with {newBoard[y - 1][x - 1]} [{x - 1},{y - 1}]")

                if c == newBoard[y - 1][x - 1]:
                    repeats += 1
                    if debugOutput:
                        print(f"item {cItem} within cellgroup is a repeat, repeats is now {repeats}")
        elif y == 3 or y == 6 or y == 9:
            cellBlock = [newBoard[y - 3][x - 1], newBoard[y - 3][x], newBoard[y - 3][x + 1],
                         newBoard[y - 2][x - 1], newBoard[y - 2][x], newBoard[y - 2][x + 1],
                         newBoard[y - 1][x - 1], newBoard[y - 1][x], newBoard[y - 1][x + 1]]
            for cItem in range(len(cellBlock)):
                c = cellBlock[cItem]
                if debugOutput:
                    if advancedDebugOutput:
                        print(
                            f"checking item {cItem} within cellgroup with {newBoard[y - 1][x - 1]} [{x - 1},{y - 1}]")

                if c == newBoard[y - 1][x - 1]:
                    repeats += 1
                    if debugOutput:
                        print(f"item {cItem} within cellgroup is a repeat, repeats is now {repeats}")
    elif x == 2 or x == 5 or x == 8:
        if y == 1 or y == 4 or y == 7:
            cellBlock = [newBoard[y - 1][x - 2], newBoard[y - 1][x - 1], newBoard[y - 1][x],
                         newBoard[y][x - 2], newBoard[y][x - 1], newBoard[y][x],
                         newBoard[y + 1][x - 2], newBoard[y + 1][x - 1], newBoard[y + 1][x]]
            for cItem in range(len(cellBlock)):
                c = cellBlock[cItem]
                if debugOutput:
                    if advancedDebugOutput:
                        print(
                            f"checking item {cItem} within cellgroup with {newBoard[y - 1][x - 1]} [{x - 1},{y - 1}]")

                if c == newBoard[y - 1][x - 1]:
                    repeats += 1
                    if debugOutput:
                        print(f"item {cItem} within cellgroup is a repeat, repeats is now {repeats}")
        elif y == 2 or y == 5 or y == 8:
            cellBlock = [newBoard[y - 2][x - 2], newBoard[y - 2][x - 1], newBoard[y - 2][x],
                         newBoard[y - 1][x - 2], newBoard[y - 1][x - 1], newBoard[y - 1][x],
                         newBoard[y][x - 2], newBoard[y][x - 1], newBoard[y][x]]
            for cItem in range(len(cellBlock)):
                c = cellBlock[cItem]
                if debugOutput:
                    if advancedDebugOutput:
                        print(
                            f"checking item {cItem} within cellgroup with {newBoard[y - 1][x - 1]} [{x - 1},{y - 1}]")

                if c == newBoard[y - 1][x - 1]:
                    repeats += 1
                    if debugOutput:
                        print(f"item {cItem} within cellgroup is a repeat, repeats is now {repeats}")
        elif y == 3 or y == 6 or y == 9:
            cellBlock = [newBoard[y - 3][x - 2], newBoard[y - 3][x - 1], newBoard[y - 3][x],
                         newBoard[y - 2][x - 2], newBoard[y - 2][x - 1], newBoard[y - 2][x],
                         newBoard[y - 1][x - 2], newBoard[y - 1][x - 1], newBoard[y - 1][x]]
            for cItem in range(len(cellBlock)):
                c = cellBlock[cItem]
                if debugOutput:
                    if advancedDebugOutput:
                        print(
                            f"checking item {cItem} within cellgroup with {newBoard[y - 1][x - 1]} [{x - 1},{y - 1}]")

                if c == newBoard[y - 1][x - 1]:
                    repeats += 1
                    if debugOutput:
                        print(f"item {cItem} within cellgroup is a repeat, repeats is now {repeats}")
    elif x == 3 or x == 6 or x == 9:
        if y == 1 or y == 4 or y == 7:
            cellBlock = [newBoard[y - 1][x - 3], newBoard[y - 1][x - 2], newBoard[y - 1][x - 1],
                         newBoard[y][x - 3], newBoard[y][x - 2], newBoard[y][x - 1],
                         newBoard[y + 1][x - 3], newBoard[y + 1][x - 2], newBoard[y + 1][x - 1]]
            for cItem in range(len(cellBlock)):
                c = cellBlock[cItem]
                if debugOutput:
                    if advancedDebugOutput:
                        print(
                            f"checking item {cItem} within cellgroup with {newBoard[y - 1][x - 1]} [{x - 1},{y - 1}]")

                if c == newBoard[y - 1][x - 1]:
                    repeats += 1
                    if debugOutput:
                        print(f"item {cItem} within cellgroup is a repeat, repeats is now {repeats}")
        elif y == 2 or y == 5 or y == 8:
            cellBlock = [newBoard[y - 2][x - 3], newBoard[y - 2][x - 2], newBoard[y - 2][x - 1],
                         newBoard[y - 1][x - 3], newBoard[y - 1][x - 2], newBoard[y - 1][x - 1],
                         newBoard[y][x - 3], newBoard[y][x - 2], newBoard[y][x - 1]]
            for cItem in range(len(cellBlock)):
                c = cellBlock[cItem]
                if debugOutput:
                    if advancedDebugOutput:
                        print(
                            f"checking item {cItem} within cellgroup with {newBoard[y - 1][x - 1]} [{x - 1},{y - 1}]")

                if c == newBoard[y - 1][x - 1]:
                    repeats += 1
                    if debugOutput:
                        print(f"item {cItem} within cellgroup is a repeat, repeats is now {repeats}")
        elif y == 3 or y == 6 or y == 9:
            cellBlock = [newBoard[y - 3][x - 3], newBoard[y - 3][x - 2], newBoard[y - 3][x - 1],
                         newBoard[y - 2][x - 3], newBoard[y - 2][x - 2], newBoard[y - 2][x - 1],
                         newBoard[y - 1][x - 3], newBoard[y - 1][x - 2], newBoard[y - 1][x - 1]]
            for cItem in range(len(cellBlock)):
                c = cellBlock[cItem]
                if debugOutput:
                    if advancedDebugOutput:
                        print(
                            f"checking item {cItem} within cellgroup with {newBoard[y - 1][x - 1]} [{x - 1},{y - 1}]")

                if c == newBoard[y - 1][x - 1]:
                    repeats += 1
                    if debugOutput:
                        print(f"item {cItem} within cellgroup is a repeat, repeats is now {repeats}")

    # final check
    if repeats <= 3:
        if debugOutput:
            print(f"repeats is {repeats}, Integrity check passed")
        return True
    else:
        if debugOutput:
            print(f"repeats is {repeats}, Integrity check failed")
        return False


def checkBoardIntegrity(board):
    if debugOutput:
        print("checkBoardIntegrity()")
    isStillValid = 0
    isFilled = True
    for y in range(len(board)):
        for x in range(len(board[y])):
            if not board[y][x] == " ":
                if not checkIntegrity(board, x + 1, y + 1, board[y][x]):
                    isStillValid += 1
                else:
                    isStillValid += 0
            else:
                isFilled = False

    if isStillValid > 0:
        if isFilled:
            return 3
        else:
            return 2
    else:
        if isFilled:
            return 1
        else:
            return 0


def forceInsertIntoBoard(x, y, num):
    global gameBoard

    if debugOutput:
        print("forceInsertIntoBoard()")
    if num == 0:
        gameBoard[y - 1][x - 1] = " "
    else:
        gameBoard[y - 1][x - 1] = num


def createBoard(difficulty):
    global gameBoard
    global playerScore
    if debugOutput:
        print("createBoard()")
    gameBoard = initBoard(3)
    diffNum = int(difficulty)
    if diffNum == 1:
        removeNumbers(20)
        playerScore = 30000
    elif diffNum == 2:
        removeNumbers(40)
        playerScore = 60000
    elif diffNum == 3:
        removeNumbers(60)
        playerScore = 90000
    elif diffNum == 4:
        createBoard(random.randint(1, 3))
    elif diffNum == 5:
        mainMenu()
    elif diffNum <= 100:
        playerScore = 0
        removeNumbers(81)
    else:
        playerScore = 0
        removeNumbers(1)

    check = checkBoardIntegrity(gameBoard)
    if debugOutput:
        if check == 0 or check == 1:
            print("Board Integrity check passed")
        else:
            print("Board Integrity check failed, recreating board")
            createBoard(difficulty)


def pattern(cellGroupSize, r, c):
    return (cellGroupSize * (r % cellGroupSize) + r // cellGroupSize + c) % (cellGroupSize * cellGroupSize)


def shuffle(s):
    return random.sample(s, len(s))


def initBoard(cellGroupSize):
    rBase = range(cellGroupSize)
    rows = [g * cellGroupSize + r for g in shuffle(rBase) for r in shuffle(rBase)]
    cols = [g * cellGroupSize + c for g in shuffle(rBase) for c in shuffle(rBase)]
    nums = shuffle(range(1, cellGroupSize * cellGroupSize + 1))

    board = [[nums[pattern(cellGroupSize, r, c)] for c in cols] for r in rows]
    return board


def removeNumbers(remove_amount):
    global gameBoard
    if debugOutput:
        print("removeNumbers()")
    h, w, r = len(gameBoard), len(gameBoard[0]), []
    spaces = [[x, y] for x in range(h) for y in range(w)]
    for k in range(remove_amount):
        r = random.choice(spaces)
        gameBoard[r[0]][r[1]] = " "
        spaces.remove(r)


def printBoard():
    if debugOutput:
        print("printBoard()")
    print("     \033[31m1   2   3   4   5   6   7   8   9     x\033[0m\n"
          "   \033[33m┌───┬───┬───┬───┬───┬───┬───┬───┬───┐\033[0m\n"
          f"\033[34m1\033[0m  \033[33m│\033[0m \033[32m{gameBoard[0][0]}\033[0m \033[33m│\033[0m \033[32m{gameBoard[0][1]}\033[0m \033[33m│\033[0m \033[32m{gameBoard[0][2]}\033[0m \033[33m│\033[0m \033[32m{gameBoard[0][3]}\033[0m \033[33m│\033[0m \033[32m{gameBoard[0][4]}\033[0m \033[33m│\033[0m \033[32m{gameBoard[0][5]}\033[0m \033[33m│\033[0m \033[32m{gameBoard[0][6]}\033[0m \033[33m│\033[0m \033[32m{gameBoard[0][7]}\033[0m \033[33m│\033[0m \033[32m{gameBoard[0][8]}\033[0m \033[33m│\033[0m\n"
          "   \033[33m├───┼───┼───┼───┼───┼───┼───┼───┼───┤\033[0m\n"
          f"\033[34m2\033[0m  \033[33m│\033[0m \033[32m{gameBoard[1][0]}\033[0m \033[33m│\033[0m \033[32m{gameBoard[1][1]}\033[0m \033[33m│\033[0m \033[32m{gameBoard[1][2]}\033[0m \033[33m│\033[0m \033[32m{gameBoard[1][3]}\033[0m \033[33m│\033[0m \033[32m{gameBoard[1][4]}\033[0m \033[33m│\033[0m \033[32m{gameBoard[1][5]}\033[0m \033[33m│\033[0m \033[32m{gameBoard[1][6]}\033[0m \033[33m│\033[0m \033[32m{gameBoard[1][7]}\033[0m \033[33m│\033[0m \033[32m{gameBoard[1][8]}\033[0m \033[33m│\033[0m\n"
          "   \033[33m├───┼───┼───┼───┼───┼───┼───┼───┼───┤\033[0m\n"
          f"\033[34m3\033[0m  \033[33m│\033[0m \033[32m{gameBoard[2][0]}\033[0m \033[33m│\033[0m \033[32m{gameBoard[2][1]}\033[0m \033[33m│\033[0m \033[32m{gameBoard[2][2]}\033[0m \033[33m│\033[0m \033[32m{gameBoard[2][3]}\033[0m \033[33m│\033[0m \033[32m{gameBoard[2][4]}\033[0m \033[33m│\033[0m \033[32m{gameBoard[2][5]}\033[0m \033[33m│\033[0m \033[32m{gameBoard[2][6]}\033[0m \033[33m│\033[0m \033[32m{gameBoard[2][7]}\033[0m \033[33m│\033[0m \033[32m{gameBoard[2][8]}\033[0m \033[33m│\033[0m\n"
          "   \033[33m├───┼───┼───┼───┼───┼───┼───┼───┼───┤\033[0m\n"
          f"\033[34m4\033[0m  \033[33m│\033[0m \033[32m{gameBoard[3][0]}\033[0m \033[33m│\033[0m \033[32m{gameBoard[3][1]}\033[0m \033[33m│\033[0m \033[32m{gameBoard[3][2]}\033[0m \033[33m│\033[0m \033[32m{gameBoard[3][3]}\033[0m \033[33m│\033[0m \033[32m{gameBoard[3][4]}\033[0m \033[33m│\033[0m \033[32m{gameBoard[3][5]}\033[0m \033[33m│\033[0m \033[32m{gameBoard[3][6]}\033[0m \033[33m│\033[0m \033[32m{gameBoard[3][7]}\033[0m \033[33m│\033[0m \033[32m{gameBoard[3][8]}\033[0m \033[33m│\033[0m\n"
          "   \033[33m├───┼───┼───┼───┼───┼───┼───┼───┼───┤\033[0m\n"
          f"\033[34m5\033[0m  \033[33m│\033[0m \033[32m{gameBoard[4][0]}\033[0m \033[33m│\033[0m \033[32m{gameBoard[4][1]}\033[0m \033[33m│\033[0m \033[32m{gameBoard[4][2]}\033[0m \033[33m│\033[0m \033[32m{gameBoard[4][3]}\033[0m \033[33m│\033[0m \033[32m{gameBoard[4][4]}\033[0m \033[33m│\033[0m \033[32m{gameBoard[4][5]}\033[0m \033[33m│\033[0m \033[32m{gameBoard[4][6]}\033[0m \033[33m│\033[0m \033[32m{gameBoard[4][7]}\033[0m \033[33m│\033[0m \033[32m{gameBoard[4][8]}\033[0m \033[33m│\033[0m\n"
          "   \033[33m├───┼───┼───┼───┼───┼───┼───┼───┼───┤\033[0m\n"
          f"\033[34m6\033[0m  \033[33m│\033[0m \033[32m{gameBoard[5][0]}\033[0m \033[33m│\033[0m \033[32m{gameBoard[5][1]}\033[0m \033[33m│\033[0m \033[32m{gameBoard[5][2]}\033[0m \033[33m│\033[0m \033[32m{gameBoard[5][3]}\033[0m \033[33m│\033[0m \033[32m{gameBoard[5][4]}\033[0m \033[33m│\033[0m \033[32m{gameBoard[5][5]}\033[0m \033[33m│\033[0m \033[32m{gameBoard[5][6]}\033[0m \033[33m│\033[0m \033[32m{gameBoard[5][7]}\033[0m \033[33m│\033[0m \033[32m{gameBoard[5][8]}\033[0m \033[33m│\033[0m\n"
          "   \033[33m├───┼───┼───┼───┼───┼───┼───┼───┼───┤\033[0m\n"
          f"\033[34m7\033[0m  \033[33m│\033[0m \033[32m{gameBoard[6][0]}\033[0m \033[33m│\033[0m \033[32m{gameBoard[6][1]}\033[0m \033[33m│\033[0m \033[32m{gameBoard[6][2]}\033[0m \033[33m│\033[0m \033[32m{gameBoard[6][3]}\033[0m \033[33m│\033[0m \033[32m{gameBoard[6][4]}\033[0m \033[33m│\033[0m \033[32m{gameBoard[6][5]}\033[0m \033[33m│\033[0m \033[32m{gameBoard[6][6]}\033[0m \033[33m│\033[0m \033[32m{gameBoard[6][7]}\033[0m \033[33m│\033[0m \033[32m{gameBoard[6][8]}\033[0m \033[33m│\033[0m\n"
          "   \033[33m├───┼───┼───┼───┼───┼───┼───┼───┼───┤\033[0m\n"
          f"\033[34m8\033[0m  \033[33m│\033[0m \033[32m{gameBoard[7][0]}\033[0m \033[33m│\033[0m \033[32m{gameBoard[7][1]}\033[0m \033[33m│\033[0m \033[32m{gameBoard[7][2]}\033[0m \033[33m│\033[0m \033[32m{gameBoard[7][3]}\033[0m \033[33m│\033[0m \033[32m{gameBoard[7][4]}\033[0m \033[33m│\033[0m \033[32m{gameBoard[7][5]}\033[0m \033[33m│\033[0m \033[32m{gameBoard[7][6]}\033[0m \033[33m│\033[0m \033[32m{gameBoard[7][7]}\033[0m \033[33m│\033[0m \033[32m{gameBoard[7][8]}\033[0m \033[33m│\033[0m\n"
          "   \033[33m├───┼───┼───┼───┼───┼───┼───┼───┼───┤\033[0m\n"
          f"\033[34m9\033[0m  \033[33m│\033[0m \033[32m{gameBoard[8][0]}\033[0m \033[33m│\033[0m \033[32m{gameBoard[8][1]}\033[0m \033[33m│\033[0m \033[32m{gameBoard[8][2]}\033[0m \033[33m│\033[0m \033[32m{gameBoard[8][3]}\033[0m \033[33m│\033[0m \033[32m{gameBoard[8][4]}\033[0m \033[33m│\033[0m \033[32m{gameBoard[8][5]}\033[0m \033[33m│\033[0m \033[32m{gameBoard[8][6]}\033[0m \033[33m│\033[0m \033[32m{gameBoard[8][7]}\033[0m \033[33m│\033[0m \033[32m{gameBoard[8][8]}\033[0m \033[33m│\033[0m\n"
          "   \033[33m└───┴───┴───┴───┴───┴───┴───┴───┴───┘\033[0m\n"
          "\033[34my\033[0m")


if __name__ == '__main__':
    mainMenu()
