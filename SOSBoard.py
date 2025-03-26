import SOSPlayer

class SOSSimpleBoard:
    def __init__(self, boardSize):
        try:
            if (2 < boardSize < 17):
                self.boardSize = int(boardSize)
            else:
                self.boardSize = int(8)
        except:
            self.boardSize = int(8)

        self.emptySpaces = self.boardSize  * self.boardSize 
        self.redPlayer = SOSPlayer.SOSPlayer('Red', 'Human', 'S')
        self.bluePlayer = SOSPlayer.SOSPlayer('Blue', 'Human', 'S')
        self.blueScore = 0
        self.redScore = 0
        self.boardArray = [[" "]*boardSize for i in range(self.boardSize)]
        self.turn = self.bluePlayer

    def resetBoard(self, size):
        self.__init__(size)

    def getBlueScore(self):
        return self.blueScore

    def getRedScore(self):
        return self.redScore

    def getBluePlayer(self):
        return self.bluePlayer

    def getRedPlayer(self):
        return self.redPlayer
    
    def getTurn(self):
        return self.turn
    
    def getPlace(self, X, Y):
        try:
            if 0 <= X <= (self.boardSize) and 0 <= Y <= (self.boardSize):
                return self.boardArray[X][Y]
            else:
                return ' '
        except:
            return ' '


    def changeTurn(self):
        if self.turn == self.bluePlayer:
            self.turn = self.redPlayer
        else:
            self.turn = self.bluePlayer

    def checkforSWin(self,moveX,moveY):
        for x in range(moveX-1, moveX+2):
                for y in range(moveY-1, moveY+2):
                    if (x != moveX or y != moveY) and self.getPlace(x, y) == 'O':
                        if self.getPlace(x+(x-moveX), y+(y-moveY)) == 'S':
                            if self.turn.getColor() == 'Blue':
                                self.blueScore += 1
                            else:
                                self.redScore += 1 

    def checkforOWin(self, moveX, moveY):
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1)]
        for dx, dy in directions:
            # Check if there's an 'S' before and after the placed 'O'
            if self.getPlace(moveX + dx, moveY + dy) == 'S' and self.getPlace(moveX - dx, moveY - dy) == 'S':
                if self.turn.getColor() == 'Blue':
                    self.blueScore += 1
                else:
                    self.redScore += 1

    def checkWin(self, moveX, moveY):
        if self.getPlace(moveX, moveY) == 'O':
            self.checkforOWin(moveX,moveY)
        elif self.getPlace(moveX, moveY) == 'S': 
            self.checkforSWin(moveX,moveY)
    
    def checkEnd(self):
        # simple win state = blue or red score over 0, or no more spaces
        if (self.blueScore > 0 or self.redScore > 0 or self.emptySpaces ==0):
            return True
        return False

    def makeMove(self, moveX, moveY):
        if self.boardArray[moveX][moveY] == ' ':
            self.boardArray[moveX][moveY] = self.getTurn().getLetter()
            self.emptySpaces -= 1
            self.checkWin(moveX, moveY)
            return self.checkEnd()
        
class SOSGeneralBoard(SOSSimpleBoard):
    def checkEnd(self):        
     # general win state = no remaining spaces
        if self.emptySpaces == 0: 
            return True
        else:
            return False