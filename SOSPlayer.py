class SOSPlayer:
    def __init__(self, PlayerColor, PlayerType, PlayerLetter):
        self.PlayerLetter = PlayerLetter
        self.PlayerColor = PlayerColor
        self.PlayerType = PlayerType
        
    def getLetter(self):
        return self.PlayerLetter
    
    def getColor(self):
        return self.PlayerColor
    
    def getType(self):
        return self.PlayerType
    
    def setLetter(self,PlayerLetter):
        self.PlayerLetter = PlayerLetter

    def setColor(self,PlayerColor):
        self.PlayerColor = PlayerColor

    def setType(self,PlayerType):
        self.PlayerType = PlayerType