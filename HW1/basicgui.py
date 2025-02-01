import tkinter as tk

window = tk.Tk()

#text
greeting = tk.Label(text="Text Entry:")
greeting.pack()

#textbox

entry = tk.Entry(fg="white", bg="dark grey", width=30)
entry.pack()

#button
button = tk.Button(
    text="Does nothing!",
    width=25,
    height=5,
    bg="dark grey",
    fg="grey",
)
button.pack()

selectedoption = tk.StringVar()
selectedoption.set('Value 1')
r1 = tk.Radiobutton(window, text='Option 1', value='Value 1', variable=selectedoption)
r2 = tk.Radiobutton(window, text='Option 2', value='Value 2', variable=selectedoption)
r1.pack()
r2.pack()

checkbox = tk.Checkbutton(window,
                text='Option 3',
                variable=selectedoption,
                onvalue='Value 3')
checkbox.pack()

window.mainloop()