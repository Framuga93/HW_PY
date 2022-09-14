# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

a = input()
str_a = str(a)
str_a = str_a.replace('.', '')
list_a = list(str_a)
into_num = map(int, list_a)
s = sum(into_num)
print(s)
