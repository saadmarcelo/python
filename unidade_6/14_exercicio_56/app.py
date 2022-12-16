def reune_dados(nome, idade, profissao, fnct):
    apresentacao =  fnct(nome, idade, profissao)
    return apresentacao

def apresenta_dados(nome, idade, profissao):
    frase = "O nome do usuario é %s, tem %d de idade e a profissao %s" % (nome, idade, profissao)
    return frase

print(reune_dados("saad", 40, "Eng", apresenta_dados))