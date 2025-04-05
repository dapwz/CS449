import SOSPlayer
import random
import copy

class SOSBoard:
    def __init__(self, boardSize):
        try:
            if (2 < boardSize < 17):
                self.boardSize = int(boardSize)
            else:
                self.boardSize = int(8)
        except:
            self.boardSize = int(8)


        self.bluePlayer = SOSPlayer.SOSPlayer('Blue')
        self.redPlayer = SOSPlayer.SOSPlayer('Red')
        self.blueScore = 0
        self.redScore = 0
        self.emptySpaces = self.boardSize  * self.boardSize 
        self.boardArray = [[" "]*self.boardSize for i in range(self.boardSize)]
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
            end = self.checkEnd()
            self.changeTurn()
            return end

class SOSBoardCPU(SOSBoard):
    def __init__(self,boardSize):
        super().__init__(boardSize)

    def findMove(self):
        size = self.getBoardSize()

        if self.getTurn().getColor() == 'Blue':
            oldscore = self.getBlueScore()
        else:
            oldscore = self.getRedScore()

        for letter in ['S','O']: #predict possible SOS if S or O are placed in each empty space
            emptyCells = []
            for row in range(size):
                for col in range(size):
                    tempboard = copy.deepcopy(self)
                    tempboard.getTurn().setLetter(letter)

                    if tempboard.getPlace(row,col)==' ':
                        emptyCells += [(row,col)] #track empty cells in case no SOS cannot be made

                        tempboard.makeMove(row,col)  #  Place letter in temporary board

                        if self.getTurn().getColor() == 'Blue':
                            newscore = tempboard.getBlueScore()
                        else:
                            newscore = tempboard.getRedScore()

                        if newscore > oldscore:  #check if temp move made a score
                                #print(row ,",", col ," produced a score")
                                self.getTurn().setLetter(letter) #update player letter
                                return (row, col)

        #if no SOS found in board, place random letter
        self.getTurn().setLetter(random.choice(['S','O']))
        return random.choice(emptyCells)
    
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

class SOSSimpleBoardCPU(SOSBoardCPU):
    def __init__(self,boardSize):
        super().__init__(boardSize)

    def checkEnd(self):
        # simple win state = blue or red score over 0, or no more spaces
        if (self.blueScore > 0 or self.redScore > 0 or self.emptySpaces ==0):
            return True
        return False

class SOSGeneralBoardCPU(SOSBoardCPU):
    def __init__(self,boardSize):
        super().__init__(boardSize)

    def checkEnd(self):        
     # general win state = no remaining spaces
        if self.emptySpaces == 0: 
            return True
        else:
            return False