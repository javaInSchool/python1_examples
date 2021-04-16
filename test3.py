from tkinter import *
import time

class Ball:
    def __init__(self,canvas,color):
        self.canvas = canvas
        self.id = canvas.create_oval(10,10,80,80, fill = color)
        self.canvas.move(self.id, 300,200)
        self.xSpeed = 0
        self.ySpeed = 1
        self.hCanvas = self.canvas.winfo_height()
    def draw(self):
        self.canvas.move(self.id,self.xSpeed,self.ySpeed)
        ovalCoords = self.canvas.coords(self.id)
        if ovalCoords[3] >= self.hCanvas:
            self.ySpeed = -3
        if ovalCoords[1] <= 0:
            self.ySpeed  = 3


window = Tk()
window.title("My game")
window.resizable(False,False)
window.wm_attributes("-topmost",1)


canvas = Canvas(window, width = 500, height = 500)
canvas.pack()

window.update()

ball = Ball(canvas, "Green")

while True:
    ball.draw()
    time.sleep(0.01)
    window.update()
