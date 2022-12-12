lista = ["Matheus", "Joao", "Pedro"]

nova_lista = lista[:]

print(lista)
print(nova_lista)


nova_lista[0] = "Marcelo"

print(lista)

print("nove lista mudada ", nova_lista)