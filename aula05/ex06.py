from tkinter import *

def promovido():
    c = float(preco.get())
    c = c * 1.7
    preco_venda.insert(0, c)

app = Tk()

app.geometry("800x600")
# Label(app, text = 'Salário',
#       font = ("Roboto 40")).grid(column = 0, row = 0)
# text = Entry(app).grid(column = 1, row = 0)

Label(app, text = "Valor de compra").grid(column = 0, row = 0)
preco = Entry(app)
preco.grid(column = 1, row = 0)
Label(app, text = "Valor de venda").grid(column = 0, row = 1)
preco_venda = Entry(app)
preco_venda.grid(column = 1, row = 1)

Button(app, text = "Calcular", command = promovido).grid(column = 0, row = 3)

app.mainloop()
