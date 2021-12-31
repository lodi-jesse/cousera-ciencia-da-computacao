def dimensoes(minha_matriz):

    matriz = minha_matriz
    cont = 0
    for x in matriz:
        cont += 1
        if cont == 1:
            j = len(x)
    i = len(matriz)
    return i, j


def soma_matrizes(m1, m2):
    result = []
    x = dimensoes(minha_matriz=m1)
    y = dimensoes(minha_matriz=m2)
    if x == y:
        for i in range(len(m1)):
            linha = []
            for j in range(len(m1[0])):
                list.append(linha, m1[i][j] + m2[i][j])
            list.append(result, linha)
        return result
    else:
        return False


m1 = [[1]]
m2 = [[2]]
soma_matrizes(m1=m1, m2=m2)

