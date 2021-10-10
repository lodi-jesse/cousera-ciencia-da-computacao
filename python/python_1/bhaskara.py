import math


def delta(a, b, c):
    return b ** 2 - 4 * a * c


def main():
    a_digitado = float(input("Digite um valor para a: "))
    b_digitado = float(input("Digite um valor para b: "))
    c_digitado = float(input("Digite um valor para c: "))
    imprime_raizes(a_digitado, b_digitado, c_digitado)


def imprime_raizes(a, b, c):
    d = delta(a, b, c)
    if d < 0:
        print("Esta equação não possui raízes reais")
    elif d == 0:
        raiz1 = (- b + (math.sqrt(d))) / (2*a)
        print(f"O valor desta raiz é {raiz1}")
    else:
        raiz1 = (- b + (math.sqrt(d))) / (2 * a)
        raiz2 = (- b - (math.sqrt(d))) / (2 * a)
        if raiz1 < raiz2:
            print(f"As raízes destas equações são {raiz1} e {raiz2}")
        else:
            print(f"As raízes destas equações são {raiz2} e {raiz1}")


main()
