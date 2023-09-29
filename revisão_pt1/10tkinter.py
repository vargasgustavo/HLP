from tkinter import *

def calcular():
    nota1 = float(n1.get())
    nota2 = float(n2.get())
    media = (nota1 + nota2) / 2
    m.config(state="normal")
    m.insert(0, str(media))
    m.config(state="readonly")

app = Tk()

app.geometry("800x600")

Label(app, text = "Nota 1: ").grid(column = 0, row = 0)
n1 = Entry(app)
n1.grid(column = 1, row = 0)

Label(app, text = "Nota 2: ").grid(column = 0, row = 1)
n2 = Entry(app)
n2.grid(column = 1, row = 1)

Label(app, text="Media").grid(column=0, row=2)
m = Entry(app, state="readonly")
m.grid(column=1, row=2)

btn = Button(app, text = "Calcular", command = calcular)
btn.grid(column = 1, row = 3)

app.mainloop()
