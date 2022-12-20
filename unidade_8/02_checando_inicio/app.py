frase = "Testamos o comeco da string"

print(frase.startswith("Testamos"))
print(frase.startswith("string"))


print(frase.endswith("Testando"))
print(frase.endswith("string"))


if (frase.endswith("string") == True):
    print("Encontramos a palavra")