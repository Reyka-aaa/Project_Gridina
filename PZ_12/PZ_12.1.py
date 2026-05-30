# В квадратной матрице элементы на главной диагонали увеличить в 2 раза
import random

m = [[random.randint(-10, 15) for _ in range(4)] for _ in range(4)]

print("исходная матрица:")
for c in m :
    print(c)

for i in range(4):
    m[i] = list(map(lambda x, idx: x * 2 if idx == i else x, m[i], range(4))) # если индекс столбца равен номеру строки то умножь на 2

print("результат:")
for c in m :
    print(c)