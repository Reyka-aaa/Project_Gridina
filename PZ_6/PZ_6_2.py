#Дан список размера N. Найти номер его первого локального минимума (локальный
# минимум — это элемент, который меньше любого из своих соседей).
import random

n = random.randint(3, 15)
A = []
for i in range(n):
    A.append(random.randint(1, 100))

print("N =", n)  # размер списка
print("список:", A)

for i in range(1, n-1):
    if A[i] < A[i-1] and A[i] < A[i+1]: # меньше левого и меньше правого
        print(f'локальный минимум: {i}')
        break
else:
    print("Нет локального минимума")