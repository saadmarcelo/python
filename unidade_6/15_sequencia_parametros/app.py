def soma_todos(*nums):
    soma = 0
    for num in nums:
        soma += num
    return soma

s = soma_todos(5,6,4,3,4,5,67,4,65,7)
print(s)
