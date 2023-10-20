from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def retira_enter(txt):
    return txt[:-1]

def salvar():
    arq = open("agenda.db", "a")
    arq.write(nome.get() + "\n")
    arq.write(idade.get() + "\n")
    arq.write(altura.get() + "\n")
    nome.delete(0, END)
    idade.delete(0, END)
    altura.delete(0, END)
    nome.focus()
    messagebox.showinfo("Sucesso", "Dado salvo com sucesso")
    arq.close()

def ler():
    grade.delete(*grade.get_children())
    arq = open("agenda.db", "r")
    while True:
        txt_nome = arq.readline()
        txt_nome = retira_enter(txt_nome)
        if txt_nome == "":
            break
        txt_idade = arq.readline()
        txt_idade = retira_enter(txt_idade)
        txt_altura = arq.readline()
        txt_altura = retira_enter(txt_altura)
        grade.insert("", END, values = (txt_nome, txt_idade, txt_altura))
    arq.close()

def cadastro():
    frame_list.forget()
    frame_cad.pack()

def listagem():
    frame_list.pack()
    frame_cad.forget()

def mostrar_autor():
    messagebox.showinfo("Autor", "Gustavo Vargas")

def mostrar_versao():
    messagebox.showinfo("SysAgenda", "Version 1.0.0")

app = Tk()
app.title("Cadastro e Listagem")
app.geometry("600x400")

main_menu = Menu(app)
menu_contato = Menu(main_menu)
main_menu.add_cascade(label = "Contatos", menu = menu_contato)
main_menu.add_command(label = "Cadastro", command = cadastro)
main_menu.add_command(label = "Listagem", command = listagem)
main_menu.add_separator()
main_menu.add_command(label = "Fim", command = quit)

menu_sobre = Menu(main_menu)
main_menu.add_cascade(label = "Sobre", menu = menu_sobre)
main_menu.add_cascade(label = "Autor", command = mostrar_autor)
main_menu.add_cascade(label = "Versão", command = mostrar_versao)

app.config(menu = main_menu)

frame_cad = Frame(app, width = 600, height = 300)
Label(frame_cad, text = "Nome").grid(column = 0, row = 0)
nome = Entry(frame_cad)
nome.grid(column = 1, row = 0)
Label(frame_cad, text = "Idade").grid(column = 0, row = 1)
idade = Entry(frame_cad)
idade.grid(column = 1, row = 1)
Label(frame_cad, text = "Altura").grid(column = 0, row = 2)
altura = Entry(frame_cad)
altura.grid(column = 1, row = 2)

btn_salvar = Button(frame_cad, text = "Salvar", command = salvar)
btn_salvar.grid(column = 0, row = 3)
btn_fim = Button(frame_cad, text = "Fim", command = quit)
btn_fim.grid(column = 1, row = 3)
#fim cadastro

frame_list = Frame(app, width = 600, height = 300)
grade = ttk.Treeview(frame_list,
                     columns = ("nome", "idade", "altura"),
                     show = "headings")
grade.column("nome", width = 300)
grade.column("idade", width = 150, anchor = "e")
grade.column("altura", width = 150, anchor = "e")
grade.heading("nome", text = "Nome")
grade.heading("idade", text = "Idade")
grade.heading("altura", text = "Altura")
grade.pack()
btn_fim_1 = Button(frame_list, text = "Fechar", command = frame_list.forget)
btn_fim_1.pack()
ler()
#fim listagem


app.mainloop()
