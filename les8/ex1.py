from tkinter import *

root = Tk()
root.geometry("600x400")
#створити ехе файл та закрити смд

def i():
    i_in = edit.get()
    i_inf = passvord.get()
    print(i_in)
    print(i_inf)
    file = open('iogin.txt', 'r')
    file.write(i_in)
    fil = open('password.txt', 'r')
    fil.read(i_inf)

    if not i_inf == fil.readline():
        rot = Tk()
        rot.geometry("600x400")

def quit():
    global root
    root.quit()

name = Label(text="Ім'я:")
name2 = Label(text="Пароль:")
name.place(x=171, y=45, )
name2.place(x=171, y=65)
root.title('Вхід')

def lk():
    def i():
        i_inf1 = edi.get()
        i_inf2 = passvor.get()
        edi.delete(0, END)
        passvord.delete(0, END)
        print(i_inf1)
        print(i_inf2)
        file2 = open('iogin.txt', 'w')
        file2.write(i_inf2)
        file1 = open('password.txt', 'w')
        file1.write(i_inf1)

    roo = Tk()
    roo.geometry("600x400")
    roo.title('Регестрация')
    b = Button(roo, text='Регестрация', command=i)
    b.pack()
    roo.resizable(False, False)
    edi = Entry(roo)
    passvor = Entry(roo, show='*')
    edi.pack()
    passvor.pack()
    name1 = Label(roo, text="Ім'я:")
    name0 = Label(roo, text="Пароль:")
    name1.place(x=177, y=20, )
    name0.place(x=177, y=40)
    b = Button(roo, text='Регестрация', command=i)
    b.place(x=240, y=75,height=40,width =110)

def c():
    e = edit.get()
    print(e)
    edit.delete(0, END)
    passvord.delete(0, END)


dn = Label(root, text='Вхiд')
dn.config(font=('Verdana', 25))
dn.pack()
edit = Entry(root)
passvord = Entry(root)
edit.pack()
passvord.pack()
b = Button(root, text='Вхiд', command=c)
b.pack()

root.resizable(False, False)
zx = Button(root, text='Регестрация', command=lk)
zx.pack()
root.mainloop()