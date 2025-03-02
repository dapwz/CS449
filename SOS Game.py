import tkinter as tk
import SOSBoard
import SOSPlayer

def BoardSizeValidation(S):
    try:
        if (2 > S > 17):

            return True
        else:
            return False
    except:
        return False

def on_button_click(gameBoard,btn,x,y,Player):
    print(f"Updating button at ({x}, {y}) with letter: {Player.getLetter()} by {Player.getColor()}")
    if gameBoard.getPlace(x,y)==" ":
        btn.config(text=Player.getLetter())
        result = gameBoard.makeMove(Player.getColor(), Player.getLetter(), x, y)
        if result == False:
            if Player.getColor() == 'Blue':
                Player = RedPlayer
            else:
                Player = BluePlayer
            TurnText.config(CenterFrame, text=f"Current turn: {Player.getColor()}")

        else:
            print(f"{Player.getLetter()} Player Wins!")
            exit



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
GameType.set('General')
GameR1 = tk.Radiobutton(TopFrame, text='Simple game', value='Simple', variable=GameType, justify="left")
GameR2 = tk.Radiobutton(TopFrame, text='General Game', value='General', variable=GameType, justify="left")
GameR1.grid(row=0, column=1, padx=2, pady=2)
GameR2.grid(row=0, column=2, padx=2, pady=2)

BoardText = tk.Label(TopFrame, text="Board size", anchor="e", justify="right")
BoardText.grid(row=0, column=3, sticky="e", padx=(80, 2), pady=2)

Boardsize = tk.IntVar()
Boardsize.set(8)

reg = TopFrame.register(BoardSizeValidation(Boardsize.get()))
BoardSizeBox = tk.Entry(TopFrame, textvariable=Boardsize, width=2)
BoardSizeBox.grid(row=0, column=4, sticky="e", padx=5, pady=5)

print('\nInitializing simple ', Boardsize.get(), ' x ', Boardsize.get())
gameBoard = SOSBoard.SOSBoard(Boardsize.get(), GameType.get())

#initialize players
TurnColor = "Blue"

BlueLetter = tk.StringVar()
BlueLetter.set('S')
BlueType = tk.StringVar()
BlueType.set('Human')
BluePlayer = SOSPlayer.SOSPlayer("Blue",BlueType.get(),BlueLetter.get())

RedType = tk.StringVar()
RedType.set('Human')
RedLetter = tk.StringVar()
RedLetter.set('S')
RedPlayer = SOSPlayer.SOSPlayer("Red",RedType.get(),RedLetter.get())

TurnPlayer = BluePlayer

### left frame - blue player label, human/computer radio buttons, S/O radio buttons
BlueText = tk.Label(LeftFrame, text="Blue player")
BlueText.grid(row=1, column=0, sticky="w", padx=2, pady=5)

BlueTypeR1 = tk.Radiobutton(LeftFrame, text='Human', value='Human', variable=BlueType, justify="left")
BlueTypeR1.bind('<Button-1>',lambda event:BluePlayer.setType('Human'))
BlueTypeR1.grid(row=2, column=0, padx=2, pady=2)

BlueTypeR2 = tk.Radiobutton(LeftFrame, text='Computer', value='Computer', variable=BlueType, justify="left")
BlueTypeR2.bind('<Button-1>',lambda event:BluePlayer.setType('Human'))
BlueTypeR2.grid(row=5, column=0, padx=2, pady=2)

BluePlayerR1 = tk.Radiobutton(LeftFrame, text='S', value='S', variable=BlueLetter, justify="left")
BluePlayerR1.bind('<Button-1>', lambda event: BluePlayer.setLetter('S'))
BluePlayerR1.grid(row=3, column=0, padx=(4, 2), pady=2)

BluePlayerR2 = tk.Radiobutton(LeftFrame, text='O', value='O', variable=BlueLetter, justify="left")
BluePlayerR2.bind('<Button-1>', lambda event: BluePlayer.setLetter('O'))
BluePlayerR2.grid(row=4, column=0, padx=(4, 2), pady=2)

RecordGame = tk.BooleanVar()
RecordCheckButton = tk.Checkbutton(LeftFrame, text='Record Game', state='disabled', variable=RecordGame)
RecordCheckButton.grid(row=6, column=0, padx=5, pady=((Boardsize.get()*10+5), 5), sticky="s")

### right frame - red player label, human/computer radio buttons, S/O radio buttons
RedText = tk.Label(RightFrame, text="Red player", justify="left")
RedText.grid(row=1, column=0, sticky="e", padx=2, pady=5)

RedTypeR1 = tk.Radiobutton(RightFrame, text='Human', value='Human', variable=RedType, justify="left")
RedTypeR1.bind('<Button-1>',lambda event: RedPlayer.setType('Human'))
RedTypeR1.grid(row=2, column=0, padx=2, pady=2)

RedTypeR2 = tk.Radiobutton(RightFrame, text='Computer', value='Computer', variable=RedType, justify="left")
RedTypeR2.bind('<Button-1>',lambda event: RedPlayer.setType('Computer'))
RedTypeR2.grid(row=5, column=0, padx=2, pady=2)

RedPlayerR1 = tk.Radiobutton(RightFrame, text='S', value='S', variable=RedLetter, justify="left")
RedPlayerR1.bind('<Button-1>', lambda event: RedPlayer.setLetter('S'))
RedPlayerR1.grid(row=3, column=0, padx=(4, 2), pady=2)

RedPlayerR2 = tk.Radiobutton(RightFrame, text='O', value='O', variable=RedLetter, justify="left")
RedPlayerR2.bind('<Button-1>', lambda event: RedPlayer.setLetter('O'))
RedPlayerR2.grid(row=4, column=0, padx=(4, 2), pady=2)

### gameboard - grid of buttons, updated when new game clicked
Board =  [[[] for _ in range(Boardsize.get())] for _ in range(Boardsize.get())]

for row in range(Boardsize.get()):
    for col in range(Boardsize.get()):
        btn = tk.Button(
            CenterFrame,
            text=" ",
            width=1,
            height=1,
            background="White"
        )
        btn.bind('<Button-1>', lambda event, 
                 gameBoard=gameBoard, btn=btn, 
                 row=row, col=col, 
                 Player=TurnPlayer: on_button_click(gameBoard, btn, row, col, Player))
        
        btn.grid(row=row, column=col, padx=(1, 0), ipadx=4, ipady=1, sticky="NWSE")
        Board[row][col] = btn

TurnText = tk.Label(CenterFrame, text="Current turn: Blue")
TurnText.grid(row=Boardsize.get()+1, columnspan=Boardsize.get(), column=0, sticky="s", padx=2, pady=(10, 5))

window.mainloop()
