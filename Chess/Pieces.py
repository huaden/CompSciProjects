curBoard = [[False]*8, [False]*8, [False]*8, [False]*8, [False]*8, [False]*8, [False]*8, [False]*8]

class Pawn:
    def __int__(self, pos, captured, ):
        self.pos = pos
        self.captured = False
        self.avalMovePawn = [[self.pos[0]-2, self.pos[1]], [self.pos[0]-1, self.pos[1]], [None, None], [None, None]]
        #index 0 = double square move, index 1 = just move forward one, index 2 = capture up and to the right,
        # index 3 = capture up and to the left



    def move(self, whatMv):
        if self.avalMovePawn[whatMv][0] is not None:
            self.pos = self.avalMovePawn[whatMv]



    def getAvalMovesPawn(self):
        row = self.pos[0]
        col = self.pos[1]
        if row > 0 and col < 8:
            if row == 6:
                self.avalMovePawn[0] = [self.pos[0]-2, self.pos[1]]
            self.avalMovePawn[1] = [self.pos[0]-1, self.pos[1]]
            if curBoard[row - 1][col + 1]:
                self.avalMovePawn[2] = [row-1, col+1]
            if curBoard[row-1][col-1]:
                self.avalMovePawn[3] = [row-1, col-1]

        return self.avalMovePawn



class Rook:
    def __int__(self, pos, captured):
        self.pos = pos
        self.captured = False
        self.avalMoveRookVert = [[None, self.pos[1]]*8]
        self.avalMoveRookHorz = [[None, self.pos[1]]*8]

    def move(self, whatMv, vert):
        if vert:
            if self.avalMoveRookVert[whatMv] is not None:
                self.pos = self.avalMoveRookVert[whatMv]
        else:
            if self.avalMoveRookHorz[whatMv] is not None:
                self.pos = self.avalMoveRookHorz[whatMv]

    def getAvalMoveRookVert(self):
        row = self.pos[0]
        col = self.pos[1]
        tempR = row
        if row >= 0 and col < 8:
            while tempR >= 0:
                if curBoard[tempR][col]:
                    self.avalMoveRookVert[tempR] = [tempR, col]
                else:
                    break
            tempR = row
            while tempR < 8:
                if curBoard[tempR][col]:
                    self.avalMoveRookVert[tempR] = [tempR, col]
                else:
                    break

        return self.avalMoveRookVert

    def getAvalMoveRookHorz(self):
        row = self.pos[0]
        col = self.pos[1]
        tempC = col
        if row >= 0 and col < 8:
            while tempC >= 0:
                if curBoard[row][tempC]:
                    self.avalMoveRookHorz[row] = [row, tempC]
                else:
                    break
            tempC = col
            while tempC < 8:
                if curBoard[row][tempC]:
                    self.avalMoveRookHorz[row] = [row, tempC]
                else:
                    break
        return self.avalMoveRookHorz




