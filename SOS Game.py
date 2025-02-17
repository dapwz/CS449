import tkinter as tk

def BoardSizeValidation(S):
    try: 
        if (2> S >16):
            
            return True
        else: 
            return False
    except:
        return False

#top row frame, equal left and right frames, gameboard center frame
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

#top frame label, 2x radio buttons, label, entry box
SOSText  = tk.Label(TopFrame,text="SOS",anchor="w",padx=2,pady=2)
SOSText.grid(row=0,column=0)

GameType = tk.StringVar()
GameType.set('Simple')
GameR1 = tk.Radiobutton(TopFrame, text='Simple game', value='Simple', variable=GameType, justify="left")
GameR2 = tk.Radiobutton(TopFrame, text='General Game', value='General', variable=GameType, justify="left")
GameR1.grid(row=0,column=1,padx=2,pady=2)
GameR2.grid(row=0,column=2,padx=2,pady=2)

BoardText  = tk.Label(TopFrame,text="Board size",anchor="e", justify="right")
BoardText.grid(row=0,column=3,sticky="e",padx=(80,2),pady=2)

Boardsize = tk.IntVar()
Boardsize.set('8')
reg = TopFrame.register(BoardSizeValidation(Boardsize))
BoardSizeBox = tk.Entry(TopFrame,textvariable=Boardsize,width=2)
BoardSizeBox.grid(row=0,column=4,sticky="e",padx=5,pady=5)

for row in range(Boardsize.get()):
    for col in range(Boardsize.get()):
        tk.Button(
            CenterFrame,
            text=f"   ",
            width=1,
            height=1,
            background="White"
        ).grid(row=row, column=col,padx=(1,0), ipadx=4,ipady=1,sticky = "NWSE")

TurnText = tk.Label(CenterFrame,text="Current turn: Blue")
TurnText.grid(row=Boardsize.get()+1,columnspan=Boardsize.get(),column=0,sticky="s",padx=2,pady=(10,5))

SPlayer=tk.StringVar()
SPlayer.set("Blue")


#left frame - blue player label, human/computer radio buttons, S/O radio buttons
BlueText  = tk.Label(LeftFrame,text="Blue player")
BlueText.grid(row=1,column=0,sticky="w",padx=2,pady=5)

BlueType = tk.StringVar()
BlueType.set('Human')

BlueTypeR1 = tk.Radiobutton(LeftFrame, text='Human', value='Human', variable=BlueType, justify="left")
BlueTypeR2 = tk.Radiobutton(LeftFrame, text='Computer', value='Computer', variable=BlueType, justify="left")
BlueTypeR1.grid(row=2,column=0,padx=2,pady=2)
BlueTypeR2.grid(row=5,column=0,padx=2,pady=2)

SPlayerR1 = tk.Radiobutton(LeftFrame, text='S', value='Blue', variable=SPlayer, justify="left")
OPlayerR1 = tk.Radiobutton(LeftFrame, text='O', value='Red', variable=SPlayer, justify="left")
SPlayerR1.grid(row=3,column=0,padx=(4,2),pady=2)
OPlayerR1.grid(row=4,column=0,padx=(4,2),pady=2)

RecordGame = tk.BooleanVar()
RecordCheckButton = tk.Checkbutton(LeftFrame,text='Record Game',state='disabled',variable=RecordGame)
RecordCheckButton.grid(row=6,column=0,padx=5,pady=((Boardsize.get()*10+5),5),sticky="s")


#right frame - red player label, human/computer radio buttons, S/O radio buttons
RedText  = tk.Label(RightFrame,text="Red player", justify="left")
RedText.grid(row=1,column=0,sticky="e",padx=2,pady=5)

RedType = tk.StringVar()
RedType.set('Computer')
RedTypeR1 = tk.Radiobutton(RightFrame, text='Human', value='Human', variable=RedType, justify="left")
RedTypeR2 = tk.Radiobutton(RightFrame, text='Computer', value='Computer', variable=RedType, justify="left")
RedTypeR1.grid(row=2,column=0,padx=2,pady=2)
RedTypeR2.grid(row=5,column=0,padx=2,pady=2)

SPlayerR2 = tk.Radiobutton(RightFrame, text='S', value='Red', variable=SPlayer, justify="left")
OPlayerR2 = tk.Radiobutton(RightFrame, text='O', value='Blue', variable=SPlayer, justify="left")
SPlayerR2.grid(row=3,column=0,padx=(4,2),pady=2)
OPlayerR2.grid(row=4,column=0,padx=(4,2),pady=2)

window.mainloop()