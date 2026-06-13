import tkinter as tk
from tkinter import ttk, messagebox

# функции
def register():
    skills = []

    if html_var.get():
        skills.append("HTML/CSS")
    if perl_var.get():
        skills.append("Perl")
    if asp_var.get():
        skills.append("ASP")
    if photoshop_var.get():
        skills.append("Adobe Photoshop")
    if java_var.get():
        skills.append("JAVA")
    if js_var.get():
        skills.append("JavaScript")
    if flash_var.get():
        skills.append("Flash")

    messagebox.showinfo(
        "Регистрация",
        f"Пользователь: {login.get()}\n"
        f"Специализация: {spec.get()}\n"
        f"Пол: {gender.get()}\n"
        f"Навыки: {', '.join(skills)}"
    )


def clear():
    login.delete(0, tk.END)
    password.delete(0, tk.END)
    confirm.delete(0, tk.END)
    text.delete("1.0", tk.END)

    spec.set("Web-мастер")
    gender.set("М")

    html_var.set(False)
    perl_var.set(False)
    asp_var.set(False)
    photoshop_var.set(False)
    java_var.set(False)
    js_var.set(False)
    flash_var.set(False)

# окно
root = tk.Tk()
root.title("Анкета Web-разработчика")
root.geometry("760x560")
root.configure(bg="#dcdcdc")

title = tk.Label(
    root,
    text="Анкета Web-разработчика",
    font=("Times New Roman", 24, "bold"),
    bg="#dcdcdc"
)
title.pack(pady=10)

main = tk.Frame(root, bg="#dcdcdc")
main.pack()

# регистрационное имя
tk.Label(
    main,
    text="Регистрационное имя",
    bg="#dcdcdc",
    anchor="w",
    width=20
).grid(row=0, column=0, sticky="w", padx=5, pady=4)

login = tk.Entry(main, width=35)
login.grid(row=0, column=1, sticky="w", pady=4)

# Пароль
tk.Label(
    main,
    text="Пароль",
    bg="#dcdcdc",
    anchor="w",
    width=20
).grid(row=1, column=0, sticky="w", padx=5)

password = tk.Entry(main, show="*", width=25)
password.grid(row=1, column=1, sticky="w")

# Подтверждение
confirm = tk.Entry(main, show="*", width=25)
confirm.grid(row=2, column=1, sticky="w")

tk.Label(
    main,
    text="подтвердите пароль",
    bg="#dcdcdc"
).grid(row=2, column=2, sticky="w", padx=10)

#  Специализация
tk.Label(
    main,
    text="Ваша специализация",
    bg="#dcdcdc",
    anchor="w",
    width=20
).grid(row=3, column=0, sticky="w", padx=5, pady=5)

spec = tk.StringVar(value="Web-мастер")

combo = ttk.Combobox(
    main,
    textvariable=spec,
    width=22,
    state="readonly"
)

combo["values"] = (
    "Web-мастер",
    "Frontend",
    "Backend",
    "Full Stack"
)

combo.grid(row=3, column=1, sticky="w")

#  Пол
tk.Label(
    main,
    text="Пол",
    bg="#dcdcdc",
    width=20,
    anchor="w"
).grid(row=4, column=0, sticky="w", padx=5)

gender = tk.StringVar(value="М")

gender_frame = tk.Frame(main, bg="#dcdcdc")
gender_frame.grid(row=4, column=1, sticky="w")

tk.Radiobutton(
    gender_frame,
    text="М",
    variable=gender,
    value="М",
    bg="#dcdcdc"
).pack(side="left")

tk.Radiobutton(
    gender_frame,
    text="Ж",
    variable=gender,
    value="Ж",
    bg="#dcdcdc"
).pack(side="left")

# Навыки
tk.Label(
    main,
    text="Ваши навыки",
    bg="#dcdcdc",
    width=20,
    anchor="nw"
).grid(row=5, column=0, sticky="nw", padx=5)

skills = tk.Frame(main, bg="#dcdcdc")
skills.grid(row=5, column=1, sticky="w")

html_var = tk.BooleanVar()
perl_var = tk.BooleanVar()
asp_var = tk.BooleanVar()
photoshop_var = tk.BooleanVar()
java_var = tk.BooleanVar()
js_var = tk.BooleanVar()
flash_var = tk.BooleanVar()

tk.Checkbutton(skills, text="знание HTML и CSS", variable=html_var, bg="#dcdcdc").pack(anchor="w")
tk.Checkbutton(skills, text="знание Perl", variable=perl_var, bg="#dcdcdc").pack(anchor="w")
tk.Checkbutton(skills, text="знание ASP", variable=asp_var, bg="#dcdcdc").pack(anchor="w")
tk.Checkbutton(skills, text="знание Adobe Photoshop", variable=photoshop_var, bg="#dcdcdc").pack(anchor="w")
tk.Checkbutton(skills, text="знание JAVA", variable=java_var, bg="#dcdcdc").pack(anchor="w")
tk.Checkbutton(skills, text="знание JavaScript", variable=js_var, bg="#dcdcdc").pack(anchor="w")
tk.Checkbutton(skills, text="знание Flash", variable=flash_var, bg="#dcdcdc").pack(anchor="w")

# О себе
tk.Label(
    main,
    text="Дополнительные\nсведения о себе",
    bg="#dcdcdc",
    justify="left",
    width=20
).grid(row=6, column=0, sticky="nw", padx=5, pady=10)

text = tk.Text(main, width=45, height=6)
text.grid(row=6, column=1, pady=10, sticky="w")

# Кнопки
buttons = tk.Frame(root, bg="#dcdcdc")
buttons.pack(pady=10)

tk.Button(
    buttons,
    text="зарегистрировать",
    width=20,
    command=register
).pack(side="left", padx=10)

tk.Button(
    buttons,
    text="очистить форму",
    width=20,
    command=clear
).pack(side="left", padx=10)

root.mainloop()