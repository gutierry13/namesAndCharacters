perguntaInput = str(input('Informe o texto: '))


def quebraTextos(texto):
    totalCaracter = 0
    quebraTexto = texto.split()
    numeroPalavras = len(quebraTexto)
    for x in range(numeroPalavras):
        letras = len(quebraTexto[x])
        totalCaracter += letras
    print('O número total de palavras é: %d' % (numeroPalavras))
    print('O número total de caracteres é: %d' % (totalCaracter))


quebraTextos(perguntaInput)
