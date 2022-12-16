def retorna_lista(numero):
    nova_list = []

    for num in numero:
        if num % 2 == 0:
            nova_list.append(num)
    return nova_list


lista = [1,2,3,4,5,6,7,8,9]

lista_par =  retorna_lista(lista)

print(lista_par)

lista2 = [234,23,5235,6745,77,234,65,234,12]

print(retorna_lista(lista2))