categoria = int(input("Entre com o valor da catagoria: "))

if categoria == 1:
    print("A categoria %d é uma bolsa" % categoria)
elif categoria == 2:
    print("A categoria %d é um tenis" % categoria)
elif categoria == 3:
    print("A categoria %d é uma mochila" % categoria)
else:
    print("A categoria nao encontrada")