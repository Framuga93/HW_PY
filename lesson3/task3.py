# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным
# и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

a = [1.1, 1.2, 3.1, 5, 10.01]
s = []
for i in range(len(a)-1):
    if (a[i] - int(a[i])) == 0:
        a.remove(a[i])
for i in range(len(a)):
        s.append(round(a[i]%1, 2))
print(f'{s} => {max(s)-min(s)}')
