#Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, надо вывести 6843
number = int(input('Введите целое число: '))

new_num = 0
while number > 0:
    new_num = new_num * 10 + number % 10
    number //= 10
print(new_num)


# вариант 2


def number_reverse(n, i):
    if n == 0:
        return i
    else:
        return number_reverse(n // 10, i * 10 + n % 10)


print(number_reverse(new_num, 0))
