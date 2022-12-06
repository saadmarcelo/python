salario = float(input("Entre com o valor do salario: "))
porcento_aumento = int(input("Entre com o percentual de aumento desejado: "))

aumento_salario = (((porcento_aumento/100) * salario)+ salario)
print("Novo salario desejado R$%.2f " % aumento_salario)