fin = open("input.txt")         #відкрити файл для читання
fout = open("output.txt", "w")  #відкрити файл для запису

number = int(fin.readline())         #для читання 1 числа з файлу
#a, b = map(int, fin.readline().split())  #прочитати 2 числа
x = number // 10  # 37 // 10 = 3
y = number % 10  # 37 % 10 = 7

fout.write(str(x)) # str - String, текстовий рядок
fout.write(" ")
fout.write(str(y))

fin.close()         #закрити файл
fout.close()        #закрити файл