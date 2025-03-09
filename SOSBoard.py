class SOSSimpleBoard:
    def __init__(self, boardSize):
        if (2 < boardSize < 17):
            self.boardSize = int(boardSize)
        else:
            self.boardSize = int(8)
        self.emptySpaces = self.boardSize * self.boardSize 
        #self.gameType = gameType #change to inheritance model
        self.blueScore = 0
        self.redScore = 0
        self.boardArray = [[" "]*boardSize for i in range(boardSize)]
        self.turn = 'Blue'

    def printBoard(self):
        print('Printing ', self.boardSize,
              ' x ', self.boardSize, ' board:')

    def setBoardSize(self,size):
        self.boardSize = int(size)
        self.boardArray = [[" "]*size for i in range(size)]

    def getBlueScore(self):
        return self.blueScore

    def getRedScore(self):
        return self.redScore

    def getPlace(self, X, Y):
        if 0 <= X <= (self.boardSize) and 0 <= Y <= (self.boardSize):
            return self.boardArray[X-1][Y-1]
        else:
            return ' '

    def checkforSWin(self,player,moveX,moveY):
        for x in range(moveX-1, moveX+2):
                for y in range(moveY-1, moveY+2):
                    if (x != moveX or y != moveY) and self.getPlace(x, y) == 'O':
                        if self.getPlace(x+(x-moveX), y+(y-moveY)) == 'S':
                            if player == 'Blue':
                                self.blueScore += 1
                            else:
                                self.redScore += 1


    def checkforOWin(self,player,moveX,moveY):
        # loop through one side (horizontal and diagonal x2)
        for x in range(moveX-1, moveX+1):
            if self.getPlace(x, moveY) == 'S':
                if self.getPlace(moveX+(moveX-x), moveY) == 'S':
                    if player == 'Blue':
                        self.blueScore += 1
                    else:
                        self.redScore += 1

        else:
            return False

    def checkWin(self, player, moveX, moveY):
        if self.getPlace(moveX, moveY) == 'O':
            self.checkforOWin(player,moveX,moveY)
        elif self.getPlace(moveX, moveY) == 'S': 
            self.checkforSWin(player,moveX,moveY)

        # simple win state = blue or red score over 0, or no more spaces
        if (self.blueScore > 0 or self.redScore > 0 or self.emptySpaces ==0):
            return True
        return False

    def makeMove(self, player, letter, moveX, moveY):
        arrayX = moveX - 1
        arrayY = moveY - 1
        if self.boardArray[arrayX][arrayY] == ' ':
            #print("Error: ", moveX, ",", moveX, ' already occupied.')
            self.boardArray[arrayX][arrayY] = letter
            self.emptySpaces -= 1
            # print(player,' setting ', letter, ' @ ',moveX,',',moveY)
            return self.checkWin(player, moveX, moveY)
        
class SOSGeneralBoard(SOSSimpleBoard):
    def checkWin(self, player, moveX, moveY):
        if self.getPlace(moveX, moveY) == 'O':
            self.checkforOWin(player,moveX,moveY)
        elif self.getPlace(moveX, moveY) == 'S': 
            self.checkforSWin(player,moveX,moveY)
            
     # general win state = no remaining spaces
        if self.emptySpaces == 0: 
            return True

        return False