import tkinter as tk
from tkinter import *

root = tk.Tk()
root.configure(bg="grey")
root.geometry("500x500")
root.title("clicker")

root.counter = 0
amountUp = 0
amountDown = 0
mycounter = root.counter
lastButton = "button"
def color():
    if root.counter == 0:
        root.configure(bg= "grey")
    elif root.counter < 0:
        root.configure(bg= "red")
    else:
        root.configure(bg="green")

def HoverColor(event):
    if root.counter == 0:
        root.configure(bg= "grey")
    elif root.counter < 0:
        root.configure(bg= "red")
    else:
        root.configure(bg="green")

### optellen
def up():
    global lastButton, amountUp
    amountUp += 1
    lastButton = "up"
    root.counter += 1
    color()
    Mylabel['text'] = str(root.counter)


def changeColor(event):
    root.configure(bg= "yellow")

### aftellen
def down():
    global lastButton, amountDown
    amountDown += 1 
    lastButton = "down"
    root.counter -= 1
    color()
    Mylabel['text'] = str(root.counter)

def labelClick(event):
    if lastButton == "up":
        amount = amountUp * 3
        Mylabel['text'] = str(amount)
    else:
        amount = amountDown / 3
        Mylabel["text"] = str(amount)

### button optellen
buttonUP = Button(root, text="Up", height=2, width=30, command=up)
root.bind("=", up)
root.bind("<Up>", lambda event: up())
buttonUP.pack()

### label getal

Mylabel = Label(root, text="0", height=2, width=30)
Mylabel.bind("<Double-Button-1>", labelClick)
root.bind("<space>", labelClick)
Mylabel.pack()

### button aftellen
buttonDown = Button(root, text="Down", height=2, width=30, command=down)
root.bind("-", down)
root.bind("<Down>", lambda event: down())
buttonDown.pack()


root.mainloop()