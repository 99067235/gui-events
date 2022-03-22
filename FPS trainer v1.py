from cProfile import label
import tkinter as tk
from tkinter import *
import tkinter
import random
import time
import threading
from tkinter.messagebox import askretrycancel, showinfo



actions  = ["press w", "press a", "press s", "press d", "single click", "double click", "triple click"]
window = tk.Tk()
window.configure(bg="black")
window.geometry("700x500")

timer= tk.StringVar(value= "loading")
score = 0
scoreLabel = Label(window, text=0, height=2, width=30)
scoreLabel.pack()
timerlabel = Label(window, textvariable=timer, height=2, width=5)
timerlabel.pack()
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

def startTimer():
    threading.Timer(1.0, clock).start()
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
    Your score is: {score}.
    Do you want to retry?""")
    if retry:
        scoreLabel["text"] = 0
        actionLabel.destroy()
        startTimer()
    else:
        window.destroy()

start = tk.Button(window, text="Click here to start", command=startTimer)
start.pack()
    

def clock():
    global timer
    i = 0
    now = 2
    while i < 1:
        timer.set(now)
        time.sleep(1)
        now = now - 1
        if now == 0:
            retry()

window.mainloop()