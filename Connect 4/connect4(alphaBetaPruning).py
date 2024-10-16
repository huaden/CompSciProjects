# Name: Hayden Robinette
# Date: Feb 8, 2023
# Purpose: Try to create a miniMax algorithm with alpha-beta pruning
# Resources used: https://www.youtube.com/watch?v=MMLtza3CZFM,
# https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-4-alpha-beta-pruning/


import pygame as pg, sys
import pygame.display
from pygame.locals import *
import time

board = [["."] * 7, ["."] * 7, ["."] * 7, ["."] * 7, ["."] * 7, ["."] * 7]
colWeight = [1,1,2,3,2,1,1]
rowWeight = [1,2,2,3,3,1]
spotVal = [[0] * 7, [0] * 7, [0] * 7, [0] * 7, [0] * 7, [0] * 7]
for i in colWeight:
    for j in rowWeight:
        spotVal[j][i] = j*i

game_state = "start_menu"
turn = "Red"
botColor = "Yellow"
playerColor = "Red"
firstPlay = "Red"
userTurn = turn == playerColor
winner = None
draw = False
white = (255, 255, 255)
black = (10, 10, 10)
width = 490
height = 420

avalMoves = [[5,0], [5,1], [5,2], [5,3], [5,4], [5,5], [5,6] ]


pg.init()
fps = 30
CLOCK = pg.time.Clock()
screen = pg.display.set_mode((width, height + 80), 0, 32)
pg.display.set_caption("Connect 4")

openingImg = pg.image.load("connect4Opening.png")
yellowChip = pg.image.load("connect4_yellowChip.png")
redChip = pg.image.load("connect4_redChip.png")

opening = pg.transform.scale(openingImg, (width, height + 80))
yellowChip = pg.transform.scale(yellowChip, (50, 50))
redChip = pg.transform.scale(redChip, (50, 50))


def game_opening():
    screen.fill(black)
    screen.blit(openingImg, (50, 50))
    pg.display.update()
    time.sleep(1)
    draw_lines()
    draw_status()


def draw_lines():
    screen.fill(white)

    # vertical lines
    pg.draw.line(screen, black, (width / 7, 0), (width / 7, height), 10)
    pg.draw.line(screen, black, (width / 7 * 2, 0), (width / 7 * 2, height), 10)
    pg.draw.line(screen, black, (width / 7 * 3, 0), (width / 7 * 3, height), 10)
    pg.draw.line(screen, black, (width / 7 * 4, 0), (width / 7 * 4, height), 10)
    pg.draw.line(screen, black, (width / 7 * 5, 0), (width / 7 * 5, height), 10)
    pg.draw.line(screen, black, (width / 7 * 6, 0), (width / 7 * 6, height), 10)

    # horizontal lines
    pg.draw.line(screen, black, (0, height / 6), (width, height / 6), 10)
    pg.draw.line(screen, black, (0, height / 6 * 2), (width, height / 6 * 2), 10)
    pg.draw.line(screen, black, (0, height / 6 * 3), (width, height / 6 * 3), 10)
    pg.draw.line(screen, black, (0, height / 6 * 4), (width, height / 6 * 4), 10)
    pg.draw.line(screen, black, (0, height / 6 * 5), (width, height / 6 * 5), 10)
    pg.draw.line(screen, black, (0, height), (width, height), 10)

    pg.display.update()


def draw_status():
    global draw
    if winner is None:
        if winner is None:
            message = turn + "'s Turn"
    else:
        message = winner + " won!"
    if draw:
        message = "Game Draw"

    screen.fill(white, (0, height, width, 80))
    font = pg.font.Font(None, 30)
    text = font.render(message, 1, (black))
    screen.blit(text, (width / 2 - text.get_width() / 2, height + 40))

    pg.display.update()

def bestMove():
    global avalMoves, spotVal
    bestScore = -10000
    move = [-1,1]
    tempAvalMove = avalMoves
    for i in range(0,len(tempAvalMove)):
        row = tempAvalMove[i][0]
        col = tempAvalMove[i][1]
        if board[row][col] == ".":
            board[row][col] = "Yellow"
            tempAvalMove[col][0] -= 1
            score = spotVal[row][col]
            score += miniMax(tempAvalMove, 0, False, -1000, 1000)
            board[row][col] = "."
            tempAvalMove[col][0] += 1
            if score > bestScore:
                bestScore = score
                move[0] = row
                move[1] = col


    draw_Move(move[0]+1, move[1]+1)



