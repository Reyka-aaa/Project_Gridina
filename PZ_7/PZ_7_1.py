#Дан символ C. Вывести два символа, первый из которых предшествует символу C в
# кодовой таблице, а второй следует за символом C.
import random
import string
c = random.choice(string.ascii_letters)
print(f"сгенерированная буква: '{c}' (код: {ord(c)})")
print(f"предыдущая буква: '{chr(ord(c)-1)}' (код: {ord(c)-1})")
print(f"следующая буква: '{chr(ord(c)+1)}' (код: {ord(c)+1})")