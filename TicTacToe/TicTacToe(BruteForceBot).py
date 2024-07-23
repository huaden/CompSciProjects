# Name: Hayden Robinette
# Date: Feb 6, 2023
# Purpose: To practice making a minimax bot
# Sources: https://www.youtube.com/watch?v=trKjYdBASyQ&t=1041s


class TicTacToeBoard:
    def __init__(board):
        board.table = [["."] * 3, ["."] * 3, ["."] * 3]
        board.moves = [[]]


TTT = TicTacToeBoard()

xoTurn = "O"
winner = None
hasNoWin = True
hasNoDraw = True


def printBoard():
    for row in range(0, 3):
        for col in range(0, 3):
            print(TTT.table[row][col], end="")
        print()
    print()


def hasWinner():
    # checks to see if all of one row is the same, returns the winner if they are
    for row in range(0, 3):
        if (TTT.table[row][0] == TTT.table[row][1] == TTT.table[row][2]) and TTT.table[row][0] != ".":
            return TTT.table[row][0]

    # checks to see if all of one column is the same, returns the winner if they are
    for col in range(0, 3):
        if (TTT.table[0][col] == TTT.table[1][col] == TTT.table[2][col]) and TTT.table[0][col] != ".":
            return TTT.table[0][col]

    # Checks diagnols for wins, returns winnere if they are
    if (TTT.table[0][0] == TTT.table[1][1] == TTT.table[2][2]) and TTT.table[0][0] != ".":
        return TTT.table[0][0]
    if (TTT.table[2][0] == TTT.table[1][1] == TTT.table[0][2]) and TTT.table[1][1] != ".":
        return TTT.table[1][1]

    # checks for draw, if there is a draw, return draw value which is "XO"
    isSpace = False
    for i in range(0, 3):
        for j in range(0, 3):
            if TTT.table[i][j] == ".":
                isSpace = True
    if not isSpace:
        return "XO"
    return None


# return the value of each possible outcome
def scoreTotal(val):
    if val == "X":
        return -1
    if val == "O":
        return 1
    if val == "XO":
        return 0


def miniMax(depth, isMaxing):
    # checks for winner/base condition to stop recursion
    win = hasWinner()
    if win is not None:
        score = scoreTotal(win)
        return score

    # if it is the Ai's turn, then you want score to be maxed
    if isMaxing:
        bestScore = -100000
        for row in range(0, 3):
            for col in range(0, 3):
                if TTT.table[row][col] == ".":  # goes to all available spots
                    TTT.table[row][col] = "O"
                    score = int(miniMax(depth + 1, False))  # checks all possible player moves
                    TTT.table[row][col] = "."
                    bestScore = max(bestScore, score)

        return bestScore
    else:  # if it is the player's turn
        bestScore = 100000
        for row in range(0, 3):
            for col in range(0, 3):
                if TTT.table[row][col] == ".":  # goes to all available spots
                    TTT.table[row][col] = "X"
                    score = int(miniMax(depth + 1, True))  # checks all possible bot moves
                    TTT.table[row][col] = "."
                    bestScore = min(score, bestScore)

        return bestScore


def bestMove():
    bestScore = -1000
    bestMove = [-1, -1]
    for row in range(0, 3):
        for col in range(0, 3):
            if TTT.table[row][col] == ".":
                TTT.table[row][col] = "O"

                score = miniMax(0, False)

                TTT.table[row][col] = "."
                if score > bestScore:
                    bestScore = score
                    bestMove[0] = row
                    bestMove[1] = col

    TTT.table[bestMove[0]][bestMove[1]] = "O"
    TTT.moves.append([bestMove[0], bestMove[1]])


printBoard()

while winner is None:
    if xoTurn == "X":
        valid = False
        while not valid:
            row = int(input("Enter the row you want to go in (1 being the highest): "))
            col = int(input("Enter the row you want to go in (1 being the farthest left): "))
            if row < 1 or col < 1:
                print("Not valid idiot")
            elif TTT.table[row - 1][col - 1] == ".":
                valid = True
            else:
                print("Not a possible move")

        TTT.table[row - 1][col - 1] = xoTurn
        TTT.moves.append([row - 1, col - 1])
        xoTurn = "O"
    elif xoTurn == "O":
        bestMove()
        xoTurn = "X"

    if hasWinner() is not None:
        winner = hasWinner()

    printBoard()
