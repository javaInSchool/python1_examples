from tkinter import *

tk = Tk()
canvas = Canvas(tk, width = 500, height = 500)
canvas.pack()
fish_obj = PhotoImage(file="fish.png")


canvas.create_image(50,50,anchor=NW,image=fish_obj)

tk.mainloop()