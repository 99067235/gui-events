import tkinter as tk
from tkinter import *
import tkinter
import random
import time

actions  = ["press w", "press a", "press s", "press d"]
root = tk.Tk()
root.configure(bg="black")
root.geometry("700x500")

timerLabel = Label(root, text=20, height= 2, width= 10)
timerLabel.pack()
timerLabel.place(x=0, y=0)
scoreLabel = Label(root, text=0, height=2, width=30)
scoreLabel.pack()
def key_pressed(event):
    if event.char == randomText and randomText == "w" or event.char == randomText and randomText == "a" or event.char == randomText and randomText == "s" or event.char == randomText and randomText == "d":
        scoreLabel["text"] += 1
        actionLabel.destroy()
        action()
    else:
        key()


def action():
    global randomText, actionLabel
    start.destroy()
    randomText = random.choice(actions)
    if randomText == "press w":
        randomText = "w"
    elif randomText == "press a":
        randomText = "a"
    elif randomText == "press s":
        randomText = "s"
    elif randomText == "press d":
        randomText = "d"
    else:
        pass
    randomX = random.randint(0,700)
    randomY = random.randint(0,500)
    actionLabel = tkinter.Label(root, text=randomText,height=2, width=5, bg= "white", fg="black")
    actionLabel.place(x=randomX, y=randomY)
    key()

def key():
    root.bind("<Key>",key_pressed)
    

start = tk.Button(root, text="Click here to start", command=action)
start.pack()




root.mainloop()