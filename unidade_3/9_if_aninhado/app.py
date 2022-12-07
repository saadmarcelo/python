idade = int(input("Entre com a idade: "))

if idade >= 18:
    print("Voce pode entrar na balada")

    metodo_de_pagamento = input("Como voce vai pagar a entrada? ")

    if metodo_de_pagamento == "dinheiro":
        print("A fila do dinheiro é numero 1")
    else:
        print("A fila do cartao é numero 2 ")
else:
    print("Voce NAO pode entrar na balada")