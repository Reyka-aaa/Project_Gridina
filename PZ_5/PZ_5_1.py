#1. Составить функцию, которая выполнит суммирования числового ряда.
def sum_series():
    try:
        n = int(input("Введите число: "))
        s = 0
        i = 1
        while i <= n:
            s += i
            i += 1
        print(s)
    except ValueError:
        print("Ошибка")

sum_series()