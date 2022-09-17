# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

ans = []
f1 = f2 = 1
n = int(input())
ans.append(f1)
ans.append(f2)
for i in range(2,n):
    f1, f2 = f2, f1 + f2
    ans.append(f2)
i = 1
for i in range(len(ans)):
    if i % 2 != 0:
        ans[i]=ans[i]*-1
ans.reverse()
ans.append(0)
f1 = f2 = 1
ans.append(f1)
ans.append(f2)
for i in range(2,n):
    f1, f2 = f2, f1 + f2
    ans.append(f2)
print(ans)


