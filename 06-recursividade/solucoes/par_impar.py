def par(n: int) -> bool:
    '''
    Devolve True se *n* é par, e False caso contrário.

    Requer que n >= 0.

    Exemplos
    >>> par(0)
    True
    >>> par(1)
    False
    >>> par(4)
    True
    >>> par(7)
    False
    '''
    assert n >= 0
    if n == 0:
        return True
    else:
        return impar(n - 1)
    # return n == 0 or impar(n - 1)


def impar(n: int) -> bool:
    '''
    Devolve True se *n* é ímpar, e False caso contrário.

    Requer que n >= 0.

    Exemplos
    >>> impar(0)
    False
    >>> impar(1)
    True
    >>> impar(4)
    False
    >>> impar(7)
    True
    '''
    assert n >= 0
    if n == 0:
        return False
    else:
        return par(n - 1)
    # return n != 0 and par(n - 1)
