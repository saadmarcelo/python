def list_num(numero):
    media = 0
    soma = 0

    for x in numero:
        soma += x

    media = soma / len(numero)

    return media

notas = [9,8,7,6,5,4,3]

media_prova = list_num(notas)

print(media_prova)