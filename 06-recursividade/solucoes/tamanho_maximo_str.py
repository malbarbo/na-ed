def tamanho_maximo_str(lst: list[str]) -> int:
    '''
    Devolve o tamanho máximo entre todas as strings de *lst*.

    Exemplos
    >>> tamanho_maximo_str([])
    0
    >>> tamanho_maximo_str(['abc'])
    3
    >>> tamanho_maximo_str(['de', 'casa', 'a'])
    4
    '''
    def _tamanho_maximo_str(lst: list[str], n: int) -> int:
        # devolve o tamanho máximo entre as primeiras *n* strings de *lst*.
        if n == 0:
            return 0
        else:
            return max(len(lst[n - 1]), _tamanho_maximo_str(lst, n - 1))
    return _tamanho_maximo_str(lst, len(lst))
