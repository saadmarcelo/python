lista = ["quadcortex", "helix", "kemper", "gt1000"]

item_um = input("qual pedaleira deseja procurar primeiro ? ")
item_dois = input("qual pedaleira deseja procurar depois ? ")

i = 0

while i < len(lista):
    if lista[i] == item_um:
        print("a pedaleria procurada antes foi %s " % item_um)
        break
    elif lista[i] == item_dois:
        print("A pedaleira procurada antes foi %s " % item_dois   )
        break

    i = i + 1
