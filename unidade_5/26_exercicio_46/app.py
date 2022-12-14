lista = [40 , 2 , 35 , 43, 2 , 1]

menor_valor = lista[0]

for n in lista:
    if n < menor_valor:
        menor_valor = n

print(menor_valor)