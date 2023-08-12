from tkinter import *

def area_tri():
    base = float(input_base.get())
    altura = float(input_altura.get())
    area = (base * altura) / 2
    print(f"A area do triangulo e {area}")