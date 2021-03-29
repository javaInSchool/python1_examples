#selection sort algorithm
numbers = [9,1,4,3,5,6,2,7,8]
length = len(numbers)         #кількіть елементів у списку
for i in range (0, length):   #загальна кількість переборів = кількість елементів
    # починаємо шукати найменше і позначаємо за найменше елемент під номером "і"
    minIndex = i
    #далі порівнюємо мінімальний елемент з кожним наступним "i+1"
    for j in range (i+1, length):
        #якщо наступний елемент менше за мінімальний, то він стає мінімальним
        if numbers[j] < numbers[minIndex]:
            #тобто запам'ятовуємо його номер у списку
            minIndex = j
    #якщо знайдений мінімальний елемент не стоїть на поточному місці
    if minIndex != i:
        #тоді міняємо місцями елементи
        numbers[i], numbers[minIndex] = numbers[minIndex], numbers[i]
        print(numbers)

