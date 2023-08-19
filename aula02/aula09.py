from tkinter import *

def cliquei(n):
    m_var.set(n)
app = Tk()

m_var = StringVar()

lbl1 = Label (app, text = "RA")
ra = Entry(app, width=10)

lbl2 = Label (app, text = "Nome")
nome = Entry(app, width=80)

saudacoes = Entry(app,
                  textvariable=m_var,
                  state="disabled",
                  width=110)

btn1 = Button(app, text="Click")
btn2 = Button(app, text="Fim", command=app.destroy)

lbl1.pack()
ra.pack()
lbl2.pack()
nome.pack()
saudacoes.pack()
btn1.pack()
btn2.pack()

app.mainloop()
