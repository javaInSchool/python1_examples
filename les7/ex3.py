#directory

file = open("input.txt", "w")
print(dir(file))

help(dir)

class Animal():
    weight = 5
    pass

print(dir(Animal))
print(dir(Animal)[len(dir(Animal))-1])
nameList = ["Serg", "Andriy", "Sveta"]
print( len(nameList) )
voc = {'id':1, 'name':"serg"}
print(len(voc))
print(len("voc"))
