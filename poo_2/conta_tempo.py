import random


class ContaTempos:
    def lista_aleatoria(self, n):
        lista = [0 for x in range(n)]
        for i in range(n):
            lista[i] = random.randrange(1000)  # gera numero aleatorios de 0 há 999
        return lista


x = ContaTempos.lista_aleatoria(n=5)
print(x)
