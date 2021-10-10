n1 = int(input("Digite um número inteiro: "))
n2 = int(input("Digite outro número inteiro: "))
n3 = int(input("Digite o último número: "))

if (n1 < n2) and (n1 < n3) and (n2 < n3):
    print("Crescente")
else:
    print("não está em ordem crescente")
