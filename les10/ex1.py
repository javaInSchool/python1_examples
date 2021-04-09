from tkinter import *
import time

window = Tk()
canvas = Canvas(window, width=600, height=400)
canvas.pack()

def move(event):
    if event.keysym == 'Up':
        canvas.move(1, 0, -5)
    elif event.keysym == 'Down':
        canvas.move(1, 0, 5)
    elif event.keysym == 'Left':
        canvas.move(1, -5, 0)
    else:
        canvas.move(1, 5, 0)

canvas.create_polygon(10, 10, 10, 60, 50, 35)
canvas.bind_all('<KeyPress-Up>', move)
canvas.bind_all('<KeyPress-Down>', move)
canvas.bind_all('<KeyPress-Left>', move)
canvas.bind_all('<KeyPress-Right>', move)

window.mainloop()