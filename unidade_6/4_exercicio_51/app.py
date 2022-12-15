def maior_q_10(numero):
    x = ""
    if numero > 10:
        x = True
    else:
        x = False
    return x

valor = maior_q_10(50)
if valor == True:
    print("O valor é MAIOR que 10")
else:
    print("O valor é menor que 10")