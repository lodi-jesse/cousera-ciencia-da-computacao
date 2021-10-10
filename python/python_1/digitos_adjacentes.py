n = int(input("Digite um número inteiro: "))

while True:
    unidade = n % 10
    resto = n // 10
    if resto > 0:
        comparaResto = resto % 10
        n = resto
        if unidade == comparaResto:
            adjacente = True
            break
    else:
        adjacente = False
    if resto == 0:
        break
if adjacente:
    print("sim")
else:
    print("não")
