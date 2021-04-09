file = open("input.txt", "r")
file2 = open("output.txt", "a+")
n = int(file.readline())

numbersList = []
for i in range (n):
    numbersList.append(file.readline())
    a,b = map(int,numbersList[i].split())
    r = a+b
    file2.write("%d \n" % r)

file.close()
file2.close()