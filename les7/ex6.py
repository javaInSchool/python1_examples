file = open("input.txt", "r")
line1 = file.readline()
print(line1)
file.close()

file = open("input.txt", "r")
line2 = file.readline()
number_list = line2.split()
print(number_list, number_list)
x, y, z = map(int, number_list)
print(x,y,z)
print( str(x) + " " + str(y) + " " + str(z) )

file.close()