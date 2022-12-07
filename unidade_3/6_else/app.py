poupanca = 200

saque = int(input("Quanto deseja sacar? "))

if saque <= poupanca:
    print("Voce sacou R$%d" % saque)
else:
    print("Voce nao tem saldo para sacar R$%d" % saque)
    print("Sua poupanca tem no momento R$%d" % poupanca)