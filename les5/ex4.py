import time
import sys

print( time.asctime() )

age = sys.stdin.readline() # readline - string

#КНИГА "КОД. Тайный язык информатики" Чарльз

def myAge(a):
    if int(a) > 16:
        print("you can get a passport")
    else:
        print("passport is not allowed")

myAge(age)