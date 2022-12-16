def dado(texto):
    x = ""
    if len(texto) > 20:
        x = True
    else:
        x = False

    return x


frase = dado("okiaubdiubaibqiuebdiquebdiuqbediuqbedifbqwiebfiwubefwefwef")

if frase == True:
    print("É um texto longo")
else:
    print("É um texto curto")