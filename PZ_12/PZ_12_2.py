# Из матрицы сформировать массив из положительных четных элементов, найти их
# сумму и среднее арифметическое.
import random

m = [[random.randint(-10, 20) for _ in range(3)] for _ in range(4)]

print("исходная матрица:")
for c in m :
    print(c)

p = list(filter(lambda x: x > 0 and x % 2 == 0, [x for c in m for x in c]))

print("положительные четные:", p)

if len(p) > 0:
    s = sum(p)
    sr = s / len(p)
    print("сумма:", s)
    print("среднее:", sr)
else:
    print("нет положительных четных элементов")