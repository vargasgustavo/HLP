text = "estou aprendendo Python"

print(text.upper())

print(text.lower())

text = "não " + text
print(text)

text = text[4:]
print(text)

if "Python" in text:
    print("Python está no texto!")
else:
    print("Python não está no texto!")
