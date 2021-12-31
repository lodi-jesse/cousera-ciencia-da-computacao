m1 = [[1], [2], [3]]
m2 = [[1, 2, 3]]


def sao_multiplicaveis(m1, m2):
    n1 = len(m1[0])
    n2 = len(m2)
    if n1 == n2:
        return True
    else:
        return False


print(sao_multiplicaveis(m1, m2))
