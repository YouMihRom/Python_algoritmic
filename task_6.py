# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.
import random

SIZE = 10
MIN_ITEM = -100
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

inmin = array.index(min_) # Индекс минимального значения
inmax = array.index(max_) # Индекс максимального значения

sum_ = 0
if inmax < inmin:
    for i in range(inmax + 1, inmin):
        sum_ += array[i]
else:
    for i in range(inmin + 1, inmax):
        sum_ += array[i]
print(sum_)
