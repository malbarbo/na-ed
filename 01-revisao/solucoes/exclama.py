def exclama(s: str, n: int) -> str:
    '''
    Cria uma string adicionando *n* símbolos '!' no final de *s*.

    Requer que n >= 0

    Exemplos
    >>> exclama('nada', 0)
    'nada'
    >>> exclama('Gol', 4)
    'Gol!!!!'
    '''
    if n == 0:
        ex = s
    else:
        ex = exclama(s, n - 1) + '!'
    return ex
