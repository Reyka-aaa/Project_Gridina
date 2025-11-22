#Дан список размера N. Найти номер его первого локального минимума (локальный
# минимум — это элемент, который меньше любого из своих соседей).
n = int(input("N: "))
lst = []
for i in range(n):
    lst.append(int(input()))

for i in range(1, n-1):
    if lst[i] < lst[i-1] and lst[i] < lst[i+1]:
        print(i)
        break
else:
    print("Нет локального минимума")