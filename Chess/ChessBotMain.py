import chess


board=chess.Board()

PIECE_VALUES = [0, 100, 350, 300, 500, 900, 0] #indexes 1-5: Pawn, Knight, Bishop, Rook, Queen


def bestMove():
    bestScore = -100000
    bestMove = None
    for move in board.legal_moves:
        board.push(move)
        score = 1
        score += miniMax(0, False, -100000, 100000)
        board.pop()
        if(score >= bestScore):
            bestScore = score
            bestMove = move
    if bestMove:
        board.push(bestMove)
    else:
        print("no move found")

def scoreBoard():
    scores = 0
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if(piece):
            if (piece.color):
                scores += PIECE_VALUES[piece.piece_type]
            else:
                scores -= PIECE_VALUES[piece.piece_type]

    return scores


def miniMax(depth, isMaxing, alpha, beta):
    if board.is_game_over():
        if(board.is_checkmate):
            if(isMaxing):
                return 100000000
            else:
                return -100000000
        return 0
    if depth == 4:
        return scoreBoard()

    if isMaxing:
        bestScore = -1000000
        for move in board.legal_moves:
            board.push(move)
            score = miniMax(depth+1, False, alpha, beta)
            board.pop()

            alpha = max(alpha, beta)
            bestScore = max(score, bestScore)
            if beta <= alpha:
                break

        return bestScore
    else:
        bestScore = 10000000
        for move in board.legal_moves:
            board.push(move)
            score = miniMax(depth+1, True, alpha, beta)
            board.pop()


            bestScore = min(score, bestScore)
            beta = min(bestScore, beta)
            if beta <= alpha:
                break
        return bestScore



while(board.is_game_over() is False):
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
            i += 1
