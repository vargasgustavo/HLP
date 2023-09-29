from tkinter import *

def calcular():
    num = float(valor.get())
    num = num * 1.7
    n.config(state = "normal")
    n.insert(0, str(num))
    n.config(state = "redondly")
    return

app = Tk()

app.geometry("800x600")

Label(app, text = "Digite um valor: ").grid(column = 0, row = 0)
valor = Entry(app)
valor.grid(column = 1, row = 0)

Label(app, text = "Acréscimo").grid(column = 0, row = 1)
n = Entry(app, state = "readonly")
n.grid(column = 1, row = 1)

btn = Button(app, text = "Calcular", command = calcular)
btn.grid(column = 0, row = 2)

app.mainloop()
