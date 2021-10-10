x = 654321
i = 0
soma = 0

while True:
    unidade = x % 10
    soma += unidade
    resto = x // 10
    x = resto
    i += 1
    if unidade == 0:
        break
print(soma)
