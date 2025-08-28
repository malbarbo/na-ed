def elevado(a: float, n: int) -> float:
    '''
    Calcula o valor *a^n* (*a* elevado à potência *n*).

    Requer que a != 0 e n >= 0:

    Exemplos
    >>> elevado(2.0, 0)
    1.0
    >>> elevado(2.0, 1)
    2.0
    >>> elevado(2.0, 2)
    4.0
    >>> elevado(2.0, 3)
    8.0
    '''
    if n == 0:
        return 1.0
    else:
        return a * elevado(a, n - 1)
