# Напишите программу для. проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.


def inputNumbers(x):
    xyz = ["X", "Y", "Z"]
    a = []
    for i in range(x):
        a.append(input(f"Введите значение {xyz[i]}: "))
    return a
    
s = inputNumbers(3)
left = not (s[0] or s[1] or s[2])
right = not s[0] and not s[1] and not s[2]
result = left == right
if result == True:
    print(f"Утверждение истинно")   
else:
    print(f"Утверждение ложно")


