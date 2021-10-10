def primalidade(n):
    if n > 1 and n % 2 == 1:
        for i in range(2, n):
            if i % 2 == 1:
                if n % i == 0:
                    return False
                    break
                else:
                    return True
    else:
        return False


primalidade(n=int(input("Digite um número: ")))
fator = 2
mulltiplicidade = 0

while n > 1:
    while n % fator == 0:
        mulltiplicidade += 1
        n = n / fator
    if mulltiplicidade > 0:
        print(f"fator {fator} multiplicidade {mulltiplicidade}")
    fator += 1
    mulltiplicidade = 0
