l = ["sofa", "televisao", "radio", "AC"]

i = 0
item_procurado = input("O que deseja buscar na casa? ")
achou = False

while i < len(l):
    if l[i] == item_procurado:
        print("Encontrado o %s " % item_procurado)
        achou = True
    i = i + 1



if achou == False:
    print("Não encontramos o item ")