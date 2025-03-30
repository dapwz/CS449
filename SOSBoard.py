import SOSPlayer
import SOSComputer as Computer

class SOSBoard:
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

    def getBoardSize(self):
        return self.boardSize

    def changeTurn(self):
        if self.turn == self.bluePlayer:
            self.turn = self.redPlayer
        else:
            self.turn = self.bluePlayer


    def checkWin(self, moveX, moveY):  # Combined S and O win checks
        if self.getPlace(moveX, moveY) not in ('S', 'O'): #check if valid move
            return  

        # offsets for all 8 directions
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
                    (0, 1)]
        
        if self.getPlace(moveX, moveY) == 'S': #if S placed, check for O and S
            for dx, dy in directions: # Check for SOS in all directions
                try:
                    if (self.getPlace(moveX + dx, moveY + dy) == 'O' and 
                        self.getPlace(moveX + 2 * dx, moveY + 2 * dy) == 'S'):
                        if self.turn.getColor() == 'Blue':
                            self.blueScore += 1
                        else:
                            self.redScore += 1
                except IndexError: #skip invalid array values
                    continue 

        elif self.getPlace(moveX, moveY) == 'O': #if O placed, check for S on opposite sides              
            for dx, dy in directions: # Check for SOS in all directions
                try: 
                    if (self.getPlace(moveX + dx, moveY + dy) == 'S' and 
                        self.getPlace(moveX - dx, moveY - dy) == 'S'):
                        if self.turn.getColor() == 'Blue':
                            self.blueScore += 1
                        else:
                            self.redScore += 1
                except IndexError: #skip invalid array values
                    continue

    def makeMove(self, moveX, moveY):
        if self.boardArray[moveX][moveY] == ' ':
            self.boardArray[moveX][moveY] = self.getTurn().getLetter()
            self.emptySpaces -= 1
            self.checkWin(moveX, moveY)
            self.changeTurn()
            return self.checkEnd()


class SOSSimpleBoard(SOSBoard):
    def __init__(self,boardSize):
        super().__init__(boardSize)

    def checkEnd(self):
        # simple win state = blue or red score over 0, or no more spaces
        if (self.blueScore > 0 or self.redScore > 0 or self.emptySpaces ==0):
            return True
        return False


class SOSGeneralBoard(SOSBoard):
    def __init__(self,boardSize):
        super().__init__(boardSize)

    def checkEnd(self):        
     # general win state = no remaining spaces
        if self.emptySpaces == 0: 
            return True
        else:
            return False