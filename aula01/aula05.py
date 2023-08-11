my_str = "Gustotoso Vargueta"

print("(",my_str,")")
print("(",my_str,")", sep = "-")
print("(",my_str,")", sep = "-", end = "")
print("(",my_str,")", sep = "-")
my_str = my_str.strip()
print("(",my_str,")", sep = "-")
print(my_str[2])
print(my_str[8:11])
print(my_str.lower())
print(my_str)
print(my_str.upper())
print(my_str)
my_str = my_str.replace("Gus", "Var")
print(my_str)
my_str = my_str.split()
print(my_str)
data = "04/08/2023"
data = data.split("/")
print(data)
tem = "2023" in data
print(tem)