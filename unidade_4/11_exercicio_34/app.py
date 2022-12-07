numero = int(input("Entre com o numero: "))

divisoes = 0
contador = numero

while contador > 0:
    if numero % contador == 0:
        divisoes = divisoes + 1

    contador = contador -1
if divisoes == 2:
    print("O numero %d é primo" % numero)
else:
    print("O numero %d NAO é primo" % numero)