import random
import copy

class ComputerPlayer():

    def findMove(board):
        size = board.getBoardSize()

        if board.getTurn().getColor() == 'Blue':
            oldscore = board.getBlueScore()
        else:
            oldscore = board.getRedScore()

        for letter in ['S','O']: #predict possible SOS if S or O are placed in each empty space
            emptyCells = []
            for row in range(size):
                for col in range(size):
                    tempboard = copy.deepcopy(board)
                    tempboard.getTurn().setLetter(letter)

                    if tempboard.getPlace(row,col)==' ':
                        emptyCells += [(row,col)] #track empty cells in case no SOS cannot be made

                        tempboard.makeMove(row,col)  #  Place letter in temporary board

                        if board.getTurn().getColor() == 'Blue':
                            newscore = tempboard.getBlueScore()
                        else:
                            newscore = tempboard.getRedScore()

                        if newscore > oldscore:  #check if temp move made a score
                                #print(row ,",", col ," produced a score")
                                board.getTurn().setLetter(letter) #update player letter
                                return (row, col)

        #if no SOS found in board, place random letter
        board.getTurn().setLetter(random.choice(['S','O']))
        return random.choice(emptyCells)
    
