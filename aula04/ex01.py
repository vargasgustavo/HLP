from tkinter import *
from tkinter import messagebox

def salvar():
    print("Socio", txt_nome.get(), "salvo com sucesso!")

app = Tk()
app.geometry("800x400")
img = PhotoImage(file = "images/download.png")
Label(app, image = img).place(x = 20,y = 20)
Label(app, text = 'Cadastro de Produtos',
      font = ("Roboto 40")).place(x = 200, y = 20)
Label(app, text = "ID").place(x = 200, y = 200)
txt_nome = Entry(app, width = 70 height = 20)
txt_nome.place(x = 250, y = 200)
btn_ok = Button(app, text = "Salvar", command = salvar)
btn_fim = Button(app, text = "Sair", command = quit)
btn_ok.grid(row = 3, column = 0)
btn_fim.grid(row = 3, column = 1)
app.mainloop()
