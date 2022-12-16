def multiplica_todos(*nums):
    multiplica = 1
    for num in nums:
        multiplica *= num
    return multiplica

x = multiplica_todos(1,2,3,4,50)
print(x)
