def divisores(n: int, x: int) -> list[int]:
    '''
    Devolve uma lista com os divisores de *n* que são *<= x*.

    Requer quer 0 <= x <= n

    Exemplos
    >>> divisores(0, 0)
    []
    >>> divisores(12, 5)
    [1, 2, 3, 4]
    >>> divisores(8, 7)
    [1, 2, 4]
    '''
    assert 0 <= x <= n
    if x == 0:
        return []
    else:
        lst = divisores(n, x - 1)
        if n % x == 0:
            lst.append(x)
        return lst
