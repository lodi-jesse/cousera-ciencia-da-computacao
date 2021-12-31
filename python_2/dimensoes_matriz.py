def dimensoes(minha_matriz):

    matriz = minha_matriz
    cont = 0
    for x in matriz:
        cont += 1
        if cont == 1:
            j = len(x)
    i = len(matriz)
    print(f"{i}X{j}")


minha_matriz = [[1, 2, 3]]
dimensoes(minha_matriz=minha_matriz)
