class Pessoa:
    def __init__(self, nome, idade, profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

    def __str__(self):
        return "O nome do usuario é %s e tem %d anos e é um %s" % (self.nome, self.idade, self.profissao)


Marcelo = Pessoa("Marcelo" , 40 , "Engenheiro")

print(Marcelo.__str__())