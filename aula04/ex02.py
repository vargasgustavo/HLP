from tkinter import *

def btnImp():
    print("Boa Tarde", nome.get())
    print("Obs.:", obs.get("1.0", END))

tela = Tk()
tela.geometry("800x500")
tela.title("FIEC - Fundação Indaiatubana de Educação e Cultura")
txt1 = Label(tela, text = "Nome")
txt2 = Label(tela, text = "Endereço")
nome = Entry(tela, width = 80)
endereco = Entry(tela)
obs = Text(tela)
btn1 = Button(tela, text = "imprimir", command = btnImp)
txt1.grid(row = 0, colunm = 0, sticky = "w")
txt2.grid(row = 1, colunm = 0, sticky = "w")
nome.grid(row = 2, colunm = 1)
endereco.grid(row = 2, colunm = 1)
obs.grid(row = 2, colunm = 1)
btn1.grid(row = 3, colunm = 0)
tela.mainloop()
