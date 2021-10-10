import math


def primo(x):
    if x > 1 and x % 2 == 1 or (x == 2):
        if x == 2 or x == 3:
            return print(True)
        for c in range(2, x):
            if c % 2 == 1:
                if x % c == 0:
                    return print(False)
                    break
                else:
                    return print(True)
    else:
        return print(False)


i = 1
while i <= 10:
    n = int(input("Digite um numero: "))
    primo(x=n)
    i += 1
    print(math.factorial(n))

