import SOSBoard

Boardsize = 3
GameType = 'General'

print('\nInitializing ',GameType,' ', Boardsize, ' x ', Boardsize)
gameBoard = SOSBoard.SOSBoard(Boardsize, GameType)

#simple win state
winState = gameBoard.makeMove('Blue','S',2,1)
winState = gameBoard.makeMove('Red','S',2,3)
winState = gameBoard.makeMove('Blue','O',2,2)
if GameType == 'Simple':
    gameBoard.printBoard()
    print('Game Score( Red: ', gameBoard.getRedScore(),', Blue: ', gameBoard.getBlueScore(), ' ) ', winState)
    exit()

#general win sate
gameBoard.printBoard()
gameBoard.printBoard()
print('Game Score (Red: ', gameBoard.getRedScore(),', Blue: ', gameBoard.getBlueScore(), ') ', winState)

winState = gameBoard.makeMove('Blue','S',1,1)
gameBoard.printBoard()
print('Game Score (Red: ', gameBoard.getRedScore(),', Blue: ', gameBoard.getBlueScore(), ') ', winState)

winState = gameBoard.makeMove('Red','O',1,2)
gameBoard.printBoard()
print('Game Score (Red: ', gameBoard.getRedScore(),', Blue: ', gameBoard.getBlueScore(), ') ', winState)


winState = gameBoard.makeMove('Blue','S',1,3)
gameBoard.printBoard()
print('Game Score (Red: ', gameBoard.getRedScore(),', Blue: ', gameBoard.getBlueScore(), ') ', winState)

winState = gameBoard.makeMove('Blue','S',3,1)
gameBoard.printBoard()
print('Game Score (Red: ', gameBoard.getRedScore(),', Blue: ', gameBoard.getBlueScore(), ') ', winState)

winState = gameBoard.makeMove('Red','O',3,2)
gameBoard.printBoard()
print('Game Score (Red: ', gameBoard.getRedScore(),', Blue: ', gameBoard.getBlueScore(), ') ', winState)

winState = gameBoard.makeMove('Blue','S',3,3)
gameBoard.printBoard()
print('Game Score (Red: ', gameBoard.getRedScore(),', Blue: ', gameBoard.getBlueScore(), ') ', winState)
