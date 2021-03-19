#Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа
# должна принимать на вход натуральное и возвращать соответствующее простое число.
# Проанализировать скорость и сложность алгоритмов.
#Первый — с помощью алгоритма «Решето Эратосфена».
import timeit


def timemark(func): # декоратор, выводящий время выполнения функции
     def wrapper(*args, **kwargs):
         t = timeit.timeit()
         res = func(*args, **kwargs)
         print(func.__name__, timeit.timeit() - t)
         return res
     return wrapper


NUMBER = 3 # номер i-го простого числа
LIMIT = 1_00 # условная граница до которой можно расчитать простые числа
array = []


@timemark
def prime(number, limit):# сложность О(n**2)
    for i in range(2, limit):
        for j in array:
            if i % j == 0:
                break
        else:
            if len(array) < number:
                array.append(i)
    return array


res_ = prime(NUMBER, LIMIT)
print(res_[NUMBER - 1])


@timemark
def sieve(n):     # сложность О(log_n + n)
    sieve_ = list(range(n + 1))
    sieve_[1] = 0    # без этой строки итоговый список будет содержать единицу
    for i in sieve_:
        if i > 1:
            for j in range(i + i, len(sieve_), i):
                sieve_[j] = 0
    arr = []
    for i in sieve_:
        if i != 0:
            arr.append(i)

    return arr


res__ = sieve(LIMIT)
print(res__[NUMBER - 1])

#prime -0.022093
#5
#sieve -0.0023709999999999565
#5
# по результатам видно, что метод Эратосфена выигрывает по скорости расчета, измерения проводились для поиска 5-го , 18-го и 25-го
# простых чисел