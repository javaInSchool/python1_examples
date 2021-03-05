numbers = [4 ,6 ,8]

print( list( range(1,9) ) )

def say_hello(name):
    print("Hello, %s , glad to see you!" % name)

def hello(name, surname):
    print("Hello, %s %s, glad to see you!" % (name, surname)  )

say_hello("Serg")
say_hello("Anton")
hello("Anton","Ivanov")