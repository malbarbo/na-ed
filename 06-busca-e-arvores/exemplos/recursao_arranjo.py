def soma(lst: list[int], n: int) -> int:
    '''
    Soma os primeiros *n* elementos de *lst*.

    Requer que 0 <= n <= len(lst).

    Exemplo
    >>> soma([5, 1, 4, 2, 3], 3)
    10
    '''
    assert 0 <= n <= len(lst)
    if n == 0:
        return 0
    else:
        return lst[n - 1] + soma(lst, n - 1)


def palindromo(lst: list[int]) -> bool:
    '''
    Devolve True se o lst é palíndromo, isto é, tem os mesmos elementos quando
    visto da direita para esquerda e da esquerda para a direita.

    Exemplos
    >>> palindromo([])
    True
    >>> palindromo([2])
    True
    >>> palindromo([1, 1])
    True
    >>> palindromo([2, 1])
    False
    >>> palindromo([2, 1, 1, 2])
    True
    >>> palindromo([2, 1, 0, 1, 2])
    True
    >>> palindromo([2, 1, 0, 1, 1])
    False
    '''
    def _palindromo(lst: list[int], ini: int, fim: int) -> bool:
        return fim <= ini or lst[ini] == lst[fim] and _palindromo(lst, ini + 1, fim - 1)
    return _palindromo(lst, 0, len(lst) - 1)
