class Pessoa:
    def falar(self):
        print("Olá pessoal!")

class Marcelo(Pessoa):
    def falar(self):
        print("eu sou o Marcelo")

class Roberto(Pessoa):
    pass

marcelo = Marcelo()

marcelo.falar()
roberto = Roberto()

roberto.falar()