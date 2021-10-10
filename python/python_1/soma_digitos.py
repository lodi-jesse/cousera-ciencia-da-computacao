n = int(input("Digite um número inteiro: "))
soma = 0

while True:
    unidade = n % 10
    soma += unidade
    resto = n // 10
    n = resto
    if resto == 0:
        break
print(soma)
