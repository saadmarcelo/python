class Banco():
    def __init__(self, nome, saldo , numero_conta):
        self.nome = nome
        self.saldo = saldo
        self.numero_conta = numero_conta
    def saque(self, valor_saque):
        if self.saldo < valor_saque:
            print("Não possui saldo suficiente")
        else:
            self.saldo -= valor_saque

    def deposito(self, valor_deposito):
        self.saldo += valor_deposito
        print("O valor do saldo é R$ %.2f" % self.saldo)

    def transferencia(self, outra_conta, valor_transferencia):
        if self.saldo <= valor_transferencia:
            self.saldo -= valor_transferencia
            outra_conta.saldo += valor_transferencia
        else:
            print("valor insuficiente para transferencia")
        # if self.nome == "Laura saad":
        #     if self.saldo <= valor_transferencia:
        #         self.saldo -= self.saldo
        #     else:
        #         print("O saldo é insuficiente apra tranferencia ")
        # print("teste")

conta_laura = Banco("laura Saad", 200 , 2)
conta_marcelo = Banco("Marcelo Saad", 100, 1)
print(conta_marcelo.saldo)


conta_marcelo.saque(70)
print("O valor do saldo é R$ %.2f "% conta_marcelo.saldo)

conta_marcelo.deposito(200)
conta_marcelo.transferencia(conta_laura, 300)
print(conta_laura.saldo)