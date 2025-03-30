import tkinter as tk
import SOSBoard
import SOSComputer as computer

def onButtonClick(btn, btnBoard, TurnText,gameBoard, x, y):

    if gameBoard.getPlace(x, y) == " ":
        letter = gameBoard.getTurn().getLetter()
        result = gameBoard.makeMove(x, y)
        blueScore = gameBoard.getBlueScore()
        redScore = gameBoard.getRedScore()
        btn.config(text=letter)
        if result == True: #game over, report winner
            if blueScore > redScore :
                TurnText.config(text=("Blue Player Wins! (" + str(blueScore) + "|" + str(redScore) + ")"))
            elif(blueScore < redScore ):
                TurnText.config(text=("Red Player Wins! ("+str(redScore)+"|"+str(blueScore)+ ")"))
            else:
                TurnText.config(text=("Tie Game. ("+str(redScore)+"|"+str(blueScore)+")"))

        else:  
            if(gameBoard.getTurn().getColor() == 'Blue'):
                TurnText.config(text="Current turn: Blue") #update GUI
            else:
                TurnText.config(text="Current turn: Red") #update GUI

def computerMove(btnBoard,TurnText,gameBoard):
    if checkComputer(gameBoard):
        x,y = computer.ComputerPlayer.findMove(gameBoard)
        computerbtn = btnBoard[x][y]
        onButtonClick(computerbtn,btnBoard,TurnText,gameBoard,x,y)


def checkComputer(gameBoard):
    if gameBoard.getTurn().getType() == 'Computer':
        return True
    else:
        return False

def InitializeGameBoard(CenterFrame):
    gameBoard = SOSBoard.SOSSimpleBoard(8) #start with default board
    StartNewGame(gameBoard,CenterFrame,8,'Simple')
    return gameBoard

def StartNewGame(gameBoard, CenterFrame, size, type):
    size = SizeCheck(size)
    for widget in CenterFrame.winfo_children():#clear center frame before drawing new board
        widget.destroy()

    if type == 'Simple':
        gameBoard.__class__ = SOSBoard.SOSSimpleBoard  # Change class to Simple
    else:
        gameBoard.__class__ = SOSBoard.SOSGeneralBoard  # Change class to General

    gameBoard.resetBoard(size)

    Board = [[[] for _ in range(size)] for _ in range(size)]
    TurnText = tk.Label(CenterFrame, text="Current turn: Blue")

    for row in range(size):
        for col in range(size):
            btn = tk.Button(
                CenterFrame,
                text=" ",
                width=1,
                height=1,
                background="White"
            )
            btn.bind('<Button-1>', lambda event,
                     btn=btn, gameBoard=gameBoard,
                     row=row, col=col, Board=Board: [onButtonClick(btn,Board,TurnText, gameBoard, row, col), computerMove(Board,TurnText,gameBoard)])

            btn.grid(row=row, column=col, padx=(1, 0),
                     ipadx=4, ipady=1, sticky="NWSE")
            Board[row][col] = btn

    TurnText.grid(row=size+1, columnspan=size,
                  column=0, sticky="S", padx=2, pady=(10, 5))
    return gameBoard , Board

def callback(input): 
    try:
        if input.isdigit(): 
            return True     
        elif input == "":
            return True
        else:  
            return False
    except:
        return False

def SizeCheck(size):
    try:
        if (2 < size < 17):  # Check if the new size is valid
            return size
        else:    
            return 8
    except:
        return 8
    
# top row frame, equal left and right frames, gameboard center frame
window = tk.Tk()
window.title("SOS Game")
TopFrame = tk.Frame(window, width=400, height=20)
LeftFrame = tk.Frame(window, width=100, height=200)
CenterFrame = tk.Frame(window, width=300, height=200)
RightFrame = tk.Frame(window, width=100, height=200)

TopFrame.pack(fill=tk.NONE, side=tk.TOP)
LeftFrame.pack(fill=tk.BOTH, side=tk.LEFT)
CenterFrame.pack(fill=tk.BOTH, side=tk.LEFT)
RightFrame.pack(fill=tk.BOTH, side=tk.RIGHT)

# top frame label, 2x radio buttons, label, entry box
SOSText = tk.Label(TopFrame, text="SOS", anchor="e", padx=2, pady=2)
SOSText.grid(row=0, column=0)

GameType = tk.StringVar()
GameType.set('Simple')
GameR1 = tk.Radiobutton(TopFrame, text='Simple game',
                        value='Simple', variable=GameType, justify="left")
GameR2 = tk.Radiobutton(TopFrame, text='General Game',
                        value='General', variable=GameType, justify="left")
GameR1.grid(row=0, column=1, padx=2, pady=2)
GameR2.grid(row=0, column=2, padx=2, pady=2)

BoardText = tk.Label(TopFrame, text="Board size", anchor="e", justify="right")
BoardText.grid(row=0, column=3, sticky="e", padx=(80, 2), pady=2)

BoardSize = tk.IntVar()
BoardSize.set(8)
gameBoard = InitializeGameBoard(CenterFrame)

reg = TopFrame.register(8)

