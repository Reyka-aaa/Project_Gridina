#Дан список размера N. Найти номер его первого локального минимума (локальный
# минимум — это элемент, который меньше любого из своих соседей).
import random

n = random.randint(3, 15)
lst = []
for i in range(n):
    lst.append(random.randint(1, 100))

print("N =", n)  # размер списка
print("список:", lst)

for i in range(1, n-1):
    if lst[i] < lst[i-1] and lst[i] < lst[i+1]:
        print(f'локальный минимум: {i}')
        break
else:
    print("Нет локального минимума")