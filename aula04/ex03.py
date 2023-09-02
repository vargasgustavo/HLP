from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def cbox():
    op = mes_esc.get()
    if op != "":
        msg = "Dado salvo com susexo!" + op
        messagebox.showinfo("Susexo", msg)

def cancelar():
    mes_esc.set("")

janela = Tk()
janela.title("Titulo da janela")
janela.geometry("500x250")
Label(janela, text = "Exemplo do Combobox").grid(row = 0, column = 1)
Label(janela, text = "Seleciona o mês").grid(row = 2, column = 0, padx = 10, pady = 25)
n = StringVar()
mes_esc = ttk.Combobox(janela, width = 27, textvariable = n)

valor = (
    "JANEIRO",
    "FEVEREIRO",
    "MARÇO",
    "ABRIL",
    "MAIO",
    "JUNHO",
    "JULHO",
    "AGOSTO",
    "SETEMBRO",
    "OUTUBRO",
    "NOVEMBRO",
    "DEZEMBRO"
)

mes_esc["values"] = valor
mes_esc.grid(row = 2, column = 1)
mes_esc.current(10) #depois de rodar pela primeira vez mudar current(1)

Label(text="").grid(row=3)
Label(text="").grid(row=4)
Label(text="").grid(row=5)
Label(text="").grid(row=6)

btnSalvar = Button(janela, text="Salvar")
btnSalvar.grid(row = 7, column = 0)

btnCancelar = Button(janela, text="Cancelar")
btnCancelar.grid(row = 7, column = 1)

btnFim = Button(janela, text="Fim")
btnFim.grid(row = 7, column = 2)

janela.mainloop()
