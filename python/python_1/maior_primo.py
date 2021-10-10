def maior_primo(k):
    for x in range(k + 1):
        tot = 0
        for i in range(1, x + 1):
            if x % i == 0:
                tot += 1
        if tot == 2:
            res = x
    return res


print(maior_primo(k=int(input("Digite um valor: "))))
