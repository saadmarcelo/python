lista = [1,2,3,4,5,6,7,8,9,10]

qual_numero = int(input("Qual o numero quer encontrar "))
achou = False
for n in lista:
    if n == qual_numero:
        print("o numero encontrado foi %d " % qual_numero)
        achou = True


if achou == False:
    print("Numero nao encontrado")


print(lista)