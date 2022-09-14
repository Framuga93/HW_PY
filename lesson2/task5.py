# Реализуйте алгоритм перемешивания списка.

import random

n = int(input())
a = []
for i in range(n):
    r = random.randint(-n, n)
    a.append(r)
print(a)
random.shuffle(a)
print(a)