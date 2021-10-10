n = int(input("Digite um número inteiro: "))

if n > 1 and n % 2 == 1:
    for i in range(2, n):
        if i % 2 == 1:
            if n % i == 0:
                primo = False
                break
            else:
                primo = True
else:
    primo = False
if primo:
    print("primo")
else:
    print("não primo")
