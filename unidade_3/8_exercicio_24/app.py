numero_a = int(input("Entre com o primeiro numero: "))
numero_b = int(input("Entre com o segundo numero: "))

mult = numero_a * numero_b

if mult <= 100:
    print("Valor baixo, o numero é %d " % mult)
else:
    print("Valor alto, o numero é %d " % mult)