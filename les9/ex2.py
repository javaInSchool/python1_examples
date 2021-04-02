from tkinter import *

window = Tk()
canvas = Canvas(window, width=600, height=400)
canvas.pack()
canvas.create_line(0,0,500,500)
canvas.create_rectangle(10,10,100,50)

window.mainloop()
