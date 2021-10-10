x = 9844


while True:
    unidade = x % 10
    resto = x // 10
    comparaUnidade = resto % 10
    x = resto
    if unidade == comparaUnidade:
        print("Adjacente")
    elif resto == 0:
       break
