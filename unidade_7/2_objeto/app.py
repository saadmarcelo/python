class Pessoa:
    def __init__(self, nome, idade, profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

marcelo = Pessoa("Marcelo", 40, "Engenheiro")

print(marcelo)

print(marcelo.nome)
print(marcelo.idade)
print(marcelo.profissao)

if marcelo.nome == "Marcelo":
    print( "O nome é Marcelo ")