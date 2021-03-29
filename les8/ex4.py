numbers = [1, 3, 5, 2, 6, 4, 7, 9, 8] # 9 = 81 9
#numbers.sort()
#bubble sort
length = len(numbers)
for i in range(length):
    for j in range(0, length - i - 1):
        if numbers[j] > numbers[j+1]:
            numbers[j],numbers[j+1] = numbers[j+1],numbers[j]
            changed = True
    if not changed:
        break
# i = 9
# j = 0 | 9-1-1 = 7
print(numbers)