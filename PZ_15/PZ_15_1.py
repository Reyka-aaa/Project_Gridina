# Приложение КАФЕДРА для автоматизации работы отдела кадров ВУЗа. Таблица
# Преподавательский состав должна содержать следующие данные: Табельный номер,
# Фамилия И. О., Дата рождения, Должность, Ученая степень, Нагрузка, Зарплата

import sqlite3

db = sqlite3.connect('kafedra.db')
cur = db.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS Преподавательский_состав (
    Табельный_номер INTEGER PRIMARY KEY,
    Фамилия_ИО TEXT NOT NULL,
    Дата_рождения DATE NOT NULL,
    Должность TEXT NOT NULL,
    Ученая_степень TEXT,
    Нагрузка REAL DEFAULT 0,
    Зарплата REAL DEFAULT 0
)
''')

data = [
    (101, 'Иванов И.И.', '1980-05-15', 'Профессор', 'Д.т.н.', 600, 120000),
    (102, 'Петров П.П.', '1975-08-20', 'Доцент', 'К.т.н.', 500, 95000),
    (103, 'Сидоров С.С.', '1990-03-10', 'Старший преподаватель', '', 400, 70000),
    (104, 'Козлова А.А.', '1985-12-01', 'Доцент', 'К.ф-м.н.', 450, 85000),
    (105, 'Морозов М.М.', '1970-07-25', 'Профессор', 'Д.ф-м.н.', 550, 110000),
    (106, 'Новикова Н.Н.', '1995-09-14', 'Ассистент', '', 350, 50000),
    (107, 'Волков В.В.', '1988-11-30', 'Старший преподаватель', 'К.п.н.', 380, 65000),
    (108, 'Соколова С.С.', '1979-04-18', 'Доцент', 'К.э.н.', 420, 80000),
    (109, 'Лебедев Л.Л.', '1983-06-22', 'Профессор', 'Д.т.н.', 620, 125000),
    (110, 'Павлова П.П.', '1992-02-28', 'Ассистент', '', 300, 45000)
]

for row in data:
    try:
        cur.execute('INSERT INTO Преподавательский_состав VALUES (?,?,?,?,?,?,?)', row)
    except:
        pass
db.commit()

def show():
    cur.execute('SELECT * FROM Преподавательский_состав')
    rows = cur.fetchall()
    print('\n--- Преподавательский состав ---')
    for r in rows:
        print(f'{r[0]} | {r[1]} | {r[2]} | {r[3]} | {r[4]} | {r[5]}ч | {r[6]}р')
    print(f'Всего: {len(rows)}\n')

def search():
    print('\n1 - По табельному номеру')
    print('2 - По фамилии')
    print('3 - По должности')
    choice = input('Выбор: ')
    try:
        if choice == '1':
            num = int(input('Табельный номер: '))
            cur.execute('SELECT * FROM Преподавательский_состав WHERE Табельный_номер=?', (num,))
        elif choice == '2':
            name = input('Фамилия: ')
            cur.execute('SELECT * FROM Преподавательский_состав WHERE Фамилия_ИО LIKE ?', (f'%{name}%',))
        elif choice == '3':
            pos = input('Должность: ')
            cur.execute('SELECT * FROM Преподавательский_состав WHERE Должность LIKE ?', (f'%{pos}%',))
        else:
            print('Неверный выбор')
            return
        rows = cur.fetchall()
        for r in rows:
            print(f'{r[0]} | {r[1]} | {r[3]} | {r[6]}р')
        print(f'Найдено: {len(rows)}')
    except Exception as e:
        print(f'Ошибка: {e}')

def delete():
    print('\n1 - По табельному номеру')
    print('2 - По фамилии')
    print('3 - По должности')
    choice = input('Выбор: ')
    try:
        if choice == '1':
            num = int(input('Табельный номер: '))
            cur.execute('DELETE FROM Преподавательский_состав WHERE Табельный_номер=?', (num,))
        elif choice == '2':
            name = input('Фамилия: ')
            cur.execute('DELETE FROM Преподавательский_состав WHERE Фамилия_ИО LIKE ?', (f'%{name}%',))
        elif choice == '3':
            pos = input('Должность: ')
            cur.execute('DELETE FROM Преподавательский_состав WHERE Должность LIKE ?', (f'%{pos}%',))
        else:
            print('Неверный выбор')
            return
        db.commit()
        print(f'Удалено записей: {cur.rowcount}')
    except Exception as e:
        print(f'Ошибка: {e}')

def update():
    print('\n1 - Изменить зарплату по табельному номеру')
    print('2 - Изменить должность по табельному номеру')
    print('3 - Изменить нагрузку по фамилии')
    choice = input('Выбор: ')
    try:
        if choice == '1':
            num = int(input('Табельный номер: '))
            salary = float(input('Новая зарплата: '))
            cur.execute('UPDATE Преподавательский_состав SET Зарплата=? WHERE Табельный_номер=?', (salary, num))
        elif choice == '2':
            num = int(input('Табельный номер: '))
            pos = input('Новая должность: ')
            cur.execute('UPDATE Преподавательский_состав SET Должность=? WHERE Табельный_номер=?', (pos, num))
        elif choice == '3':
            name = input('Фамилия: ')
            load = float(input('Новая нагрузка: '))
            cur.execute('UPDATE Преподавательский_состав SET Нагрузка=? WHERE Фамилия_ИО LIKE ?', (load, f'%{name}%'))
        else:
            print('Неверный выбор')
            return
        db.commit()
        print(f'Обновлено записей: {cur.rowcount}')
    except Exception as e:
        print(f'Ошибка: {e}')

while True:
    print('\n КАФЕДРА ')
    print('1 - Показать всех')
    print('2 - Поиск')
    print('3 - Удаление')
    print('4 - Редактирование')
    print('5 - Выход')
    cmd = input('Выбор: ')
    if cmd == '1': show()
    elif cmd == '2': search()
    elif cmd == '3': delete()
    elif cmd == '4': update()
    elif cmd == '5': break
    else: print('Неверная команда')

db.close()
