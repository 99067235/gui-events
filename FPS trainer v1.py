import tkinter as tk
from tkinter import *
import tkinter
import random
import time
from tkinter.messagebox import askretrycancel, showinfo

e = False
buttonClicked = False
actions  = ["press w", "press a", "press s", "press d", "single click", "double click", "triple click"]
window = tk.Tk()
window.configure(bg="black")
window.geometry("700x500")

score = 0
scoreLabel = Label(window, text=0, height=2, width=30)
scoreLabel.pack()
def key_pressed(event):
    global score
    if event.char == randomText:
        score += 1
        scoreLabel["text"] += 1
        actionLabel.destroy()
        action()
    else:
        key()

def labelClick(event):
    global score
    score += 2
    scoreLabel["text"] += 2
    actionLabel.destroy()
    action()


def action():
    global randomText, actionLabel, buttonClicked
    buttonClicked = True
    start.destroy()
    randomText = random.choice(actions)
    if randomText == "press w":
        randomText = "w"
        key()
    elif randomText == "press a":
        randomText = "a"
        key()
    elif randomText == "press s":
        randomText = "s"
        key()
    elif randomText == "press d":
        randomText = "d"
        key()
    else:
        pass
    randomX = random.randint(0,600)
    randomY = random.randint(0,400)
    actionLabel = tkinter.Label(window, text=randomText,height=2, width=9, bg= "white", fg="black")
    if randomText == "single click":
        actionLabel.bind("<Button-1>", labelClick)
    elif randomText == "double click":
        actionLabel.bind("<Double-Button-1>", labelClick)
    elif randomText == "triple click":
        actionLabel.bind("<Triple-Button-1>", labelClick)
    actionLabel.place(x=randomX, y=randomY)
    key()

def key():
    window.bind("<Key>",key_pressed)

def retry():
    global now, scoreLabel, e
    retry = askretrycancel("Retry?", f"""
    Your score is: {score}.
    Do you want to retry?""")
    if retry:
        scoreLabel["text"] = 0
        actionLabel.destroy()
        now = 2
        e = False
        action()
    else:
        window.destroy()

start = tk.Button(window, text="Click here to start", command=action)
start.pack()
    
now = 4
class Clock():
    def __init__(self):
        global timerlabel
        self.window = window
        timerlabel = self.label = tk.Label(window, text=now, height= 2, width= 10)
        self.label.pack()
        self.label.place(x=0, y=0)
        self.update_clock()
        self.window.mainloop()

    def update_clock(self):
        global now, e
        self.label.configure(text=now)
        self.window.after(1000, self.update_clock)
        if now == 0 and e == False:
            e = True
            retry()
        elif now > 0:
            now = now - 1

app = Clock()
window.mainloop()