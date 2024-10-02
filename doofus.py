import tkinter as tk
from tkinter import messagebox
from math import sqrt

#region метод с вычислением
def calculate():
    try:
        a = float(entryA.get())
        b = float(entryB.get())
        c = float(entryC.get())

        aStr = f"{int(a)}" if a.is_integer() else f"{a:.2f}"
        bStr = f"+{int(b)}" if b.is_integer() else f"+{b:.2f}"
        bStr = f"{int(b)}" if b.is_integer() else f"{b:.2f}"

        if c > 0:
            cStr = f"+{int(c)}" if c.is_integer() else f"+{c:.2f}"
        else:
            cStr = f"{int(c)}" if c.is_integer() else f"{c:.2f}"

        equationLabel.config(text=f"{aStr}x^2 {bStr}x {cStr} = 0")

        discriminant = b**2 - 4 * a * c
        dResult.set(f"D = {int(discriminant)}")
        if discriminant > 0:
            x1 = (-b + sqrt(discriminant)) / (2 * a)
            x2 = (-b - sqrt(discriminant)) / (2 * a)
            x1Result.set(f"x1 = {int(x1) }")
            x2Result.set(f"x2 = {int(x2) }")
        elif discriminant == 0:
            x = -b / (2 * a)
            x1Result.set(f"x1 = {int(x) }")
            x2Result.set("x2 = ")
        else:
            x1Result.set("x1 = Не существует")
            x2Result.set("x2 = Не существует")
    except ValueError:
        messagebox.showerror("Что-то не так", "Введите корректные коэффициенты")
#endregion

#region настройки окна + отступы
window = tk.Tk()
window.title("Вторая лабораторная")
window.geometry("400x250")
window.resizable(False,False)
labelPadding = (10, 5)
entryPadding = (5, 5)
#endregion

#region Создание компонентов
equationLabel = tk.Label(window, text="ax^2 + bx + c = 0", font=("Arial", 10))
labelA = tk.Label(window, text="Коэффициент a:")
labelB = tk.Label(window, text="Коэффициент b:")
labelC = tk.Label(window, text="Коэффициент c:")

entryFrameA = tk.Frame(window, padx=10, pady=10)
entryFrameB = tk.Frame(window, padx=10, pady=10)
entryFrameC = tk.Frame(window, padx=10, pady=10)
entryA = tk.Entry(entryFrameA)
entryB = tk.Entry(entryFrameB)
entryC = tk.Entry(entryFrameC)

calculateButton = tk.Button(window, text="Вычислить", command=calculate, padx=56, pady=5)

dResult = tk.StringVar(value="D = ")
x1Result = tk.StringVar(value="x1 = ")
x2Result = tk.StringVar(value="x2 = ")
labelD = tk.Label(window, textvariable=dResult)
labelX1 = tk.Label(window, textvariable=x1Result)
labelX2 = tk.Label(window, textvariable=x2Result)
#endregion

#region Подстановка компонентов в сетку
equationLabel.grid(row=0, column=0, columnspan=2, pady=(20, 10))
labelA.grid(row=1, column=0)
labelB.grid(row=2, column=0)
labelC.grid(row=3, column=0)
calculateButton.grid(row=4, column=0, columnspan=2, pady=(10, 10))
labelD.grid(row=1, column=2)
labelX1.grid(row=2, column=2)
labelX2.grid(row=3, column=2)
#endregion

#region тут помещение в сетку
entryFrameA.grid(row=1, column=1)
entryFrameB.grid(row=2, column=1)
entryFrameC.grid(row=3, column=1)
entryA.pack() # эта вся херня для корректного помещения
entryB.pack()
entryC.pack()
#endregion

window.mainloop()