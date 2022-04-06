import tkinter as tk
from tkinter import *
import tkinter
import random
import time
import threading
from tkinter.messagebox import askretrycancel


actions  = ["press w", "press a", "press s", "press d", "single click", "double click", "triple click"]
window = tk.Tk()
window.configure(bg="black")
window.geometry("700x500")


score = 0
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

def clock():
    global timer, timerlabel
    timer = 20
    timeVar = tkinter.StringVar(value= str(timer))
    timerlabel = Label(window, textvariable=timeVar, height=2, width=5)
    timerlabel.pack()
    for i in range(timer):
        time.sleep(1)
        timer -= 1
        timeVar.set(str(timer))
        if timer == 0:
            retry()
    
def startTimer():
    global counter, timerlabel, scoreLabel
    scoreLabel = Label(window, text=0, height=2, width=5, font=("Comic Sans MS", 14))
    scoreLabel.pack()
    scoreLabel.place(x=640, y=0)
    counter = threading.Timer(1.0, clock).start()
    action()

def action():
    global randomText, actionLabel, buttonClicked
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
    Your score: {score}.
    Do you want to retry?""")
    if retry:
        scoreLabel["text"] = 0
        actionLabel.destroy()
        timerlabel.destroy()
        startTimer()
    else:
        window.destroy()

start = tk.Button(window, text="Click here to start", command=startTimer)
start.pack()


window.mainloop()