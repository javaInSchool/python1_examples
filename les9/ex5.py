from tkinter import *
import time
window = Tk()
canvas = Canvas(window, width=600, height=400)
canvas.pack()

myImage = PhotoImage(file='groot.png')
canvas.create_image(10,10, anchor=NW, image = myImage)
for i in range(0, 30):
    canvas.move(1,5,0)
    window.update()
    time.sleep(0.5)

window.mainloop()