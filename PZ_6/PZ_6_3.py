#Дан список размера N (N — четное число). Поменять местами его первый элемент
# со вторым, третий — с четвертым и т. д.
import random

n = random.randint(2, 10) * 2
lst = []
for i in range(n):
    lst.append(random.randint(1, 100))

print("N =", n) # размер списка
print("список:", lst)

for i in range(0, n, 2):
    lst[i], lst[i+1] = lst[i+1], lst[i]

print("результат:", lst)

