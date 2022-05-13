class Buscador:
    def busca_sequencial(self, lista, x):
        for i in range(len(lista)):
            if lista[i] == x:
                return i
        return -1

    def busca_binaria(self, lista, x):
        first = 0
        last = len(lista) - 1

        while first <= last:
            half = (first + last) // 2
            if lista[half] == x:
                return half
            else:
                if x < lista[half]:
                    last = half - 1
                else:
                    first = half + 1
        return False


