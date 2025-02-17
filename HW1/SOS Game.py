import tkinter as tk

window = tk.Tk()
TopFrame = tk.Frame(window, width=400, height=20, bg="light grey")
LeftFrame = tk.Frame(window, width=100, height=200, bg="grey")
CenterFrame = tk.Frame(window, width=300, height=200, bg="light grey")
RightFrame = tk.Frame(window, width=100, height=200, bg="grey")

TopFrame.pack(fill=tk.BOTH, side=tk.TOP, expand=True)
LeftFrame.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
CenterFrame.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
RightFrame.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)


window.mainloop()