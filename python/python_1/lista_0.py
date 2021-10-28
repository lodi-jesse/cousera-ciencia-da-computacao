lista = []

while True:
    n = int(input("Digite um sequencia de número terminado em (0) e digite (0) para parar:  "))
    if n != 0:
        lista.append(n)
    if n == 0:
        break
print(sorted(lista, reverse=True))
