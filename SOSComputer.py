import random

class ComputerPlayer():

    def findMove(self,board):
        size = board.getboardsize()
        for letter in ['S','O']: #predict possible SOS if S or O are placed in each empty space

            for row in range(size):
                for col in range(size):
                    if board[row][col] == ' ':  # Empty cell
                        emptyCells += (row,col) #track empty cells in case no SOS can be made
                        board[row][col] = letter  # Temporarily place letter
                        if self.check_sos(board, row, col):
                            board[row][col] = ' '  # Undo the move
                            return row, col, letter
                        board[row][col] = ' '  # Undo the move
        
        #if no SOS found in board, place random letter
        return random.choice(emptyCells), random.choice(['S','O'])
    
    def checkSOS(board,row,col):
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
                    (0, 1), (1, -1), (1, 0), (1, 1)]
        for dr, dc in directions:
            try:
                if (0 <= row + 2 * dr < 8 and 0 <= col + 2 * dc < 8 and
                    board[row][col] == 'S' and
                    board[row + dr][col + dc] == 'O' and
                    board[row + 2 * dr][col + 2 * dc] == 'S'):
                    return True
            except IndexError:
                continue
        return False
    

