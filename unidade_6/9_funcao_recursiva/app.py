def soma_ate_100(n):
    if n < 100:
        n += 1
        print(n)
        return soma_ate_100(n)
    else:
        return n

numero = 94

num_100 = soma_ate_100(numero)

print(num_100)