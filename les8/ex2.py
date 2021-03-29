import random
number = random.randint(1,1000)
#print(number)
while True:
    print("Вгадай число від 1 до 1000")
    userNumber = int (input())
    if userNumber == number:
        print("Правильно, вгадав!")
        break;
    elif userNumber < number:
        print("Вкажи більше число")
    elif userNumber > number:
        print("Вкажи менше число")

def booleanRandom():
    number = random.randint(0, 2)
    if number == 0:
        return True
    else:
        return False

print(booleanRandom())