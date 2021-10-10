def maximo(x, y, z):
    if x == y == z:
        return x
    if x > y and x > z or (x == y > z or x > y == z or x == z > y):
        return x
    elif y > x and y > z or (y == x > z or y > x == z or y == z > x):
        return y
    elif z > x and z > y or (z == x > y or z > x == y or z == y > x):
        return z


print(maximo(x=int(input("Digite um número: ")),
             y=int(input("digite um número: ")),
             z=int(input("digite um número: "))))

