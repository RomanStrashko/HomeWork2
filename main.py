# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

# number = input('Введите вещественное число: ')
# print(number)
# sum = 0
# for i in number:
#     if i != '.':
#         sum += int(i)
# print(f'Сумма цифр числа {number} = {sum}')


# 2. Задайте список из n чисел последовательности (1 + 1/n)^n. Вывести консоль сам список и сумму его элементов.

# n = int(input('Введите количество чисел: '))
# my_list = []
# for i in range(1, n + 1):
#     my_list.append(round((1 + 1/i) ** i, 2))
# print(my_list)
# sum = 0
# for i in range(len(my_list)):
#     sum += my_list[i]
# print(f'Сумма элементов списка = {sum}')


# 3. Реализуйте алгоритм перемешивания списка. Встроенный алгоритм SHUFFLE не использовать! Реализовать свой метод

import random

size = int(input('Введите размер списка: '))
my_list = []
for i in range(size):
    my_list.append(random.randint(0, 100))
print(f'Изначальный список: {my_list}')
for i in range(len(my_list)):
    j = random.randint(0, len(my_list) - 1)
    temp = my_list[i]
    my_list[i] = my_list[j]
    my_list[j] = temp
print(f'Перемешанный список: {my_list}')



