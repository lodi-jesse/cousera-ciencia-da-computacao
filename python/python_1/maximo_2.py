def maximo(x, y):
    if x == y:
        return x
    if x > y:
        return x
    elif x < y:
        return y


print(maximo(x=int(input("Digite um número: ")),
             y=int(input("digite um número: "))))