def scoring(val):
    global botColor, playerColor
    if val == "Yellow":
        return 100000000
    if val == "Red":
        return -100000000
    if val == "Draw":
        return 0

def countVal(countRed, countYellow, countEmpty, emptyRow):
    score = 0
    if countRed == 3 and countEmpty == 1:
        score -= 8
        if emptyRow >= 3:
            score -=2
    if countYellow == 3 and countEmpty == 1:
        score += 10
        if emptyRow >= 3:
            score +=2
    if countRed == 2 and countEmpty >= 1:
        score -= 3
    if countYellow == 2 and countEmpty >= 1:
        score += 3
    return score
def scoreBoard():
    global board
    score = 0
    for row in range(0, 6):
        for i in range(0, 4):
            countRed = 0
            countYellow = 0
            empty = 0
            emptyRow = 0
            for q in range(0,4):
                if board[row][i+q] == playerColor:
                    countRed += 1
                if board[row][i+q] == botColor:
                    countYellow += 1
                if board[row][i+q] == ".":
                    empty += 1
                    emptyRow = row
            score += countVal(countRed, countYellow, empty, emptyRow)

    for col in range(0, 7):
        for i in range(0, 3):
            countRed = 0
            countYellow = 0
            empty = 0
            emptyRow = 0
            for q in range(0,4):
                if board[i+q][col] == playerColor:
                    countRed += 1
                if board[i+q][col] == botColor:
                    countYellow += 1
                if board[i+q][col] == ".":
                    empty += 1
                    emptyRow = i+q
            score += countVal(countRed, countYellow, empty, emptyRow)


    for row in range(0, 3):
        for col in range(0, 4):
            countRed = 0
            countYellow = 0
            empty = 0
            emptyRow = 0
            for q in range(0,4):
                if board[row+q][col+q] == playerColor:
                    countRed += 1
                if board[row+q][col+q] == botColor:
                    countYellow += 1
                if board[row+q][col+q] == ".":
                    empty += 1
                    emptyRow = row+q
            score += countVal(countRed, countYellow, empty, emptyRow)

    for row in range(5, 2, -1):
        for col in range(0, 4):
            countRed = 0
            countYellow = 0
            empty = 0
            emptyRow = 0
            for q in range(0,4):
                if board[row-q][col+q] == playerColor:
                    countRed += 1
                if board[row-q][col+q] == botColor:
                    countYellow += 1
                if board[row-q][col+q] == ".":
                    empty += 1
                    emptyRow = row-q
            score += countVal(countRed, countYellow, empty, emptyRow)

    return score



#time per move by depth
# Depth 4: 1.53s
# Depth 5: 2.76s, 3.41s, 4.05s, 4.25s, 3.43s, 3.43s, 3.46s, 4.40s, 3.01s, 2.9s, 0.53s
# Depth 6: 7.13s, 6.91s, 14.65s, 11.6s, 13.18s, 15.18s, 12.05s, 13.93s, 9.99s, 1.99s
# Depth 7: 45.86s
# Depth 8:

def miniMax(curMoves, depth, isMaxing, alpha, beta):
    wins = checkWin()
    win = wins[0]
    if win is not None:
        return scoring(win)
    if depth == 5:
        return scoreBoard()

    if isMaxing:
        bestScore = -1000
        for i in range(0,len(curMoves)):
            row = curMoves[i][0]
            col = curMoves[i][1]
            if board[row][col] == ".":
                if row >= 0:
                    board[row][col] = "Yellow"
                    curMoves[col][0] -= 1
                    score = miniMax(curMoves, depth +1, False, alpha, beta)
                    board[row][col] = "."
                    curMoves[col][0] += 1

                    bestScore = max(score, bestScore)
                    alpha = max(alpha, bestScore)
                    if beta <= alpha:
                        break

        return bestScore
    else:
        bestScore = 1000
        for i in range(0,len(curMoves)):
            row = curMoves[i][0]
            col = curMoves[i][1]
            if board[row][col] == ".":
                if row >= 0:
                    board[row][col] = "Red"
                    curMoves[col][0] -= 1
                    score = miniMax(curMoves, depth +1, True, alpha, beta)
                    board[row][col] = "."
                    curMoves[col][0] += 1

                    bestScore = min(score, bestScore)
                    beta = min(bestScore, beta)
                    if beta <= alpha:
                        break
        return bestScore








