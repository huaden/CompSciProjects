#Name: Hayden Robinette
#Last Date Updated: Feb 3, 2024
#Purpose: Tic Tac Toe game with a bot mode and two player mode

import pygame as pg,sys
import pygame.display
from pygame.locals import*
import time

game_state = "start_menu"
XO = 'x'
winner = None
draw = False
width = 400
height = 400
white = (255,255,255)
lineColor = (10,10,10)
userTurn = True
xWins = 0
oWins = 0
drawCount = 0
TTT = [[None]*3, [None]*3, [None]*3]

pg.init()
fps = 30
CLOCK = pg.time.Clock()
screen = pg.display.set_mode((width, height+100), 0, 32)
pg.display.set_caption("Tic Tac Toe")

opening = pg.image.load('opening.png')
x_img = pg.image.load('xImage.png')
o_img = pg.image.load('oImage.png')


opening = pg.transform.scale(opening, (width, height+100))
x_img = pg.transform.scale(x_img, (80, 80))
o_img = pg.transform.scale(o_img, (80, 80))



def game_opening():
    screen.blit(opening, (0,0))
    pg.display.update()
    time.sleep(1)
    draw_lines()
    draw_status()

def draw_lines():
    screen.fill(white)
    pg.draw.line(screen, lineColor, (width/3,0), (width/3, height), 10)
    pg.draw.line(screen, lineColor, (width/3*2, 0), (width/3*2, height), 10)
    pg.draw.line(screen, lineColor, (0, height/3), (width, height/3), 10)
    pg.draw.line(screen, lineColor, (0, height/3*2), (width, height/3*2), 10)

def bot_move():
    global XO, TTT, userTurn
    botX = -1
    botY = -1

    if(TTT[1][0] == None):
        botX = 1
        botY = 0
    if(TTT[2][0] == None and TTT[1][1] == 'x'):
        botX = 2
        botY = 0
    if(TTT[2][0] == 'o' and TTT[0][2] == 'x' and TTT[2][2] == None):
        botX = 2
        botY = 2

    for row in range(0,3):
        if(((TTT[row][0] == TTT[row][1] and TTT[row][0] is not None and TTT[row][2] == None) or (TTT[row][1] == TTT[row][2] and TTT[row][1] is not None and TTT[row][0] == None)
                or (TTT[row][0] == TTT[row][2] and TTT[row][0] is not None and TTT[row][1] == None))):
            if(TTT[row][0] == None):
                botX = row
                botY = 0
            elif(TTT[row][1]== None):
                botX = row
                botY = 1
            else:
                botX = row
                botY = 2

    for col in range(0,3):
        if((TTT[0][col] == TTT[1][col] and TTT[0][col] is not None and TTT[2][col] == None) or (TTT[1][col] == TTT[2][col] and TTT[1][col] is not None and TTT[0][col] == None)
                or (TTT[0][col] == TTT[2][col] and TTT[0][col] is not None and TTT[1][col] == None)):
            if(TTT[0][col] == None):
                botX = 0
                botY = col
            elif(TTT[1][col]== None):
                botX = 1
                botY = col
            else:
                botX = 2
                botY = col

    if((TTT[0][0] == TTT[1][1] and TTT[0][0] is not None and TTT[2][2] == None) or (TTT[1][1] == TTT[2][2] and TTT[0][0] is None and TTT[1][1] is not None)
            or (TTT[0][0] == TTT[2][2] and TTT[0][0] is not None and TTT[1][1] == None) ):
        if(TTT[0][0] == None):
            botX = 0
            botY = 0
        if(TTT[2][2] == None):
            botX = 2
            botY = 2

    if((TTT[2][0] == TTT[1][1] and TTT[2][0] is not None and TTT[0][2] == None) or (TTT[1][1] == TTT[0][2] and TTT[1][1] is not None and TTT[2][0] == None)
            or (TTT[2][0] == TTT[0][2] and TTT[2][0] is not None and TTT[1][1] == None)):
        if(TTT[2][0] == None):
            botX = 2
            botY = 0
        if(TTT[0][2] == None):
            botX = 0
            botY = 2



    if(TTT[1][1] == None):
        botX = 1
        botY = 1

    if(botX == -1):
        for row in range(0,3):
            for col in range(0,3):
                if TTT[row][col] == None:
                    botX = row
                    botY = col


    if TTT[botX][botY] is None:
        global XO
        time.sleep(1)
        drawX0(botX+1, botY+1)


def draw_status():
    global draw, xWins, oWins
    if winner is None:
        message = XO.upper() + "'s Turn"
    else:
        message = winner.upper() + " won!"
    if draw:
        message = "Game Draw"

    font = pg.font.Font(None, 30)
    text = font.render(message, 1, (255,255,255))
    xCount = font.render("X: " + str(xWins), 1, (255,255,255))
    oCount = font.render("O: " + str(oWins), 1, (255,255,255))

    screen.fill((0,0,0), (0,400, 500, 100))
    text_rect = text.get_rect(center=(width/2, 500-50))
    screen.blit(text, text_rect)
    screen.blit(xCount, (width/5 - xCount.get_width()/2, 500-50))
    screen.blit(oCount, (width/5*4 - xCount.get_width()/2, 500-50))
    pg.display.update()

