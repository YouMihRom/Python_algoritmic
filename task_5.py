#В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный». Это два абсолютно разных значения.

import random

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

max_negative = 0
for i in array:
    if i < 0 and max_negative == 0:
        max_negative = i
    elif i < 0 and max_negative < i:
        max_negative = i

print(f'{max_negative} {array.index(max_negative)}')
