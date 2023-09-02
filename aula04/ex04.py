from tkinter import *
from tkinter import ttk

def salvar():
    print()

def cancelar():
    print()

janela = Tk()
janela.title("Titulo da janela")
janela.geometry("500x300")
opcoes = {"m":"Masculino", "f":"Feminino"}
sex_var = StringVar(janela, "m")

rb_m = Radiobutton(janela,
                   text = "Masculino",
                   value = "m",
                   variable = sex_var)

rb_f = Radiobutton(janela,
                   text = "Feminino",
                   value = "f",
                   variable = sex_var)
Label(janela, text = "Escolha o sexo").place(x = 10, y = 10)
rb_m.place(x = 20, y = 20)
rb_f.place(x = 20, y = 100)

btnSalvar = Button(janela, text = "Salvar", command = salvar, width = 7)
btnCancelar = Button(janela, text = "Cancelar", command = cancelar, width = 7)
btnFim = Button(janela, text = "Fim", command = quit, width = 7)
btnSalvar.place(x = 20, y = 200)
btnCancelar.place(x = 170, y = 300)
btnFim.place(x = 330, y = 200)
janela.mainloop()