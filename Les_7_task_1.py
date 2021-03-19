# Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами на промежутке
# [-100; 100). Выведите на экран исходный и отсортированный массивы.
# Примечания:
# ● алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
# ● постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
# Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.

import random


LENGTH = 10
MIN = -100
MAX = 99
array = [random.randint(MIN, MAX) for i in range(LENGTH)]
print(array)
print('*' * 50)


def sort_array(array):
    n = 1
    while n < LENGTH:
        flag = True
        for i in range(LENGTH - 1):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                flag = False
        if flag == True:
            break
        n += 1
    return array

print(sort_array(array))
