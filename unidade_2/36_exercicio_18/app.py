saldo = 359.56
print(saldo)
novo_valor = float(input("Entre o novo a ser adicionado: "))
cartao_credito = 125.98

conta_final = saldo + novo_valor - cartao_credito

input("O valor de saldo em conta é R$%.2f" % conta_final)