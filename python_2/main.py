def cria_matriz(num_linhas, num_colunas):
    matriz = []  #cria uma lista
    for i in range(num_linhas):
        linha = []
        for j in range(num_colunas):
            valor = int(input("Digite um valor:"))
            linha.append(valor)

        matriz.append(linha)

    return matriz


def print_matriz():
    linhas = int(input("Digite a quantidade de linhas: "))
    colunas = int(input("Digite a quantidade de colunas: "))
    matiz = cria_matriz(num_linhas=linhas, num_colunas=colunas)
    for i in matiz:
        print(i)


if __name__ == '__main__':
    print_matriz()