BoardSizeBox = tk.Entry(TopFrame, textvariable=BoardSize, width=3)
BoardSizeBox.bind(
    '<FocusOut>', lambda event: BoardSize.set(SizeCheck(BoardSize.get()))) #field validation
BoardSizeBox.bind(
    '<Return>', lambda event: BoardSize.set(SizeCheck(BoardSize.get()))) #field validation
BoardSizeBox.grid(row=0, column=4, sticky="e", padx=5, pady=5)
reg2 = BoardSizeBox.register(callback) 
BoardSizeBox.config(validate="key", validatecommand=(reg2, '%P'))

# left frame - blue player label, human/computer radio buttons, S/O radio buttons
BlueLetter = tk.StringVar()
BlueLetter.set('S')
BlueType = tk.StringVar()
BlueType.set('Human')

BlueText = tk.Label(LeftFrame, text="Blue player")
BlueText.grid(row=1, column=0, sticky="w", padx=2, pady=5)

BlueTypeR1 = tk.Radiobutton(LeftFrame, text='Human',
                            value='Human', variable=BlueType, justify="left")
BlueTypeR1.bind('<Button-1>', lambda event, gameBoard=gameBoard: gameBoard.getBluePlayer().setType('Human'))
BlueTypeR1.grid(row=2, column=0, padx=2, pady=2)

BlueTypeR2 = tk.Radiobutton(
    LeftFrame, text='Computer', value='Computer', variable=BlueType, justify="left")
BlueTypeR2.bind('<Button-1>', lambda event, gameBoard=gameBoard: gameBoard.getBluePlayer().setType('Computer'))
BlueTypeR2.grid(row=5, column=0, padx=2, pady=2)

BluePlayerR1 = tk.Radiobutton(
    LeftFrame, text='S', value='S', variable=BlueLetter, justify="left")
BluePlayerR1.bind('<Button-1>', lambda event,gameBoard=gameBoard: gameBoard.getBluePlayer().setLetter('S'))
BluePlayerR1.grid(row=3, column=0, padx=(4, 2), pady=2)

BluePlayerR2 = tk.Radiobutton(
    LeftFrame, text='O', value='O', variable=BlueLetter, justify="left")
BluePlayerR2.bind('<Button-1>', lambda event,gameBoard=gameBoard: gameBoard.getBluePlayer().setLetter('O'))
BluePlayerR2.grid(row=4, column=0, padx=(4, 2), pady=2)

RecordGame = tk.BooleanVar()
RecordCheckButton = tk.Checkbutton(
    LeftFrame, text='Record Game', state='disabled', variable=RecordGame)
RecordCheckButton.grid(row=6, column=0, padx=5, pady=(
    (BoardSize.get()*10+5), 5), sticky="s")

# right frame - red player label, human/computer radio buttons, S/O radio buttons
RedType = tk.StringVar()
RedType.set('Human')
RedLetter = tk.StringVar()
RedLetter.set('S')

RedText = tk.Label(RightFrame, text="Red player", justify="left")
RedText.grid(row=1, column=0, sticky="e", padx=2, pady=5)

RedTypeR1 = tk.Radiobutton(RightFrame, text='Human',
                           value='Human', variable=RedType, justify="left")
RedTypeR1.bind('<Button-1>', lambda event, gameBoard=gameBoard: gameBoard.getRedPlayer().setType('Human'))
RedTypeR1.grid(row=2, column=0, padx=2, pady=2)

RedTypeR2 = tk.Radiobutton(RightFrame, text='Computer',
                           value='Computer', variable=RedType, justify="left")
RedTypeR2.bind('<Button-1>', lambda event, gameBoard=gameBoard: gameBoard.getRedPlayer().setType('Computer'))
RedTypeR2.grid(row=5, column=0, padx=2, pady=2)

RedPlayerR1 = tk.Radiobutton(
    RightFrame, text='S', value='S', variable=RedLetter, justify="left")
RedPlayerR1.bind('<Button-1>', lambda event, gameBoard=gameBoard: gameBoard.getRedPlayer().setLetter('S'))
RedPlayerR1.grid(row=3, column=0, padx=(4, 2), pady=2)

RedPlayerR2 = tk.Radiobutton(
    RightFrame, text='O', value='O', variable=RedLetter, justify="left")
RedPlayerR2.bind('<Button-1>', lambda event, gameBoard=gameBoard: gameBoard.getRedPlayer().setLetter('O'))
RedPlayerR2.grid(row=4, column=0, padx=(4, 2), pady=2)

NewGame = tk.Button(RightFrame, text="New Game", width=1,
                    height=1, background="White"
                    )
NewGame.bind('<Button-1>', lambda event:[StartNewGame(gameBoard,CenterFrame,BoardSize.get(),GameType.get()),
                                    BlueLetter.set('S'),
                                    RedLetter.set('S'),
                                    BlueType.set('Human'),
                                    RedType.set('Human')
                                    ] )
NewGame.grid(row=8, column=0, padx=(1, 0), ipadx=4, ipady=10, sticky="NWSE")

window.mainloop()