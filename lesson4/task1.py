# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

def accurate(numObj, digits=0):
    return f"{numObj:.{digits}f}"

d = 0.001
n = 3.1415926535
i = 0
while d < 1:
    d *= 10
    i += 1
print(accurate(n,i))
