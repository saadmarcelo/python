renda = float(input("Entre com a renda: "))

if renda < 2000:
    limite = 1000
elif renda < 4000:
    limite = 2000
elif renda < 6000:
    limite = 3000
elif renda > 10000:
    print("falar com o genrente")
    limite = 3000

print("Parabens seu limite de cretido aprovado é R$%d" % limite)