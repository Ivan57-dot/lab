import PySimpleGUI as sg
from clothing import Calculator, Exporter

c = Calculator()
e = Exporter()

layout = [
    [sg.Text("Изделие:"), sg.Combo(["Пиджак", "Брюки", "Костюм-тройка"], default_value="Пиджак", key="item")],
    [sg.Text("Размер:"), sg.Spin([i for i in range(44, 61)], initial_value=48, key="size")],
    [sg.Button("Рассчитать")],
    [sg.Text("Ткань: --\nСтоимость: --", key="res", size=(30, 2))],
    [sg.Button("Word"), sg.Button("Excel")]
]

window = sg.Window("Одежда", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    
    if event == "Рассчитать":
        name = values["item"]
        s = int(values["size"])
        f, cost = c(name, s)
        window["res"].update(f"Ткань: {f} м\nСтоимость: {cost} руб")
    
    if event in ("Word", "Excel"):
        if not c.result:
            sg.popup_error("Сначала рассчитайте")
            continue
        name, size, f, cost, _ = c.result
        fmt = "docx" if event == "Word" else "xlsx"
        file = sg.popup_get_file("Сохранить", save_as=True, default_extension=f".{fmt}")
        if file:
            if fmt == "docx":
                e.docx(file, name, size, f, cost)
            else:
                e.xlsx(file, name, size, f, cost)
            sg.popup("Сохранено")

window.close()