#Дан первый член A и разность D арифметической прогрессии. Сформировать и
# вывести список размера 10, содержащий 10 первых членов данной прогрессии: A, A
#+ D, A + 2*D, A + 3*D, ... .
import random

a = random.randint(1, 10)
d = random.randint(1, 5)

A = []
for i in range(10):
    A.append(a + i * d)

print("A =", a)
print("D =", d)
print("Прогрессия:", A)