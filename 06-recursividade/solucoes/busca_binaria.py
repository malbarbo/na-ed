def busca_binaria(lst: list[int], val: int) -> bool:
    '''
    Devolve True se *val* está em *lst*, e False caso contrário.

    Requer que os elementos de *lst* estejam em ordem não decrescente.

    Exemplos
    >>> busca_binaria([], 10)
    False
    >>> busca_binaria([10], 10)
    True
    >>> lst = [3, 6, 8, 10, 12, 12, 16, 20]
    >>> for val in range(25):
    ...     # o resultado da busca binária deve ser o mesmo que o do operador in
    ...     assert busca_binaria(lst, val) == (val in lst)
    '''
    def _busca_binaria(lst: list[int], val: int, ini: int, fim: int) -> bool:
        if fim < ini:
            return False
        else:
            m = (ini + fim) // 2
            if val == lst[m]:
                return True
            elif val < lst[m]:
                return _busca_binaria(lst, val, ini, m - 1)
            else: # val > lst[n]
                return _busca_binaria(lst, val, m + 1, fim)
    return _busca_binaria(lst, val, 0, len(lst) - 1)
