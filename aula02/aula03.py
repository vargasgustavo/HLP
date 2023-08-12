'''
Foda -->
'''
#<-- Se

from tkinter import *

def media():
    n1 = float(n1.get())
    n2 = float(n2.get())
    m = (n1 + n2) /2
    if (m <= 6):
        print(f"Reprovado com media {m}")
    else:
        print(f"Aprovado com media {m}")
    sit_var.set()

app = Tk()
app.geometry("1280x720")
app.title("Meu primeiro programa em Tk")

Label(app, text="RA: ").place(x = 460, y = 20)
input_ra = Entry(app)
input_ra.place(x = 490, y = 20)

Label(app, text="Nome do aluno: ").place(x = 650, y = 20)
input_nome = Entry(app)
input_nome.place(x = 780, y = 20)

Label(app, text="Digite a primeira nota: ").place(x = 360, y = 80)
n1 = Entry(app)
n1.place(x = 490, y = 80)

Label(app, text="Digite a segunda nota: ").place(x = 650, y = 80)
n2 = Entry(app)
n2.place(x = 780, y = 80)

b = Button(text = "Confirma", command = media)
b.place(x =600, y = 150)

Label(app, text = "Situação").place(x = 10, y = 150)
sit = Entry(app, textvariable = sit_var, state = "disabled")

app.mainloop()
