def menor_nome(nomes):
    menor = str(min((nomes), key=lambda x: len(x.strip()))).upper()

    return menor


print(menor_nome(nomes=['maria', ' josé ', '   PAULO', 'Catarina   ']))
