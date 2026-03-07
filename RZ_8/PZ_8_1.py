#Создать словарь из списков keys = ['Ten', 'Twenty', 'Thirty'] и values = [10, 20, 30]
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

result_dict = {}
for i in range(len(keys)):
    result_dict.update({keys[i]: values[i]})  # метод update()

print(result_dict)