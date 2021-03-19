#Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых трех уроков.
#Примечание. Идеальным решением будет:
#● выбрать хорошую задачу, которую имеет смысл оценивать (укажите в комментарии какую задачу вы взяли),
#● написать 3 варианта кода (один у вас уже есть),
#● проанализировать 3 варианта и выбрать оптимальный,
#● результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили замеры),
#● написать общий вывод: какой из трёх вариантов лучше и почему.


# Lesson_3_task_2
#Во втором массиве сохранить индексы четных элементов первого массива.
import timeit
import random


def timemark(func): # декоратор, выводящий время выполнения функции
     def wrapper(*args, **kwargs):
         t = timeit.timeit()
         res = func(*args, **kwargs)
         print(func.__name__, timeit.timeit() - t)
         return res
     return wrapper


SIZE = 100 # размер списка
MIN_ITEM = 0# Минимальное значение элементов в списке
MAX_ITEM = 100# Максимальное значение элементов списка
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'Массив для итераций: {array}')


@timemark
def first(array):
    new_array = []
    for num, i in enumerate(array):
        if i % 2 == 0:
            new_array.append(num)
    return new_array


first(array)


@timemark
def second(array):
    new_array = []
    for i in array:
        if i % 2 == 0:
            new_array.append(array.index(i))
    return new_array


second(array)


@timemark
def third(array):
    new_array = [array.index(i) for i in array if i % 2 == 0]
    return new_array


third(array)

#first 0.008433400000000008
#second -0.007563800000000009
#third 0.001685999999999993
# Вывод : при одинаковой алгоритмической сложности, одни и те же операции выполняемые разными методами
# будут иметь разное время на выполнение.
# измерения проводились для списка размером от 100 до 10_000 элементов. первый метод стабильно давал лучшие результаты.
