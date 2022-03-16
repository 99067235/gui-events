import tkinter as tk
from tkinter import *
import tkinter
import random
import time

actions  = ["press w", "press a", "press s", "press d", "double click"]
root = tk.Tk()
root.configure(bg="black")
root.geometry("700x500")


scoreLabel = Label(root, text=0, height=2, width=30)
scoreLabel.pack()
def key_pressed(event):
    if event.char == randomText:
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

now = 3
class Clock():
    def __init__(self):
        self.window = root
        self.label = tk.Label(root, text=20, height= 2, width= 10)
        self.label.pack()
        self.label.place(x=0, y=0)
        self.update_clock()
        self.window.mainloop()

    def update_clock(self):
        global now
        self.label.configure(text=now)
        now = now - 1
        self.window.after(1000, self.update_clock)
        if now == 0:
            self.window.destroy()

app=Clock()
root.mainloop()