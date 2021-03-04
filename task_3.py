# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

min_ = array[0] # минимальное значение в массиве
max_ = array[0] # максимальное значение в массиве

for i in array:
    if i > max_:
        max_ = i
    if i < min_:
        min_ = i
print(min_, max_)

inmin = array.index(min_)
inmax = array.index(max_)
array[inmin], array[inmax] = max_, min_
print(array)
