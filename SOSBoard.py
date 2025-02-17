class SOSBoard:
    def __init__(self, boardSize, gameType):
        self.boardSize = int(boardSize)
        self.gameType = gameType
        self.blueScore = 0
        self.redScore = 0
        self.boardArray = [[" "]*boardSize for i in range(boardSize)]

    def printBoard(self):
        print('\nPrinting ',self.boardSize, ' x ', self.boardSize, ' board:\n')

        for i in self.boardArray:
            for j in i:
                print(j, end=" ")
            print()

    def getBlueScore(self):
        return self.blueScore
    
    def getRedScore(self):
        return self.redScore