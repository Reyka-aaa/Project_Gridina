#Создать словарь из списков keys = ['Ten', 'Twenty', 'Thirty'] и values = [10, 20, 30]
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

pairs = list(zip(keys, values))
print(pairs)

result_dict = dict(zip(keys, values))
print(result_dict)
