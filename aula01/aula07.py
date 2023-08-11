texto1 = "Python"

texto2 = '''Este texto tem mais
de uma linha por 
isso tem tres aspas

Gu esta feliz'''
print(texto1)
print(texto2)
print("O texto 1 tem ", len(texto1), "caracteres")
print("O texto 2 tem ", len(texto2), "caracteres")
print(texto2[0:5])
print(texto2[:9])
print(texto2[0:9:2])
print(texto2[0::2])
print(texto2[::-1])
print("")
print("---------------------------------------------")
print("")
texto1 = texto1 + "\n" + texto2
print(texto1)