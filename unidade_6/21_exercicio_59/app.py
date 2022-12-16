import random

aleatorio = random.randint(1,10)

x = int(input("Entre com um numero de 1 a 10: "))

if x == aleatorio:
    print("Correto o numero é %d" % aleatorio)
else:
    print("Errou o numero é %d " % aleatorio)