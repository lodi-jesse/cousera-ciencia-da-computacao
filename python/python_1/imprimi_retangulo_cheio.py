def main():

    altura = int(input("Digite a altura: "))
    largura = int(input("Digite a largura "))
    if altura > largura:
        imprime(altura=largura,largura=altura)
    else:
        imprime(altura=altura, largura=largura)


def imprime(altura, largura):
    for i in range(altura):
        for j in range(largura - 1):
            print("#", end="")
        print("#")


main()
