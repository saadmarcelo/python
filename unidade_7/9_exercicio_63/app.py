class Pessoa():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
class Superheroi(Pessoa):
    def __init__(self, nome, idade, poder):
        super().__init__(nome, idade)
        self.poder = poder
    def utilizar_super_poder(self):
        print("O super heroi utilizou o poder %s " % self.poder)

Marcelo = Pessoa("Marcelo", 40)
print(Marcelo.idade)

Saad = Superheroi("saad", 40 , "força")

Saad.utilizar_super_poder()