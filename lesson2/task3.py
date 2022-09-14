# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

n = int(input())
s = 0
l = []
for i in range (1,n+1):
    s += ((1+1/i)**i)
    l.append(round(((1+1/i)**i),2))
print(l)
print(round(s,2))