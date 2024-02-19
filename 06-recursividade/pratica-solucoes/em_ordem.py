def em_ordem(lst: list[int]) -> bool:
    '''
    Devolve True se os elementos de *lst* estão em ordem não decrescente, False
    caso contrário.

    Exemplos
    >>> em_ordem([])
    True
    >>> em_ordem([4])
    True
    >>> em_ordem([7, 5])
    False
    >>> em_ordem([5, 7])
    True
    >>> em_ordem([5, 5, 7, 12])
    True
    >>> em_ordem([5, 5, 7, 12, 11])
    False
    '''
    def _em_ordem(lst: list[int], n: int) -> bool:
        # Verifica se os últimos len(lst) - n elementos de lst estão em ordem
        if n >= len(lst) - 1:
            return True
        else:
            return lst[n] <= lst[n + 1] and _em_ordem(lst, n + 1)
        # return n >= len(lst) - 1 or lst[n] <= lst[n + 1] and _em_ordem(n + 1)

    return _em_ordem(lst, 0)
