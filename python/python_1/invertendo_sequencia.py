lista = []

while True:
    n = int(input("Digite um valor para terminar digite[0]: "))
    if n != 0:
        lista.insert(0, n)
    if n == 0:
        break

for i in lista:
    print(i)
