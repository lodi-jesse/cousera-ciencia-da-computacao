def maiusculas(frase):
    res = " "
    for i in range(len(frase)):
        if frase[i].isupper():
            res += frase[i]
    return res



