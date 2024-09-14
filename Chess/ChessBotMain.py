import chess


#board=chess.Board()

PIECE_VALUES = [0, 100, 350, 300, 500, 900, 0] #indexes 1-5: Pawn, Knight, Bishop, Rook, Queen


def bestMove(board, myColor):
    bestScore = -100000#sets the best score to a small number so any score will be better
    bestMove = None
    for move in board.legal_moves:#iterates through all possible moves
        board.push(move)
        score = 1
        score += miniMax(0, False, -100000, 100000, board, myColor)
        board.pop()#sees what happens if the move is chosen then undos the move
        if(score >= bestScore):
            bestScore = score
            bestMove = move

    if bestMove:#chooses the best move
        #print(bestMove)
        #board.push(bestMove)
        return bestMove
    else:
        print("no move found")
        return None

def scoreBoard(board, myColor):
    scores = 0
    PIECE_VALUES = [0, 100, 350, 300, 500, 900, 0]
    for square in chess.SQUARES:#goes through all square of the board and adds the pieces left values
        piece = board.piece_at(square)
        if(piece):
            if (piece.color == myColor):
                scores += PIECE_VALUES[piece.piece_type]
            else:
                scores -= PIECE_VALUES[piece.piece_type]

    return scores


def miniMax(depth, isMaxing, alpha, beta, board, myColor):

    if board.is_game_over():
        if board.is_checkmate():#returns max points if you win or least points if you lose
            if(isMaxing):
                return 100000000
            else:
                return -100000000
        return 0
    if depth == 3:#checks 3 moves ahead
        return scoreBoard(board, myColor)






    if isMaxing:#is the bots maximize the score
        bestScore = -1000000
        for move in board.legal_moves:#checks all legal moves available for the bot
            board.push(move)
            score = miniMax(depth+1, False, alpha, beta, board, myColor)
            board.pop()

            alpha = max(alpha, score)#sets the alpha value so that if a worse move appears it will skip it
            bestScore = max(score, bestScore)#chooses the best score
            if beta <= alpha:#if the current move path isn't as good as the best one then skip it
                break

        return bestScore
    else:#not the bots turn so they want to minimize the loses
        bestScore = 10000000
        for move in board.legal_moves:
            board.push(move)
            score = miniMax(depth+1, True, alpha, beta, board, myColor)
            board.pop()


            bestScore = min(score, bestScore)
            beta = min(bestScore, beta)#sets the current max score for this path
            if beta <= alpha:
                break
        return bestScore


