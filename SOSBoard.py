class SOSBoard:
    def __init__(self, boardSize, gameType):
        self.boardSize = int(boardSize)
        self.emptySpaces = self.boardSize * self.boardSize
        self.gameType = gameType
        self.blueScore = 0
        self.redScore = 0
        self.boardArray = [[" "]*boardSize for i in range(boardSize)]

    def printBoard(self):
        print('Printing ', self.boardSize,
              ' x ', self.boardSize, ' board:')

        for i in self.boardArray:
            for j in i:
                print(j, end=" ")
            print()

    def getBlueScore(self):
        return self.blueScore

    def getRedScore(self):
        return self.redScore

    def getPlace(self, X, Y):
        if 0<=X<=(self.boardSize)  and 0<=Y<=(self.boardSize):
            return self.boardArray[X-1][Y-1]
        else:
            return ' '

    def checkWin(self, player, moveX, moveY):
        if self.getPlace(moveX,moveY) == 'O': # if O is placed, check for S in all 4 directions (vertical, horizontal, diagonal x2)
            for x in range(moveX-1, moveX+1): #loop through one side (horizontal and diagonal x2)
                if self.getPlace(x, moveY) == 'S':
                        if self.getPlace(moveX+(moveX-x),moveY) == 'S':
                            # win state?
                            if player == 'Blue':
                                self.blueScore += 1
                            else:
                                self.redScore += 1

            if self.getPlace(moveX, moveY+1) == 'S': #check vertical
                        if self.getPlace(moveX,moveY-1) == 'S':
                            # win state?
                            if player == 'Blue':
                                self.blueScore += 1
                            else:
                                self.redScore += 1

        if self.getPlace(moveX,moveY) == 'S': #check all 8 directions
            for x in range(moveX-1, moveX+2):
                for y in range(moveY-1, moveY+2):
                    if (x != moveX or y != moveY) and self.getPlace(x, y) == 'O':
                        if self.getPlace(x+(x-moveX),y+(y-moveY)) == 'S':
                            # win state?
                            if player == 'Blue':
                                self.blueScore += 1
                            else:
                                self.redScore += 1                        
                        

                

        if self.gameType == 'Simple' and (self.blueScore > 0 or self.redScore > 0): # simple win state = blue or red score over 0
            return True

        if self.gameType == 'General' and self.emptySpaces == 0: #general win state = no remaining spaces
            return True
        
        return False

    def makeMove(self, player, letter, moveX, moveY):
        arrayX = moveX - 1
        arrayY = moveY - 1
        if self.boardArray[arrayX][arrayY] != ' ':
            print("Error: ", moveX, ",", moveX, ' already occupied.')
        else:
            self.boardArray[arrayX][arrayY] = letter
            self.emptySpaces -= 1
            #print(player,' setting ', letter, ' @ ',moveX,',',moveY)
            return self.checkWin(player, moveX, moveY)
