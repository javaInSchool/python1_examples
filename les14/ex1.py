from tkinter import *
import time

class Game:
    def __init__(self):
        self.window = Tk()
        self.window.title("Платформер з чоловічком паличкою")
        self.window.resizable(False, False)
        self.canvas = Canvas(self.window, width = 800, height = 600 )
        self.canvas.pack()
        self.window.update()

        self.backgr = PhotoImage (file = "back.gif")
        w = self.backgr.width()  #дізнатись ширину картинки фону
        h = self.backgr.height()
        for x in range (0, 8):
            for y in range(0, 6):
                self.canvas.create_image(x * w, y * h, image = self.backgr, anchor ='nw')
        self.sprites = []
        self.isRun = True

    def mainloop(self):
        while True:
            if self.isRun == True:
                for sprite in self.sprites:
                    sprite.move()
            self.window.update()
            time.sleep(0.01)

class Coordinates:
    def __init__(self, x1=0, y1=0, x2=0, y2=0):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

class Sprite:
    def __init__(self, game):
        self.game = game
        self.endgame = False
        self.coordinates = None
    def move(self):
        pass
    def coordinates(self):
        return self.coordinates

class Platform(Sprite):
    def __init__(self, game, image, x, y, width, height):
        Sprite.__init__(self, game)
        self.image = image
        self.imageId = game.canvas.create_image(x, y, image = image, anchor = 'nw')
        self.coordinates = Coordinates(x,y ,x + width, y + height)

class StickMan(Sprite):
    def __init__(self, game):
        Sprite.__init__(self,game)
        self.imagesLeft = [
            PhotoImage(file = 'manL1.gif'),
            PhotoImage(file = 'manL2.gif'),
            PhotoImage(file = 'manL3.gif')
        ]
        self.imagesRight = [
            PhotoImage(file='manR1.gif'),
            PhotoImage(file='manR2.gif'),
            PhotoImage(file='manR3.gif')
        ]
        self.image = game.canvas.create_image(300,500,\
                image = self.imagesLeft[0],anchor = 'nw')
        self.x = -2
        self.y = 0
        self.currentImage = 0
        self.currentImageAdd = 1
        self.lastTime = time.time()
        self.coordinates = Coordinates()
        game.canvas.bind_all('<KeyPress-Left>', self.moveLeft)
        game.canvas.bind_all('<KeyPress-Right>', self.moveRight)
        game.canvas.bind_all('<space>', self.jump)
    def moveLeft(self,evt):
        self.x = -2
        print(self.x)
    def moveRight(self,evt):
        self.x = 2
        print(self.x)
    def jump(self,evt):
        pass

myGame = Game()

tempImage = PhotoImage(file = 'platform1.gif')
platform1 = Platform(myGame, tempImage, 10, 500, 100, 10)
platform2 = Platform(myGame, tempImage, 400, 200, 100, 10)
tempImage = PhotoImage(file = 'platform2.gif')
platform3 = Platform(myGame, tempImage, 200, 400, 65, 10)
platform4 = Platform(myGame, tempImage, 300, 380, 65, 10)
myGame.sprites.append(platform1)
myGame.sprites.append(platform2)
myGame.sprites.append(platform3)
myGame.sprites.append(platform4)

stickman1 = StickMan(myGame)
myGame.sprites.append(stickman1)

myGame.mainloop()