def remove_repetidos(lista):
    lista_nova = []
    for i in lista:
        if i not in lista_nova:
            lista_nova.append(i)
    return sorted(lista_nova)


remove_repetidos(lista=[1, 2, 3])
