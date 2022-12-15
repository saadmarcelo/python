def saudacao(nome):
    return "olá %s " % nome

sds = saudacao("Marcelo")

print(sds + "tudo bem?")

def soma(a, b):
    return a + b

s = soma(50, 200)

print(s)

def profissao(nome):
    p = ""

    if nome == "marcelo":
        p = "programador"
    else:
        p = "Não identificado"

    return p

prof = profissao("marcelo")

print(prof)