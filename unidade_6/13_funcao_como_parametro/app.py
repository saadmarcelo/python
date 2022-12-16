def soma(a,b):
    return a + b

def multiplicacao(a , b):
    return a * b

def operacao(a, b, f):
    resultado = f(a, b)
    return resultado

print(operacao(5,5, soma))

print(operacao(10, 2, multiplicacao))