perguntarNome = str(input('Qual o nome?: '))


def recebeNome(nome):
    iniciais = []
    arrayNome = nome.split()
    for x in range(len(arrayNome)):
        if arrayNome[x] not in ['e', 'do', 'da', 'dos', 'das', 'de', 'di', 'du']:
            quebrarNome = arrayNome[x][0]
            iniciais.append(quebrarNome)
            final = ''.join(iniciais).upper()
    print(final)


recebeNome(perguntarNome)
