from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os
from dotenv import load_dotenv

load_dotenv()

import pyautogui

import time

import chess
from ChessBotMain import miniMax,scoreBoard,bestMove


pyautogui.size()

service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://lichess.org/")
driver.maximize_window()


username = os.getenv("username")
password = os.getenv("password")

driver.find_element(By.XPATH, '/html[1]/body[1]/header[1]/div[2]/a[1]').click()
time.sleep(2)

driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/main[1]/form[1]/div[1]/div[1]/input[1]').send_keys(username)#writes my username
driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/main[1]/form[1]/div[1]/div[2]/div[1]/input[1]').send_keys(password)#writes my password
time.sleep(2)

driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/main[1]/form[1]/div[1]/button[1]').click()#clicks the login button
time.sleep(2)
#opens lichess and logins in to the bot account







goTo_URL = input("Copy the url of the game please: ")
driver.get(goTo_URL)#goes to the game I want to go to

Icolor = input("Enter your color (B) or (W): ")
Icolor = Icolor.capitalize()
myColor = True
color = chess.WHITE
if(Icolor.__eq__("B")):
    myColor = False
    color = chess.BLACK




moves = []
board=chess.Board()
PIECE_VALUES = [0, 100, 350, 300, 500, 900, 0] #indexes 1-5: Pawn, Knight, Bishop, Rook, Queen




rows = [('a', 480), ('b', 540), ('c', 600), ('d', 660), ('e', 720), ('f', 790), ('g', 850), ('h', 910)]#pixel values of squares from left to right
columns = [('1', 690), ('2', 630), ('3', 570), ('4', 510), ('5', 440), ('6', 380), ('7', 320), ('8', 260)]#pixel values from bottom to top
if(myColor == False):
    rows = [('h', 480), ('g', 540), ('f', 600), ('e', 660), ('d', 720), ('c', 790), ('b', 850), ('a', 910)]
    columns = [('8', 690), ('7', 630), ('6', 570), ('5', 510), ('4', 440), ('3', 380), ('2', 320),('1', 260)]




def get_lastMove(prevMove):
    lastMove = driver.find_element(By.CSS_SELECTOR, '.a1t').get_attribute('innerHTML')#gets the last move from the game


    if(not lastMove.__eq__(prevMove)):#if it is a new move add it the board
        move_text = lastMove

        move = board.parse_san(move_text)
        moves.append(lastMove)
        board.push(move)
        print("Last Move: " + move.uci())
    return lastMove



def getPixelVal(val, arr):#matches the pixel values to the move value i.e. e = 720 or 660
    for item in arr:
        if(val == item[0]):
            return item[1]
    return None

def clickMove(sugMoveUCI):
    firstClick = (sugMoveUCI[0:1], sugMoveUCI[1:2]) 
    secondClick = (sugMoveUCI[2:3], sugMoveUCI[3:4])#seperates the move into the curPos of the piece then where the piece is moving

    firstX = getPixelVal(firstClick[0], rows)
    firstY = getPixelVal(firstClick[1], columns)
    #gets the cur position of the piece

    secX = getPixelVal(secondClick[0], rows)
    secY = getPixelVal(secondClick[1], columns)
    #gets the square where the peice is going
    

    pyautogui.moveTo(firstX,firstY)
    pyautogui.click()
    time.sleep(.5)
    pyautogui.moveTo(secX, secY)
    pyautogui.click()
    time.sleep(.5)
    #moves the piece
    if(len(sugMoveUCI) > 4):#if promoting a pawn, make sure to click on queen
        pyautogui.click()


prevMove = ""


if(myColor):#automatic first move for white, selects e4
    move = board.parse_san("e4")
    moves.append(move)
    board.push(move)
    prevMove = "e4"
    print("Suggested move: " + move.uci())
    time.sleep(3)
    clickMove(move.uci())





while(board.is_game_over() is False):

    prevMove = get_lastMove(prevMove)#sets the previous move to the last move to determine whose turn it is and upate the board if the other player has moved

    if(board.turn == myColor):#if it is my turn, find the best move

        prevMove = bestMove(board, color)#gets the best move
        san_text = board.san(prevMove)
        board.push(prevMove)#adds it to the board
        #prevMove = board.san(prevMove)#updates the last move
        sugMoveUCI = prevMove.uci()
        print("Suggested move: " + sugMoveUCI)
        clickMove(sugMoveUCI)
        prevMove = san_text
        

        
        
    
    
    time.sleep(2)
    