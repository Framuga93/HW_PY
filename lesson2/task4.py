# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов
# на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

import random

n = int(input())
a = []

for i in range(n):
    r = random.randint(-n, n)
    a.append(r)
print(a)

num = 1
with open('file.txt') as f:
    for i in f:
        if int(i) < n:
            num *= a[int(i)]
        else: num *= 1
print(num)