texto = "esta semana vou estudar Python"
print("Texto original ->", texto)
print(texto.lower())
print(texto.upper())
texto = texto + " e C++"
print(texto[:-6])
print("Texto modificado ->", texto + " e C++")

if ("python" in texto.lower()):
    print("Python está no texto")
else:
    print("Python não está no texto")
