# 1. Ввести 4 числа. Найти и вывести сумму и количество отрицательных чисел.
count = 0
sum_neg = 0
for i in range(4):
    num = input(f"Введите число {i + 1}: ")
    while type(num) != int:
        try:
            num = int(num)
        except ValueError:
            print("Неправильно ввели!")
            num = input(f"Введите число {i + 1}: ")

    if num < 0:
        count += 1
        sum_neg += num

print(f"Количество отрицательных чисел: {count}")
print(f"Сумма отрицательных чисел: {sum_neg}")

# 2. Ввести 4 числа. Найти и вывести количество четных чисел.
count_even = 0
for i in range(4):
    num = input(f"Введите число {i + 1}: ")
    while type(num) != int:
        try:
            num = int(num)
        except ValueError:
            print("Неправильно ввели!")
            num = input(f"Введите число {i + 1}: ")

    if num % 2 == 0:
        count_even += 1

print(f"Количество четных чисел: {count_even}")

# 3. Найти и вывести квадраты и кубы чисел от 2 до 5.
print("Число\tКвадрат\tКуб")
for i in range(2, 6):
    print(f"{i}\t{i ** 2}\t{i ** 3}")

# 4. Найти и вывести S=1!+2!+3!+4!+…+n! (n>1)
n = input("Введите n (n>1): ")
while type(n) != int:
    try:
        n = int(n)
        if n <= 1:
            print("n должно быть больше 1!")
            n = input("Введите n (n>1): ")
        else:
            break
    except ValueError:
        print("Неправильно ввели!")
        n = input("Введите n (n>1): ")

S = 0
for i in range(1, n + 1):
    factorial = 1
    j = i
    while j:
        factorial *= j
        j -= 1
    S += factorial

print(f"S = {S}")

# 5. Ввести N чисел. Найти и вывести их среднее арифметическое.
N = input("Введите количество чисел N: ")
while type(N) != int:
    try:
        N = int(N)
    except ValueError:
        print("Неправильно ввели!")
        N = input("Введите количество чисел N: ")

sum_numbers = 0
for i in range(N):
    num = input(f"Введите число {i + 1}: ")
    while type(num) != int:
        try:
            num = int(num)
        except ValueError:
            print("Неправильно ввели!")
            num = input(f"Введите число {i + 1}: ")
    sum_numbers += num

average = sum_numbers / N
print(f"Среднее арифметическое: {average}")

# 6. Ввести N чисел. Посчитать и вывести количество чисел равных нулю.
N = input("Введите количество чисел N: ")
while type(N) != int:
    try:
        N = int(N)
    except ValueError:
        print("Неправильно ввели!")
        N = input("Введите количество чисел N: ")

count_zero = 0
for i in range(N):
    num = input(f"Введите число {i + 1}: ")
    while type(num) != int:
        try:
            num = int(num)
        except ValueError:
            print("Неправильно ввели!")
            num = input(f"Введите число {i + 1}: ")

    if num == 0:
        count_zero += 1

print(f"Количество чисел равных нулю: {count_zero}")

# 7. Даны два целых числа А и В (А < В). Вывести в порядке убывания все целые числа,
# расположенные между А и В (включая сами числа А и В), а также количество этих чисел.
a = input("Введите число A: ")
b = input("Введите число B: ")
while type(a) != int:
    try:
        a = int(a)
    except ValueError:
        print("Неправильно ввели!")
        a = input("Введите число A: ")
while type(b) != int:
    try:
        b = int(b)
    except ValueError:
        print("Неправильно ввели!")
        b = input("Введите число B: ")

if a >= b:
    print("Ошибка: A должно быть меньше B")
else:
    k = 0
    i = b
    while i >= a:
        print(i)
        i -= 1
        k += 1
    print(f'Количество чисел: {k}')

# 8. Даны два целых числа А и В (А < В). Найти сумму всех целых чисел от А до В включительно.
a = input("Введите число A: ")
b = input("Введите число B: ")
while type(a) != int:
    try:
        a = int(a)
    except ValueError:
        print("Неправильно ввели!")
        a = input("Введите число A: ")
while type(b) != int:
    try:
        b = int(b)
    except ValueError:
        print("Неправильно ввели!")
        b = input("Введите число B: ")

if a >= b:
    print("Ошибка: A должно быть меньше B")
else:
    sum_range = 0
    i = a
    while i <= b:
        sum_range += i
        i += 1
    print(f'Сумма чисел от {a} до {b}: {sum_range}')

# 9. Посчитать и вывести количество элементов арифметической прогрессии,
# удовлетворяющих условию 10<ai<30.
k = input("Введите количество чисел арифметической прогрессии: ")
while type(k) != int:
    try:
        k = int(k)
    except ValueError:
        print("Неправильно ввели!")
        k = input("Введите число: ")

l = 1
s = 1
count_progression = 0
while l <= k:
    if 10 < s < 30:
        count_progression += 1
    l += 1
    s += 3

print(f"Количество элементов прогрессии в диапазоне 10<ai<30: {count_progression}")

# 10. Вывести первые N (N≥3) чисел Фибоначчи и посчитать количество четных чисел.
N = input("Введите N (N≥3): ")
while type(N) != int:
    try:
        N = int(N)
        if N < 3:
            print("N должно быть не меньше 3!")
            N = input("Введите N (N≥3): ")
        else:
            break
    except ValueError:
        print("Неправильно ввели!")
        N = input("Введите N (N≥3): ")

fib1, fib2 = 1, 1
count_even_fib = 0

print("Числа Фибоначчи:")
print(fib1)
if fib1 % 2 == 0:
    count_even_fib += 1

print(fib2)
if fib2 % 2 == 0:
    count_even_fib += 1

for i in range(2, N):
    fib_next = fib1 + fib2
    print(fib_next)
    if fib_next % 2 == 0:
        count_even_fib += 1
    fib1, fib2 = fib2, fib_next

print(f"Количество четных чисел Фибоначчи: {count_even_fib}")

# 11. Дана арифметическая прогрессия а1=1, а2=4, а3=7, а4=10, а5=13, …
# Составить программу, которая каждый элемент прогрессии разделит на 2 и результат округлит до ближайшего целого.
k = input("Введите количество чисел арифметической прогрессии: ")
while type(k) != int:
    try:
        k = int(k)
    except ValueError:
        print("Неправильно ввели!")
        k = input("Введите число: ")

l = 1
s = 1
print("Прогрессия после деления на 2 и округления:")
while l <= k:
    result = round(s / 2)
    print(result)
    l += 1
    s += 3