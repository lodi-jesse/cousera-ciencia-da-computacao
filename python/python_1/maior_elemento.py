def maior_elemento(lista):
    c = 0
    for i in lista:
        c += 1
        if c == 1:
            maior = i
        else:
            if i > maior:
                maior = i
    return maior


maior_elemento(lista=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
