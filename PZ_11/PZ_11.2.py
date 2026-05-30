# Составить генератор (yield), который выводит из строки только цифры
def d(s):
    for i in s:
        if i.isdigit():
            yield i
t = input('s =')
r = ''.join(d(t)) # в строку
print(r)
