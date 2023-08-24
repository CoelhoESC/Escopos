"""
Funções (def) - Escopo local e global de variaveis!
"""
variavel = 'valor'  # Escopo Global


def func():
    print(variavel)  # Mostra o valor da variavel global


def func2():
    variavel = 'Outro valor'  # global variavel
    print(variavel)
    # A variavel muda de valor, pois é um escopo Local, a variavel Global irá continuar com seu valor para outros code!


def func3(arg=None):  # Trocando o valor da variavel global! Usando paramentros!
    arg = arg.replace('v', 'c')
    return arg


if '__main__' == __name__:
    func()

    func2()  # Valor da variavel global não é mudado
    print(variavel)  # Escopo Global

    outra_variavel = func3(arg=variavel)  # Troco valor, sem mexer na variavel global!
    print(outra_variavel)
    print(variavel)  # Escopo Global
