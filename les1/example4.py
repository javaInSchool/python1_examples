import time

print("Калькулятор")
f = input()
while f in '1234567890':
    if f not in '1234567890':
        print('Напиши число')
        f = input()

s = input()
while s in '/+-':
    if s not in '/+-':
        print('Напиши одно из этих символов: / * + -')
        s = input()

ff = input()
while ff in '1234567890':
    if ff not in '1234567890':
        print('Напиши число')
        ff = input()

time.sleep(2)
print('Нажми Enter')
input()
print(str(f) +s+ str(ff) )