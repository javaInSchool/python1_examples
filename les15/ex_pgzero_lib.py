import pgzrun

alien = Actor('alien.png')
alien.pos = 100, 56

WIDTH = 500
HEIGHT = alien.height + 20

def draw():
    screen.clear()  #pycharm  каже про помилку, але код працює!
    alien.draw()
pgzrun.go() # Must be last line