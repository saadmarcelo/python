class Carro:
    def __init__(self, portas, motor, teto_solar, marca, preco):
        self.portas = portas
        self.motor = motor
        self.teto_solar = teto_solar
        self.marca = marca
        self.preco = preco

civic = Carro(4, 2.0, False, "honda", 120.000)

print(civic.preco)
print(civic.marca)