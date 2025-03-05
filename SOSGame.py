import tkinter as tk
import SOSBoard
import SOSPlayer

# initialize players
global BluePlayer, RedPlayer, TurnPlayer, Board, gameBoard, CenterFrame
BluePlayer = SOSPlayer.SOSPlayer('Blue', 'Human', 'S')
RedPlayer = SOSPlayer.SOSPlayer('Red', 'Human', 'S')
TurnPlayer = BluePlayer
TurnColor = "Blue"


def BoardSizeValidation(S):
    try:
        if (2 < S < 17):
            return True
        else:
            return False
    except:
        return False


def on_button_click(btn, x, y):
    global BluePlayer, RedPlayer, TurnPlayer, gameBoard, TurnText
    print(
        f"Updating button at ({x}, {y}) with letter: {TurnPlayer.getLetter()} by {TurnPlayer.getColor()}")
    if gameBoard.getPlace(x, y) == " ":
        btn.config(text=TurnPlayer.getLetter())
        result = gameBoard.makeMove(
            TurnPlayer.getColor(), TurnPlayer.getLetter(), x, y)
        if result == True:
            if gameBoard.getBlueScore() > gameBoard.getRedScore():
                Winner = 'Blue Player Wins!'
            elif(gameBoard.getBlueScore() < gameBoard.getRedScore()):
                Winner = 'Red Player Wins!'
            else:
                Winner = 'Tie Game.'
            TurnText.config(text=Winner)
            print(
                f"[Blue:{gameBoard.getBlueScore()}|Red:{gameBoard.getRedScore()}] - {Winner}")
            
        else:
            if TurnPlayer.getColor() == 'Blue':
                TurnPlayer = RedPlayer
                TurnText.config(text="Current turn: Red")
            else:
                TurnPlayer = BluePlayer
                TurnText.config(text="Current turn: Blue",)

def StartNewGame(size, type):
    global Board, gameBoard, TurnPlayer, CenterFrame, TurnText
    print('\nInitializing ', type, ' ', size, ' x ', size)
    TurnPlayer = BluePlayer
    

    for widget in CenterFrame.winfo_children():
        widget.destroy()

    if BoardSizeValidation(size): #TODO: move to board logic AND to field validation.
        gameBoard = SOSBoard.SOSBoard(size, type)
        Board = [[[] for _ in range(size)] for _ in range(size)]
    else:
        print('\nInvalid Size used, reseting to default')
        gameBoard = SOSBoard.SOSBoard(8, type)
        size = 8
        Board = [[[] for _ in range(8)] for _ in range(8)]

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
                     btn=btn, row=row, col=col,
                     : on_button_click(btn, row, col))
            btn.grid(row=row, column=col, padx=(1, 0),
                     ipadx=4, ipady=1, sticky="NWSE")
            Board[row][col] = btn
    TurnText = tk.Label(CenterFrame, text="Current turn: Blue")
    TurnText.grid(row=size+1, columnspan=size,
                  column=0, sticky="S", padx=2, pady=(10, 5))
    return gameBoard

def SizeCheck(event,size):
    if  BoardSizeValidation(size):  # Check if the new size is valid
        return size
    else:    
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
SOSText = tk.Label(TopFrame, text="SOS", anchor="w", padx=2, pady=2)
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

reg = TopFrame.register(8)
BoardSizeBox = tk.Entry(TopFrame, textvariable=BoardSize, width=3)
BoardSizeBox.bind(
    '<FocusOut>', lambda event: BoardSize.set(SizeCheck(event,BoardSize.get()))) #field validation
BoardSizeBox.bind(
    '<Return>', lambda event: BoardSize.set(SizeCheck(event,BoardSize.get()))) #field validation
BoardSizeBox.grid(row=0, column=4, sticky="e", padx=5, pady=5)

gameBoard = StartNewGame(BoardSize.get(), GameType.get())


# left frame - blue player label, human/computer radio buttons, S/O radio buttons
BlueLetter = tk.StringVar()
BlueLetter.set('S')
BlueType = tk.StringVar()
BlueType.set('Human')

BlueText = tk.Label(LeftFrame, text="Blue player")
BlueText.grid(row=1, column=0, sticky="w", padx=2, pady=5)

BlueTypeR1 = tk.Radiobutton(LeftFrame, text='Human',
                            value='Human', variable=BlueType, justify="left")
BlueTypeR1.bind('<Button-1>', lambda event: BluePlayer.setType('Human'))
BlueTypeR1.grid(row=2, column=0, padx=2, pady=2)

BlueTypeR2 = tk.Radiobutton(
    LeftFrame, text='Computer', value='Computer', variable=BlueType, justify="left")
BlueTypeR2.bind('<Button-1>', lambda event: BluePlayer.setType('Human'))
BlueTypeR2.grid(row=5, column=0, padx=2, pady=2)

BluePlayerR1 = tk.Radiobutton(
    LeftFrame, text='S', value='S', variable=BlueLetter, justify="left")
BluePlayerR1.bind('<Button-1>', lambda event: BluePlayer.setLetter('S'))
BluePlayerR1.grid(row=3, column=0, padx=(4, 2), pady=2)

BluePlayerR2 = tk.Radiobutton(
    LeftFrame, text='O', value='O', variable=BlueLetter, justify="left")
BluePlayerR2.bind('<Button-1>', lambda event: BluePlayer.setLetter('O'))
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
RedTypeR1.bind('<Button-1>', lambda event: RedPlayer.setType('Human'))
RedTypeR1.grid(row=2, column=0, padx=2, pady=2)

RedTypeR2 = tk.Radiobutton(RightFrame, text='Computer',
                           value='Computer', variable=RedType, justify="left")
RedTypeR2.bind('<Button-1>', lambda event: RedPlayer.setType('Computer'))
RedTypeR2.grid(row=5, column=0, padx=2, pady=2)

RedPlayerR1 = tk.Radiobutton(
    RightFrame, text='S', value='S', variable=RedLetter, justify="left")
RedPlayerR1.bind('<Button-1>', lambda event: RedPlayer.setLetter('S'))
RedPlayerR1.grid(row=3, column=0, padx=(4, 2), pady=2)

RedPlayerR2 = tk.Radiobutton(
    RightFrame, text='O', value='O', variable=RedLetter, justify="left")
RedPlayerR2.bind('<Button-1>', lambda event: RedPlayer.setLetter('O'))
RedPlayerR2.grid(row=4, column=0, padx=(4, 2), pady=2)

NewGame = tk.Button(RightFrame, text="New Game", width=1,
                    height=1, background="White")
NewGame.bind(
    '<Button-1>', lambda event: StartNewGame(BoardSize.get(), GameType.get()))
NewGame.grid(row=8, column=0, padx=(1, 0), ipadx=4, ipady=10, sticky="NWSE")

window.mainloop()