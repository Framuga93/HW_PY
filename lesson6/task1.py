# Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.
#
#
#

# inp = list(map(int , input().split()))
# print(list(filter(lambda x: inp.count(x)==1, inp)))




# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
#
# n = int(input())
# s = 1
# i = 1
# for i in range(n):
#     s = (i+1)*s
#     print(s)
#
# import math
# x = int(input('input N: '))
# factorial = lambda x: x and x * factorial(x - 1) or 1
# print(factorial(x))





# Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число.
# В качестве символа-разделителя используйте пробел.

# import re
# s = str(input())
# r = re.split(' ', s)
# t = map(int, r)
# k = map(int,r)
# print(min(t))
# print(max(k))


# s = list(map(int, (input().split())))
# print(max(s),min(s))


# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# a = [2, 3, 5, 9, 3, 2, 3, 2]
# s = 0
# i = 1
# while i < len(a):
#     s += a[i]
#     i += 2
# print(s)

# a = [2, 3, 5, 9, 3, 2, 3, 2]
# print(sum(a[1::2]))





# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# with open("words.txt", "r") as fin:
#     for line in fin:
#         words = line.split()
#         for word in words:
#             if "абв" in word:
#                 words.remove(word)
#         sentence = " ".join(words)
#         print(sentence)
#


# inp = list(map(str, input('isert text: ').split()))
# sample = input('insert remove text: ')
# print(list(filter(lambda x: x != sample, inp)))