def checkWin():
    global board
    retVal = [None, None]
    for row in range(0, 6):
        for i in range(0, 4):

            if (board[row][i] == board[row][i + 1] == board[row][i + 2]) and board[row][i + 3] == ".":
                retVal[1] = board[row][i]
            if (board[row][i] == board[row][i + 1] == board[row][i + 3]) and board[row][i + 2] == ".":
                retVal[1] = board[row][i]
            if (board[row][i] == board[row][i + 3] == board[row][i + 2]) and board[row][i + 1] == ".":
                retVal[1] = board[row][i]
            if (board[row][i + 3] == board[row][i + 1] == board[row][i + 2]) and board[row][i] == ".":
                retVal[1] = board[row][i+1]
            if board[row][i] != "." and (board[row][i] == board[row][i + 1] == board[row][i + 2]
                                         == board[row][i + 3]):
                retVal[0] = board[row][i]
                return retVal


    for col in range(0, 7):
        for i in range(0, 3):

            if (board[i][col] == board[i+1][col] == board[i+2][col]) and board[i+3][col] == ".":
                retVal[1] = board[i][col]
            if (board[i][col] == board[i+1][col] == board[i+3][col]) and board[i+2][col] == ".":
                retVal[1] = board[i][col]
            if (board[i][col] == board[i+3][col] == board[i+2][col]) and board[i+1][col] == ".":
                retVal[1] = board[i][col]
            if (board[i+3][col] == board[i+1][col] == board[i+2][col]) and board[i][col] == ".":
                retVal[1] = board[i+1][col]
            if board[i][col] != "." and (board[i + 1][col] == board[i + 2][col] == board[i + 3][col]
                                         == board[i][col]):
                retVal[0] = board[i][col]
                return retVal

    for row in range(0, 3):
        for col in range(0, 4):
            if (board[row][col] != ".") and (board[row][col] == board[row + 1][col + 1]
                                             == board[row + 2][col + 2] == board[row + 3][col + 3]):
                retVal[0] = board[row][col]
                return retVal

    for row in range(5, 2, -1):
        for col in range(0, 4):
            if (board[row][col] != ".") and (board[row][col] == board[row - 1][col + 1]
                                             == board[row - 2][col + 2] == board[row - 3][col + 3]):
                retVal[0] = board[row][col]
                return retVal

    isDraw = True
    for row in range(0, 6):
        for col in range(0, 7):
            if board[row][col] == ".":
                isDraw = False
                break
        if not isDraw:
            break
    if isDraw:
        return ["Draw", None]
    return [None, None]




def draw_Move(row, col):
    global board, turn, avalMoves, userTurn
    xPos = 0
    yPos = 0

    if col == 1:
        xPos = 15
    elif col == 2:
        xPos = width / 7 + 15
    elif col == 3:
        xPos = width / 7 * 2 + 15
    elif col == 4:
        xPos = width / 7 * 3 + 15
    elif col == 5:
        xPos = width / 7 * 4 + 15
    elif col == 6:
        xPos = width / 7 * 5 + 15
    elif col == 7:
        xPos = width / 7 * 6 + 15



    if avalMoves[col-1][0] >= 0:
        row = avalMoves[col-1][0]
        board[row][col-1] = turn
        row += 1
        avalMoves[col-1][0] -= 1


    if row == 1:
        yPos = 15
    elif row == 2:
        yPos = height / 6 + 15
    elif row == 3:
        yPos = height / 6 * 2 + 15
    elif row == 4:
        yPos = height / 6 * 3 + 15
    elif row == 5:
        yPos = height / 6 * 4 + 15
    elif row == 6:
        yPos = height / 6 * 5 + 15

    if turn == "Red":
        turn = "Yellow"
        screen.blit(redChip, (xPos, yPos))

    elif turn == "Yellow":
        screen.blit(yellowChip, (xPos, yPos))
        turn = "Red"
    pg.display.update()
    time.sleep(1)


