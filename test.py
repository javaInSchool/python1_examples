file = open("input.txt", "r")
x,y = map(int,file.readline().split())
file.close()
file = open("output.txt", "w")


while x != 0 and y != 0:
    if x > y:
        x %= y
    else:
        y %= x

gcd = x + y

file.write(str(gcd))

file.close()