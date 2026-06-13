# Из исходного текстового файла (hotline.txt) перенести в первый файл строки с
# корректными номерами телефонов (т.е. в номере должно быть 11 цифр, например,
# 86532547891), а во второй с некорректными номерами телефонов.
# Посчитать полученные строки в каждом файле.

import re

i = "hotline.txt"
o1 = "valid_phones.txt"
o2 = "invalid_phones.txt"

with open(i, "r", encoding="utf-8") as f:
    l = f.readlines()

p = re.compile(r"\d{11}")
v = []
n = []
c1 = 0
c2 = 0

for s in l:
    if p.search(s):
        v.append(s)
        c1 += 1
    else:
        n.append(s)
        c2 += 1

with open(o1, "w", encoding="utf-8") as f:
    f.writelines(v)

with open(o2, "w", encoding="utf-8") as f:
    f.writelines(n)

print(f"Корректные: {o1} -> {c1} строк")
print(f"Некорректные: {o2} -> {c2} строк")
