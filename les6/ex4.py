class Animals():
    def move(self):
        print("I go to tree")
    def eat(self):
        print("Nyam , nyam")
    pass

class Giraffe(Animals):
    def __init__(self,weight):
        self.weight = weight        #field
    def findFood(self):
        self.move()
        print("I found!")
        self.move()
        self.eat()
        self.weight = self.weight + 1
        print("my weight %s" % self.weight)
    pass

melman = Giraffe(200)
melman.findFood()

