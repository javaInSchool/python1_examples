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

myGame = Game()
myGame.mainloop()