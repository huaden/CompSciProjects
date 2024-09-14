color = input("Enter your color (B) or (W): ")
color = color.capitalize()
myColor = True
if(color.__eq__("B")):
    myColor = False

"""
while(board.is_game_over() is False):#temp code to test
print(board)
print("\n\n\n")
if(board.turn):
    bestMove()
else:

    i = 0
    for move in board.legal_moves:
        print(str(i) + ". " + str(move) + "   ", end='')
        i += 1
    moveNum = int(input("Enter your move number please: "))
    i = 0
    for move in board.legal_moves:
        if(i == moveNum):
            board.push(move)
        i += 1#

"""