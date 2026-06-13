import tkinter as tk
from tkinter import messagebox


def calculate():
    try:
        V = float(entry_v.get())
        U = float(entry_u.get())
        T1 = float(entry_t1.get())
        T2 = float(entry_t2.get())

        if U >= V:
            messagebox.showerror(
                "Ошибка",
                "Скорость течения должна быть меньше скорости лодки!"
            )
            return

        S1 = V * T1
        speed_river = V - U
        S2 = speed_river * T2
        S = S1 + S2

        result.config(
            text=(
                f"Путь по озеру: {S1:.2f} км\n"
                f"Путь по реке: {S2:.2f} км\n"
                f"Общий путь: {S:.2f} км"
            )
        )

    except ValueError:
        messagebox.showerror(
            "Ошибка",
            "Введите корректные числовые значения!"
        )


# Создание окна
root = tk.Tk()
root.title("Расчет пути лодки")
root.geometry("420x320")
root.resizable(False, False)

# Заголовок
tk.Label(
    root,
    text="Расчет пути лодки",
    font=("Arial", 16, "bold")
).pack(pady=10)

# Поля ввода
tk.Label(root, text="Скорость лодки V (км/ч):").pack()
entry_v = tk.Entry(root)
entry_v.pack()

tk.Label(root, text="Скорость течения U (км/ч):").pack()
entry_u = tk.Entry(root)
entry_u.pack()

tk.Label(root, text="Время по озеру T1 (ч):").pack()
entry_t1 = tk.Entry(root)
entry_t1.pack()

tk.Label(root, text="Время против течения T2 (ч):").pack()
entry_t2 = tk.Entry(root)
entry_t2.pack()

# Кнопка вычисления
tk.Button(
    root,
    text="Вычислить",
    command=calculate,
    width=20
).pack(pady=10)

# Поле результата
result = tk.Label(root, text="", font=("Arial", 11), justify="left")
result.pack()

root.mainloop()