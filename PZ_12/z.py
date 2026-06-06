def toggleCaseOddWords(s):
    return ' '.join(map(lambda w: w.swapcase() if len(w) % 2 != 0 else w, s.split()))

text = input("Введите строку: ")
print(toggleCaseOddWords(text))