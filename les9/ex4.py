from tkinter import *

window = Tk()
canvas = Canvas(window, width=600, height=400)
canvas.pack()

myImage = PhotoImage(file='stickman.png')
canvas.create_image(10,10, anchor=NW, image = myImage)

window.mainloop()