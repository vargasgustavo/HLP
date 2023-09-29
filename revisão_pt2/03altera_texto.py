text = "esta semana vou estudar Python"
print(f'Texto original ---> {text}')

text = text.upper()
print(f'Texto em maiúsculo ---> {text}')

text = text.lower()
print(f'Texto em minúsculo ---> {text}')

text = text + " e C++"
print(f'Texto alterado ---> {text}')

text = text[:-6]
print(f'Voltei ---> {text}')

if "Python" in text:
    print("Python está no texto!")
else:
    print("Python não está no texto!")
