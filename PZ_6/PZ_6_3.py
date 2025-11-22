#Дан список размера N (N — четное число). Поменять местами его первый элемент
# со вторым, третий — с четвертым и т. д.
n = int(input("N: "))
lst = []
for i in range(n):
    lst.append(int(input()))

for i in range(0, n, 2):
    lst[i], lst[i+1] = lst[i+1], lst[i]

print(lst)

