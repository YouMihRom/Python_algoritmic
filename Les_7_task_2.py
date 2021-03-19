#Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
import random

LENGTH = 9
MIN = 0
MAX = 50
array = [random.uniform(MIN, MAX) for i in range(LENGTH)]
print(array)
print('*' * 50)


def merge_sort(array):

    if len(array) <= 1:
        return array

    left_side = merge_sort(array[:len(array) // 2])
    right_side = merge_sort(array[len(array) // 2:])

    i = j = 0
    res = []

    while i < len(left_side) or j < len(right_side):

        if i >= len(left_side):
            res.append(right_side[j])
            j += 1

        elif j >= len(right_side):
            res.append(left_side[i])
            i += 1

        elif left_side[i] < right_side[j]:
            res.append(left_side[i])
            i += 1

        else:
            res.append(right_side[j])
            j += 1

    return res


print(merge_sort(array))