def check_win():
    global TTT, winner, draw, xWins, oWins, drawCount

    for row in range(0,3):
        if((TTT[row][0] == TTT[row][1] == TTT[row][2]) and TTT[row][0] is not None):
            winner = TTT[row][0]
            if(winner == 'x'):
                xWins += 1
            else:
                oWins += 1
            pg.draw.line(screen, (250, 0, 0), (0,(row+1)*height/3 - height/6),
                         (width, (row+1)*height/3 - height/6), 5)
            break
    for col in range(0,3):
        if((TTT[0][col] == TTT[1][col] == TTT[2][col]) and TTT[0][col] is not None):
            winner = TTT[0][col]
            if(winner == 'x'):
                xWins += 1
            else:
                oWins += 1
            pg.draw.line(screen, (250, 0, 0), (((col+1)*width/3 - width/6), 0),
                         (((col+1)*width/3 - width/6), height), 5)
            break
    if((TTT[0][0] == TTT[1][1] == TTT[2][2] ) and TTT[0][0] is not None):
        winner = TTT[0][0]
        if(winner == 'x'):
            xWins += 1
        else:
            oWins += 1
        pg.draw.line(screen, (250,0,0), (50,50), (350, 350), 5)

    if(TTT[2][0] == TTT[1][1] == TTT[0][2] and TTT[1][1] is not None):
        winner = TTT[1][1]
        if(winner == 'x'):
            xWins += 1
        else:
            oWins += 1
        pg.draw.line(screen, (250, 0,0), (350, 50), (50,350), 5)

    if(all([all(row) for row in TTT]) and winner is None):
        draw = True
        drawCount += 1
    draw_status()

def drawX0(row, col):
    global TTT, XO, userTurn
    if row==1:
        xPos = 30
    if row==2:
        xPos = width/3+30
    if row==3:
        xPos = width/3*2 + 30

    if col==1:
        yPos = 30
    if col==2:
        yPos = height/3+30
    if col==3:
        yPos = height/3*2 + 30

    TTT[row-1][col-1] = XO
    if XO == 'x':
        XO = 'o'
        screen.blit(x_img, (yPos, xPos))
    else:
        XO = 'x'
        screen.blit(o_img, (yPos, xPos))

    pg.display.update()


def userClick():
    global TTT, game_state, userTurn, winner
    if(userTurn):
        x,y = pg.mouse.get_pos()

        if(x < width/3):
            x = 1
        elif(x < width/3*2):
            x = 2
        elif(x < width):
            x = 3
        else:
            x = None
        if(y < height/3):
            y = 1
        elif(y < height/3*2):
            y = 2
        elif(y < height):
            y = 3
        else:
            y = None

        if x and y and TTT[y - 1][x - 1] is None:
            global XO
            drawX0(y, x)
            check_win()
            if(game_state == "bot" and (not winner and not draw)):
                bot_move()
                check_win()

def reset_game():
    global TTT, XO, winner, draw
    time.sleep(1)
    XO = 'x'
    draw = False
    winner = None
    game_opening()
    TTT = [[None]*3, [None]*3, [None]*3]

def resetCounters():
    global xWins,oWins,drawCount
    xWins = 0
    oWins = 0
    drawCount = 0

def draw_start_menu():
    global xWins, oWins, drawCount
    screen.fill((0,0,0))
    font = pg.font.Font(None, 40)
    title = font.render('Tic Tac Toe', True, (255,255,255))
    start = font.render(('Two-Player (Enter)'), True, (255,255,255))
    computer = font.render('Computer (C)', True, (255,255,255))
    quitButton = font.render('Quit (Q)', True, (255,255,255))
    screen.blit(title, (width/2-title.get_width()/2, height/2 - title.get_height()/2))
    screen.blit(start, (width/2-start.get_width()/2, height/2 + start.get_height()/2))
    screen.blit(computer, (width/2 - computer.get_width()/2, height/2+start.get_height()+computer.get_height()/2))
    screen.blit(quitButton, (width/2 -quitButton.get_width()/2, height/2+start.get_height()+computer.get_height()+quitButton.get_height()/2))
    pygame.display.update()

def draw_end_screen():
    screen.fill((0,0,0))
    font = pg.font.Font(None, 50)
    playAgain = font.render('Play again (Y)', True, (255,255,255))
    returnToHome = font.render('Back to Home (B)', True, (255,255,255))
    screen.blit(playAgain, (width/2 - playAgain.get_width()/2, height/2 - playAgain.get_height()/2))
    screen.blit(returnToHome, (width/2 - returnToHome.get_width()/2, height/2 + returnToHome.get_height()/2))
    pygame.display.update()





game_opening()
temp = ""
while(True):
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
            game_state = "bot"
        if keys[pygame.K_q]:
            pg.quit()
            sys.exit()
    if game_state == "in_game":
        if(event.type == MOUSEBUTTONDOWN):
            userClick()
            if(winner or draw):
                temp = game_state
                time.sleep(
                game_state = "end"
    if game_state == "bot":
        if event.type == MOUSEBUTTONDOWN and userTurn == True:
            userClick()
            if(winner or draw):
                temp = game_state
                time.sleep(2)
                game_state = "end"
    if game_state == "end":
        draw_end_screen()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_b]:
            game_state = "start_menu"
            resetCounters()
        if keys[pygame.K_y]:
            reset_game()
            game_state = temp

    pg.display.update()
    CLOCK.tick(fps)













