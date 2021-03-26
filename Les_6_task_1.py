# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# Примечание: По аналогии с эмпирической оценкой алгоритмов идеальным решением будет:
#
# ● выбрать хорошую задачу, которую имеет смысл оценивать по памяти;
#
# ● написать 3 варианта кода (один у вас уже есть);
#
# ● проанализировать 3 варианта и выбрать оптимальный;
#
# ● результаты анализа (количество занятой памяти в вашей среде разработки) вставить в виде комментариев в файл с кодом.
# Не забудьте указать версию и разрядность вашей ОС и интерпретатора Python

# ОС 64x Win 10
# Python 3.9

import random
import sys


SIZE = 10000
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
#print(f'Массив для итераций: {array}')


def size_culk(func):
    def size(*args, **kwargs):
        _sum = 0
        for i in args:
            _sum += sys.getsizeof(i)
        res = func(*args, **kwargs)
        print(func.__name__, _sum)
        return res
    return size


@size_culk
def first(array):
    new_array = []
    for num, i in enumerate(array):
        if i % 2 == 0:
            new_array.append(num)
    return new_array


first(array)


@size_culk
def second(array):
    new_array = []
    for i in array:
        if i % 2 == 0:
            new_array.append(array.index(i))
    return new_array


second(array)


@size_culk
def third(array):
    new_array = [array.index(i) for i in array if i % 2 == 0]
    return new_array


third(array)

#
#first 85176 байт
#second 85176 байт
#third 85176 байт
