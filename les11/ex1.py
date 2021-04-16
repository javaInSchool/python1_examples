from tkinter import *
import time
import random

class Ball:
    def __init__(self, canvas, stick, color):
        self.canvas = canvas
        self.stick = stick
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
        if self.touchStick(ovalCoords):
            self.ySpeed = -3

    def touchStick(self, coords):
        stickCoord = self.canvas.coords(self.stick.id)
        if coords[2] >= stickCoord[0] and coords[0] <= stickCoord[2]:   # check X - coords
            if coords[3] >= stickCoord[1] and coords[3] <= stickCoord[3]: # check Y - coords
                return True
        return False

class Stick:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0,0, 100, 10, fill = color)
        self.canvas.move(self.id, 250,350)
        self.x = 0
        self.wCanvas = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>', self.moveLeft )
        self.canvas.bind_all('<KeyPress-Right>', self.moveRight )

    def moveLeft(self, event):
        self.x = -2
        print(self.x)
    def moveRight(self, event):
        self.x = 2
        print(self.x)

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        stickCoords = self.canvas.coords(self.id) # x1, y1 - top-left corner,  x2, y2 - bottom, right corner
        if (stickCoords[2] >= self.wCanvas ) or (stickCoords[0] <= 0):
            self.x = 0

window = Tk()
window.title("MyGame")
window.resizable(False, False)
window.wm_attributes("-topmost", 1)

canvas = Canvas(window, width=600, height=400)
canvas.pack()

window.update()

stick = Stick(canvas, 'yellow')             #створюємо паличку для відбивання м'яча
ball = Ball(canvas, stick, 'Green')

#canvas.bind_all('<KeyPress-Up>', move)
#canvas.bind_all('<KeyPress-Down>', move)

while True:
    ball.draw()
    stick.draw()
    window.update()
    time.sleep(0.01)
    #window.mainloop()