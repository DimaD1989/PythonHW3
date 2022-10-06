# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
#  стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
# list=[2, 3, 5, 9]
# sum=0
# for i in range(len(list)+1):
#         if i % 2 !=0:
#                 sum += list[i]
# print('Сумма всех чисел последовательности:', sum)

# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
# list = input('Введите ряд чисел через пробел: ').split()
# list_mult = []

# for i in range(len(list) // 2):
#     j = int(list[i]) * int(list[-1 - i])
#     list_mult.append(j)
#     i *= 1

# print('Произведение пар чисел списка:', list_mult)

# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
list_num =[3.3, 5.1, 1.01]
ost_list = []
for i in range(len(list_num)):
    a = int(list_num[i])
    b= round(list_num[i] - int(list_num[i]), 2)
    ost_list.append(b)
    c_min = ost_list[0]
    c_max = ost_list[0]
    for j in ost_list:
        if j < c_min:
            c_min=j
        else:
            if j>c_max:
                c_max=j
d=c_max-c_min

print(d)


# a=list_mult = [float('0' + str(list)[str(list).index('.'):])]
# for i in range(len(list)):
#     math.modf(len(list))
# list_mult.append(x)
# print(list_mult)
# x = float(input())
# y = x-math.floor(x)
# print(y)
# from math import *

# x = int(float(input('Введите ряд вещественных чисел через пробел: '))).split()
# if x > 1:
#     a = floor(x)
#     b = x - a
#     print(round(b, 2))
# else:
#     print(x)
# a = 1.45678
# b = float('0.%s' % str(a).split('.')[1])
# print(b)

# def sum_number(n: float) -> int:
#     num=int(str(n).replace('.', ''))
#     sum = 0
#     while num != 0:
#         sum = sum + num%10
#         # num //= 10
#     return sum

# n = float(input('Введите вещественное число: '))
# sum = sum_number(n)
# print(sum)


# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10
# n = int(input())
# b = ''
# while n>0:
#         b = str(n%2)+b
#         n = n // 2
# print(b)


# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# def Fibonacci(n):
#     if n in [1, 2]:                       
#         return 1
#     else:
#         return Fibonacci(n-1) + Fibonacci(n-2)

# def NegaFibonacci(n):
#     if n == 1:                       
#         return 1
#     elif n == 2:                       
#         return -1
#     else:
#         num1, num2 = 1, -1
#         for i in range(2, n):
#             num1, num2 = num2, num1 - num2
#         return num2

# list = [0]
# num = int(input('Ведите число: '))
# for e in range(1, num + 1):
#     list.append(Fibonacci(e))
#     list.insert(0, NegaFibonacci(e))
# print(list)