from tkinter import *
import random
from tkinter import colorchooser

def generateRect(width, height, color):
    x1 = random.randrange(width)+50
    y1 = random.randrange(height)+50
    w = x1 + random.randrange(width)
    h = y1 + random.randrange(height)
    canvas.create_rectangle(x1, y1, w, h, fill = color)

window = Tk()
canvas = Canvas(window, width=600, height=400)
canvas.pack()
c = colorchooser.askcolor()
print(c)
for i in range (0,100):
    generateRect(200,200, c[1])

window.mainloop()