def userClick():
    global board, game_state, winner
    if userTurn:
        x, y = pg.mouse.get_pos()

        for i in range(1, 8):
            if x < width / 7 * i:
                x = i
                break

        for i in range(1, 7):
            if y < height / 6 * i:
                y = i
                break

        if x and y and board[y - 1][x - 1] == ".":
            global turn
            draw_Move(y, x)
            win = checkWin()
            winner = win[0]
            draw_status()
            if(game_state == "in_bot") and winner is None:
                bestMove()
                win  = checkWin()
                winner = win[0]
                draw_status()


def reset_game():
    global board, winner, turn, draw, avalMoves
    board = [["."] * 7, ["."] * 7, ["."] * 7, ["."] * 7, ["."] * 7, ["."] * 7]
    avalMoves = [[5,0], [5,1], [5,2], [5,3], [5,4], [5,5], [5,6] ]
    winner = None
    turn = "Red"
    draw = False
    game_opening()


def draw_start_menu():
    screen.fill((0, 0, 0))
    font = pg.font.Font(None, 40)
    title = font.render('Connect 4', True, (255, 255, 255))
    start = font.render(('Two-Player (Enter)'), True, (255, 255, 255))
    computer = font.render('Computer (C)', True, (255, 255, 255))
    quitButton = font.render('Quit (Q)', True, (255, 255, 255))
    screen.blit(title, (width / 2 - title.get_width() / 2, height / 2 - title.get_height() / 2))
    screen.blit(start, (width / 2 - start.get_width() / 2, height / 2 + start.get_height() / 2))
    screen.blit(computer,
                (width / 2 - computer.get_width() / 2, height / 2 + start.get_height() + computer.get_height() / 2))
    screen.blit(quitButton, (width / 2 - quitButton.get_width() / 2,
                             height / 2 + start.get_height() + computer.get_height() + quitButton.get_height() / 2))
    pygame.display.update()


def draw_end_screen():
    global winner
    screen.fill((0,0,0))
    font = pg.font.Font(None, 40)
    font2 = pg.font.Font(None, 50)
    winMessage = font2.render((winner + " Won!"), True, (255,255,255))
    drawMessage = font2.render((winner), True, (255,255,255))
    playAgain = font.render('Play again (Y)', True, (255,255,255))
    returnToHome = font.render('Back to Home (B)', True, (255,255,255))
    if winner != "Draw":
        screen.blit(winMessage, (width/2 - winMessage.get_width()/2, height/2 - 50))
    else:
        screen.blit(drawMessage, (width/2 - drawMessage.get_width()/2, height/2 - 50))
    screen.blit(playAgain, (width/2 - playAgain.get_width()/2, height/2 - playAgain.get_height()/2+50))
    screen.blit(returnToHome, (width/2 - returnToHome.get_width()/2, height/2 + returnToHome.get_height()/2+50))
    pygame.display.update()


game_opening()

while (True):
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit()
    if game_state == "start_menu":
        draw_start_menu()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            reset_game()
            game_state = "in_game"
        if keys[pygame.K_c]:
            reset_game()
            game_state = "in_bot"
        if keys[pygame.K_q]:
            pg.quit()
            sys.exit()

    if game_state == "in_game":
        if event.type == MOUSEBUTTONDOWN:
            userClick()
            time.sleep(1)
            if (winner or draw):
                temp = game_state
                time.sleep(2)
                game_state = "end"
    if game_state == "in_bot":
        if firstPlay == "Yellow":
            bestMove()
            firstPlay = "Not"
        if event.type == MOUSEBUTTONDOWN:
            userClick()
            if (winner or draw):
                temp = game_state
                time.sleep(2)
                game_state = "end"
    if game_state == "end":
        draw_end_screen()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_b]:
            game_state = "start_menu"
        if keys[pygame.K_y]:
            reset_game()
            game_state = temp


    pg.display.update()
    CLOCK.tick(fps)