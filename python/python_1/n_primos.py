def n_primo(n):
    soma = tot = 0
    for i in range(1, n + 1):
        tot = 0
        for j in range(1, i + 1):
            if i % j == 0:
                tot += 1
        if tot == 2:
            soma += 1

    return print(soma)


n_primo(n=int(input("Digite um número maior ou igual a 2: ")))
