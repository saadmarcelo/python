numero_a = int(input("Entre com o primeiro valor: "))
numero_b = int(input("Entre com o segundo valor: "))

if numero_a > numero_b:
    numero_c = numero_a

if numero_b > numero_a:
    numero_c = numero_b

if numero_b == numero_a:
    numero_c = numero_b
    print("Os numeros sao iguais")

print("O maior numero é o %d" % numero_c)