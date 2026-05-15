from clothing.db import save_to_db
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from clothing.calc import calculate
from clothing.export import save_to_docx, save_to_xlsx

win = tk.Tk()
win.title("Расчёт одежды")
win.geometry("300x250")

item = tk.StringVar(value="Пиджак")
size = tk.IntVar(value=48)
result = {"f": 0, "c": 0, "i": "", "s": 0}

def calc():
    f, c = calculate(item.get(), size.get())
    lab1.config(text=f"Ткань: {f} м")
    lab2.config(text=f"Цена: {c} руб")
    result.update({"f": f, "c": c, "i": item.get(), "s": size.get()})
    save_to_db(item.get(), size.get(), f, c)

def save(fmt):
    if not result["f"]:
        messagebox.showwarning("Ошибка", "Сначала нажмите Рассчитать")
        return
    fname = filedialog.asksaveasfilename(defaultextension=f".{fmt}")
    if fname:
        if fmt == "docx":
            save_to_docx(fname, result["i"], result["s"], result["f"], result["c"])
        else:
            save_to_xlsx(fname, result["i"], result["s"], result["f"], result["c"])
        messagebox.showinfo("OK", "Сохранено")

ttk.Label(win, text="Изделие:").pack(pady=5)
ttk.Combobox(win, textvariable=item, values=["Пиджак", "Брюки", "Костюм-тройка"], state="readonly").pack()

ttk.Label(win, text="Размер:").pack(pady=5)
ttk.Spinbox(win, from_=44, to=60, textvariable=size, width=5).pack()

ttk.Button(win, text="Рассчитать", command=calc).pack(pady=10)

lab1 = ttk.Label(win, text="Ткань: —")
lab1.pack()
lab2 = ttk.Label(win, text="Цена: —")
lab2.pack()

ttk.Button(win, text="Сохранить Word", command=lambda: save("docx")).pack(pady=5)
ttk.Button(win, text="Сохранить Excel", command=lambda: save("xlsx")).pack()

win.mainloop()