tupla = ("marcelo", "joao", "pedro")

for nome in tupla:
    print(nome)

    if nome == "joao":
        print("Parabens Joao!")

x = 0

while x < len(tupla):
    print(tupla[x])
    x = x + 1