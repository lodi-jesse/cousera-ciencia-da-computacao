def menor_nome(nomes):
    menor = str(min((nomes), key=lambda x: len(x.strip()))).upper()

    return menor.strip().capitalize()


print(menor_nome(nomes=['maria', ' josé ', '   PAULO', 'Catarina   ']))
