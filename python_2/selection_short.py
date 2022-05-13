def ordena(lista):
    for i in range(len(lista)):
        for j in range(len(lista)-1):
            if lista[i] < lista[j]:
                aux = lista[j]
                lista[j] = lista[i]
                lista[i] = aux
    return lista
