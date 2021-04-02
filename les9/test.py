from tkinter import *
import pickle


class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password

    def __eq__(self, other):
        if not isinstance(other, User):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return self.name == other.name and self.password == other.password
    pass

def getData():
    name = nameTextField.get()
    password = passwordTextField.get()
    user = User(name, password)
    file = open("data.dat", "rb")
    userLoad = pickle.load(file)
    file.close()
    if user.__eq__(userLoad):
        print("You are enter")
    else:
        print("Wrong pass or login")

    nameTextField.delete(0, END)
    passwordTextField.delete(0, END)

def reg():
    name = nameTextField.get()
    password = passwordTextField.get()
    user = User(name,password)
    file = open("data.dat", "wb")
    pickle.dump(user, file)
    file.close()
    print("Registration sucsesful")
    nameTextField.delete(0, END)
    passwordTextField.delete(0, END)
    pass

root = Tk()
root.title('Кабінет')
root.geometry("600x400")
root.resizable(False, False)

header = Label(root, text='Вхiд')
header.config(font=('Verdana', 25))
header.pack()

nameLabel = Label(text="Ім'я:")
nameLabel.place(x=171, y=45)

passwordLabel = Label(text="Пароль:")
passwordLabel.place(x=171, y=65)

nameTextField = Entry(root)
nameTextField.pack()

passwordTextField = Entry(root)
passwordTextField.pack()

enter = Button(root, text='Вхiд', command=getData)
enter.pack()

registration = Button(root, text='Регестрация', command=reg)
registration.pack()

root.mainloop()