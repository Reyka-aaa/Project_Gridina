# Задание 1.
# Средствами языка Python сформировать текстовый файл (.txt), содержащий
# последовательность из целых положительных и отрицательных чисел. Сформировать новый
# текстовый файл (.txt) следующего вида, предварительно выполнив требуемую обработку элементов:
# Исходные данные:
# Количество элементов:
# Минимальный элемент:
# Квадраты четных элементов:
# Сумма квадратов четных элементов:
# Среднее арифметическое суммы квадратов четных элементов:

import random

n = []
a = random.randint(1, 11)

for i in range(a):
    n.append(random.randint(-99, 100))

f1 = open('data_1.txt', 'w')
for i in n:
    f1.write(str(i) + ' ')
f1.close()

f1 = open('data_1.txt')
k = f1.read().split()

for i in range(len(k)):
    k[i] = int(k[i])

f1.close()

c = len(k)
m = min(k)

kv = []
s = 0
for i in k:
    if i % 2 == 0:
        kv.append(i * i)
        s = s + (i * i)

if len(kv) > 0:
    sr = s / len(kv)
else:
    sr = 0

f2 = open('data_2.txt', 'w', encoding='utf-16')

f2.write('Исходные данные: ')
f2.write(str(k))
f2.write('\n')

f2.write('Количество элементов: ')
f2.write(str(c))
f2.write('\n')

f2.write('Минимальный элемент: ')
f2.write(str(m))
f2.write('\n')

f2.write('Квадраты четных элементов: ')
f2.write(str(kv))
f2.write('\n')

f2.write('Сумма квадратов четных элементов: ')
f2.write(str(s))
f2.write('\n')

f2.write('Среднее арифметическое суммы квадратов четных элементов: ')
f2.write(str(sr))

f2.close()

for i in open('data_2.txt', encoding='utf-16'):
    print(i, end='')