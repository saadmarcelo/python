class Carro():
    def __init__(self, marca, valor, portas, tanque_combustivel):
        self.marca = marca
        self.valor = valor
        self.portas = portas
        self.tanque_combustivel = tanque_combustivel
    def abastece(self, litros):
        if self.tanque_combustivel >= 100:
            print("O tanque esta cheio")
        else:
            self.tanque_combustivel += litros
            if self.tanque_combustivel > 100:
                self.tanque_combustivel = 100

    def dirigir(self, km):
        km_por_litro = 10
        self.tanque_combustivel = (km/ km_por_litro)


fusca = Carro("VW", 15000 , 4 , 70)

print(fusca.marca)

fusca.abastece(90)
print(fusca.tanque_combustivel)

fusca.dirigir(100)
print(fusca.tanque_combustivel)

fusca.abastece(10)
print(fusca.tanque_combustivel)