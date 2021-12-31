def imprime_matriz(minha_matriz):

    linhas = len(minha_matriz)
    colunas = len(minha_matriz[0])

    for i in range(linhas):
        for j in range(colunas):
            if(j == colunas - 1):
                print(minha_matriz[i][j])
            else:
                print(minha_matriz[i][j], end=" ")
    print()


minha_matriz = []
imprime_matriz(minha_matriz=minha_matriz)
