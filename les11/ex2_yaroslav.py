#Unlimited life version of the pinball game python code
from tkinter import *  # Comes from the standard library of python, GUI
import random
import time


# Create Ball class and define the ball
class Ball:
    def __init__(self, canvas, paddle, color):  # Initialization function
        self.canvas = canvas  # Assign the object variable canvas to the object variable canvas
        self.paddle = paddle #Assign object variables to paddle
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)  # The function creat_oval returns the ID of the creation target
        self.canvas.move(self.id, 245, 100)  # Move the ball to the center of the canvas
        starts = [-3, -2, -1, 1, 2, 3]  # Define a list storage initial speed
        random.shuffle(starts)  # Randomly arrange the numbers in the list
        self.x = starts[0]  # Take the first number in the list
        self.y = -3  # Change the upward speed of the ball to 3, and the initial combined speed becomes larger
        self.canvas_height = self.canvas.winfo_height()  # Get the current canvas height and assign it to the object variable canvas_height
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False

    def hit_paddle(self, pos): #Define pinball hitting operation, return true when two images intersect, otherwise false
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if paddle_pos[1] <= pos[3] <= paddle_pos[3]:
                return True
        return False

#Draw the ball on the canvas as defined
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)  # Make the ball move, call the move function on the canvas, the incoming parameters are x, y
        pos = self.canvas.coords(self.id)  # Create a variable and assign the canvas function coords to pos, and return a list by the ID of the circle. The 4 numbers are the coordinates of the upper left corner and the lower right corner.
        if pos[1] <= 0:#The positions of 0 and 1 in the list pos are the coordinates of the upper left of the circle, and the positions of 2 and 3 are the coordinates of the lower right
            self.y = 4  # Changing the number can realize the speed of the ball in different directions
        if pos[3] >= self.canvas_height:
# self.hit_bottom = True #If you want to achieve the ball to the bottom of the canvas, gameover can add this line, and comment out the next line
            self.y = -4
        if self.hit_paddle(pos) == True:#Realize the rebound when the ball contacts the racket
            self.y = -4
        if pos[0] <= 0:
            self.x = 4
        if pos[2] >= self.canvas_width:
            self.x = -4


# Create racket class
class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas #Similar to the ball class, first pass in the canvas object variable
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 300)#Set the racket in the initial position when the game starts
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()#Set the left and right movement range of the racket
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)#Bind the buttons and the left and right buttons of the racket separately
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)

    def draw(self): #Draw the racket on the canvas
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:#These two if statements are used to set the racket boundary
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0

#Define left and right key functions
    def turn_left(self, evt):
        self.x = -5# Changing the value can change the flexibility of the racket

    def turn_right(self, evt):
        self.x = 5


# Create game canvas
tk = Tk()  # Create tk object
tk.title("Variable Speed ​​Pinball Game")  # Use the title function in the tk object to title the window
tk.resizable(0, 0)  # Make the window size not changeable both horizontally and vertically
tk.wm_attributes("-topmost", 1)  # Put the window containing our canvas before all other windows
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)  # bd=0 is to ensure that there is no border outside the canvas
canvas.pack()  # Let the canvas adjust its own size according to the width and height parameters given in the previous line
tk.update()  # Let tkinter initialize the animation in the game

paddle = Paddle(canvas, 'blue')
ball = Ball(canvas, paddle, 'red')  # Create an object of Ball class

while 1:  # Animation loop, let tkinter keep drawing
    if ball.hit_bottom == False:#If the ball is not received, gameover
        ball.draw()
        paddle.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)  # Loop once, the time for python to rest on its own, can be understood as the interval time when drawing pictures all the time