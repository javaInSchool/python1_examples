from tkinter import *
import time
import random

def move(event):
    if event.keysym == 'Up':
        canvas.move(1, 0, -5)
    elif event.keysym == 'Down':
        canvas.move(1, 0, 5)
    elif event.keysym == 'Left':
        canvas.move(1, -5, 0)
    else:
        canvas.move(1, 5, 0)

class Ball:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_oval(10,10,80,80, fill = color)
        self.canvas.move(self.id, 300,200)
        self.xSpeed = 0
        self.ySpeed = 3
        self.hCanvas = self.canvas.winfo_height()
        print(self.canvas.winfo_height())
    def draw(self):
        self.canvas.move(self.id, self.xSpeed, self.ySpeed)
        ovalCoords = self.canvas.coords(self.id)
        if ovalCoords[3] >= self.hCanvas: # x1, y1, x2, y2
            self.ySpeed = -3
        if ovalCoords[1] <= 0:
            self.ySpeed = 3

window = Tk()
window.title("MyGame")
window.resizable(False, False)
window.wm_attributes("-topmost", 1)

canvas = Canvas(window, width=600, height=400)
canvas.pack()

id_polygon = canvas.create_polygon(10, 10, 10, 60, 50, 35)
print(id_polygon)

window.update()
ball = Ball(canvas, 'Green')

canvas.bind_all('<KeyPress-Up>', move)
canvas.bind_all('<KeyPress-Down>', move)
canvas.bind_all('<KeyPress-Left>', move)
canvas.bind_all('<KeyPress-Right>', move)

while True:
    ball.draw()
    window.update()
    time.sleep(0.01)
    #window.mainloop()