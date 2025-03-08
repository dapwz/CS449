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

        for i in self.boardArray:
            for j in i:
                print(j, end=" ")
            print()
            
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

    def checkWin(self, player, moveX, moveY):
        # if O is placed, check for S in all 4 directions (vertical, horizontal, diagonal x2)
        if self.getPlace(moveX, moveY) == 'O':
            # loop through one side (horizontal and diagonal x2)
            for x in range(moveX-1, moveX+1):
                if self.getPlace(x, moveY) == 'S':
                    if self.getPlace(moveX+(moveX-x), moveY) == 'S':
                        # win state?
                        if player == 'Blue':
                            self.blueScore += 1
                        else:
                            self.redScore += 1

            if self.getPlace(moveX, moveY+1) == 'S':  # check vertical
                if self.getPlace(moveX, moveY-1) == 'S':
                    # win state?
                    if player == 'Blue':
                        self.blueScore += 1
                    else:
                        self.redScore += 1

        if self.getPlace(moveX, moveY) == 'S':  # check all 8 directions
            for x in range(moveX-1, moveX+2):
                for y in range(moveY-1, moveY+2):
                    if (x != moveX or y != moveY) and self.getPlace(x, y) == 'O':
                        if self.getPlace(x+(x-moveX), y+(y-moveY)) == 'S':
                            # win state?
                            if player == 'Blue':
                                self.blueScore += 1
                            else:
                                self.redScore += 1

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
    def checkWin(self,player, moveX, moveY):
        # if O is placed, check for S in all 4 directions (vertical, horizontal, diagonal x2)
        if self.getPlace(moveX, moveY) == 'O':
            # loop through one side (horizontal and diagonal x2)
            for x in range(moveX-1, moveX+1):
                if self.getPlace(x, moveY) == 'S':
                    if self.getPlace(moveX+(moveX-x), moveY) == 'S':
                        # win state?
                        if player == 'Blue':
                            self.blueScore += 1
                        else:
                            self.redScore += 1

            if self.getPlace(moveX, moveY+1) == 'S':  # check vertical
                if self.getPlace(moveX, moveY-1) == 'S':
                    # win state?
                    if player == 'Blue':
                        self.blueScore += 1
                    else:
                        self.redScore += 1

        if self.getPlace(moveX, moveY) == 'S':  # check all 8 directions
            for x in range(moveX-1, moveX+2):
                for y in range(moveY-1, moveY+2):
                    if (x != moveX or y != moveY) and self.getPlace(x, y) == 'O':
                        if self.getPlace(x+(x-moveX), y+(y-moveY)) == 'S':
                            # win state?
                            if player == 'Blue':
                                self.blueScore += 1
                            else:
                                self.redScore += 1
     # general win state = no remaining spaces
        if self.emptySpaces == 0: 
            return True

        return False