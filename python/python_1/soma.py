print("Digite uma sequência de valores terminado por zero")

soma = 0

while True:
    valor = int(input("Digite um valor: "))
    soma += valor
    if valor == 0:
        break
print(f"A soma dos valores digitados é: {soma}")
