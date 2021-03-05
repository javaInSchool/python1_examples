a = 5
b = 4

def square(x,y):
    return x * y

def printAnswer(s):
    print("Площадь прямоугольника:")
    print("%s, м2" % s)

sq = square(11, 5)
printAnswer(sq)
sq = square(a, b)
printAnswer(sq)