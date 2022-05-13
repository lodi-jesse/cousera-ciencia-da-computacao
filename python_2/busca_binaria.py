def busca(lista, elemento):
    first = 0
    last = len(lista) - 1

    while first <= last:
        half = (first + last) // 2
        print(half)
        if lista[half] == elemento:
            return half
        else:
            if elemento < lista[half]:
                last = half - 1
            else:
                first = half + 1
    return False


print(busca([2, 6, 5, 7, 9], 2))
