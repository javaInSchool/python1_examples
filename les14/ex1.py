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
        self.canvasH = self.canvas.winfo_height()
        self.canvasW = self.canvas.winfo_width()
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
            self.window.update_idletasks()
            self.window.update()
            time.sleep(0.02)

class Coordinates:
    def __init__(self, x1=0, y1=0, x2=0, y2=0):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

# див картинку у поясненні урок 13
def checkX(c1, c2): #c - об'єкт класу Coordinates
    if (c1.x1 > c2.x1 and c1.x1 < c2.x2) or (c1.x2 > c2.x1 and c1.x2 < c2.x2) \
            or (c2.x1 > c1.x1 and c2.x1 < c1.x2) or (c2.x2 > c1.x1 and c2.x2 < c1.x2):
        return True
    else:
        return False

# див картинку у поясненні урок 13
def checkY(c1, c2): #c - об'єкт класу Coordinates
    if (c1.y1 > c2.y1 and c1.y1 < c2.y2) or (c1.y2 > c2.y1 and c1.y2 < c2.y2) \
            or (c2.y1 > c1.y1 and c2.y1 < c1.y2) or (c2.y2 > c1.y1 and c2.y2 < c1.y2):  # див картинку у поясненні
        return True
    else:
        return False

def touchLeft(c1, c2):
    if checkY(c1,c2):
        if c1.x1 <= c2.x2 and c1.x1 >= c2.x1: # перевірка одна, бо перевіряємо ліворуч
            return True
    return False

def touchRight(c1, c2):
    if checkY(c1,c2):
        if c1.x2 >= c2.x1 and c1.x2 <= c2.x2: # перевірка одна, бо перевіряємо  праворуч
            return True
    return False

def touchTop(c1, c2):
    if checkX(c1,c2):
        if c1.y1 <= c2.y2 and c1.y1 >= c2.y1: # перевірка одна, бо перевіряємо зверху
            return True
    return False

def touchBottom(y, c1, c2):
    if checkX(c1,c2):
        yTemp = c1.y2 + y
        if yTemp >= c2.y1 and yTemp <= c2.y2:
            return True
    return False


class Sprite:
    def __init__(self, game):
        self.game = game
        self.endgame = False
        self.coordinates = None
    def move(self):
        pass
    def getCoords(self):
        return self.coordinates

class Platform(Sprite):
    def __init__(self, game, image, x, y, width, height):
        Sprite.__init__(self, game)
        self.image = image
        self.imageId = game.canvas.create_image(x, y, image = image, anchor = 'nw')
        self.coordinates = Coordinates(x,y ,x + width, y + height) #з класу Coordinates

class StickMan(Sprite):
    def __init__(self, game):
        Sprite.__init__(self,game)
        self.imagesLeft = [
            PhotoImage(file = 'stick-L1.gif'),
            PhotoImage(file = 'stick-L2.gif'),
            PhotoImage(file = 'stick-L3.gif')
        ]
        self.imagesRight = [
            PhotoImage(file='stick-R1.gif'),
            PhotoImage(file='stick-R2.gif'),
            PhotoImage(file='stick-R3.gif')
        ]
        self.imageId = game.canvas.create_image(300,500,\
                image = self.imagesLeft[0],anchor = 'nw')
        self.x = -2
        self.y = 0
        self.currentImage = 0
        self.currentImageAdd = 1
        self.lastTime = time.time()
        self.coordinates = Coordinates()
        self.jump_count = 0
        game.canvas.bind_all('<KeyPress-Left>', self.turnLeft)
        game.canvas.bind_all('<KeyPress-Right>', self.turnRight)
        game.canvas.bind_all('<space>', self.jump)

    def turnLeft(self,evt):
        if self.y == 0:
            self.x = -2

    def turnRight(self,evt):
        if self.y == 0:
            self.x = 2

    def jump(self,evt):
        if self.y == 0:
            self.y = -4
            self.jump_count = 0

    def animate(self):
        if self.x != 0 and self.y == 0:
            if time.time() - self.lastTime > 0.1:
                self.lastTime = time.time()
                self.currentImage = self.currentImage + self.currentImageAdd
                if self.currentImage >= 2:
                    self.currentImageAdd = -1
                if self.currentImage <= 0:
                    self.currentImageAdd = 1
        if self.x < 0:
            if self.y != 0:
                self.game.canvas.itemconfig(self.imageId, image = self.imagesLeft[2])
            else:
                self.game.canvas.itemconfig(self.imageId, \
                        image=self.imagesLeft[self.currentImage])
        if self.x > 0:
            if self.y != 0:
                self.game.canvas.itemconfig(self.imageId, image = self.imagesRight[2])
            else:
                self.game.canvas.itemconfig(self.imageId, \
                        image=self.imagesRight[self.currentImage])

    def move(self):
        self.animate()
        if self.y < 0:
            self.jump_count = self.jump_count + 1
            if self.jump_count > 20:
                self.y = 4
        if self.y > 0:
            self.jump_count = self.jump_count - 1

        co = self.getCoords()
        left = True
        right = True
        bottom = True
        top = True
        falling = True

        #чи торкається чоловічок об нижчю межу полотна
        if self.y > 0 and co.y2 >= self.game.canvasH:
            self.y = 0
            bottom = False
        # чи торкається чоловічок об верхню межу полотна
        if self.y < 0 and co.y1 <= 0:
            self.y = 0
            top = False
        # чи торкається чоловічек об праву сторону полотна
        if self.x > 0 and co.x2 >= self.game.canvasW:
            self.x = 0
            right = False
        # чи торкається чоловічек об ліву сторону полотна
        if self.x < 0 and co.x1 <= 0:
            self.x = 0
            left = False

        for sprite in self.game.sprites:
            if sprite == self:
                continue
            sprite_coords = sprite.getCoords()
            if top and self.y < 0 and touchTop(co, sprite_coords):
                self.y = -self.y
                top = False

            if bottom and self.y > 0 and touchBottom(self.y, co, sprite_coords):
                self.y = sprite_coords.y1 - co.y2
                if self.y < 0:
                    self.y = 0
                bottom = False
                top = False

            if bottom and falling and self.y == 0 and \
                    co.y2 < self.game.canvasH and touchBottom(1, co, sprite_coords):
                falling = False

            if left and self.x < 0 and touchLeft(co, sprite_coords):
                self.x = 0
                left = False
                if sprite.endgame:
                    self.game.isRun = False

            if right and self.x > 0 and touchRight(co, sprite_coords):
                self.x = 0
                right = False
                if sprite.endgame:
                    self.game.isRun = False

            if bottom and falling and self.y == 0 and \
                    co.y2 < self.game.canvasH:
                self.y = 4

            self.game.canvas.move(self.imageId, self.x, self.y)


    def getCoords(self):
        xyCoords = self.game.canvas.coords(self.imageId) #coords() - метод/дія полотна
        self.coordinates.x1 = xyCoords[0]
        self.coordinates.y1 = xyCoords[1]
        self.coordinates.x2 = xyCoords[0] + 54
        self.coordinates.y2 = xyCoords[1] + 60
        return self.coordinates


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