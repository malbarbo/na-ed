def soma(n: int) -> int:
    '''
    Devolve a soma de todos os números naturais até *n*.

    Requer que n >= 0.

    Exemplos
    >>> soma(0)
    0
    >>> soma(4)
    10
    '''
    if n <= 0:
        return 0
    else:
        return n + soma(n - 1)


def lista_n(n: int) -> list[int]:
    '''
    Devolve a lista [1, 2, ..., *n*].

    Requer que n >= 0.

    Exemplos
    >>> lista_n(0)
    []
    >>> lista_n(3)
    [1, 2, 3]
    '''
    if n <= 0:
        return []
    else:
        lst = lista_n(n - 1)
        lst.append(n)
        return lst
