import math


def hipotenusa(n):
    i = 1
    while i <= n:
        j = 1
        while j <= n:
            a = i
            b = j
            c = int(math.hypot(a, b))
            if (c > a) and (c > b) and (c < (a + b)):
                if (a ** 2) + (b ** 2) == c ** 2:
                    if c == n:
                        return c
            j = j + 1
        i = i + 1

    return 0


def soma_hipotenusas(n):
    soma = old = 0
    for i in range(1, n + 1):
        result = hipotenusa(i)
        if result > old:
            old = result
            soma = soma + result

    return print(soma)


soma_hipotenusas(n=int(input("Digite um número: ")))
