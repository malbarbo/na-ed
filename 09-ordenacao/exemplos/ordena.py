def ordena(lst: list[int]):
    '''
    Ordena os elementos de *lst* em ordem não decrescente.

    Exemplo

    >>> lst = [5, 2, 4, 6, 1, 3]
    >>> ordena(lst)
    >>> lst
    [1, 2, 3, 4, 5, 6]

    Testes de propriedade
    A seguir, listas com tamanhos n = 0, 1, ..., 10,
    são geradas com os elementos 0, 1, ..., n. Para
    cada lista todas as suas permutações são usadas
    para testar o algoritmo de ordenação.
    >>> from itertools import permutations
    >>> for n in range(0, 11):
    ...     for p in permutations(range(n)):
    ...         lst = list(p)
    ...         ordena(lst)
    ...         assert lst == list(range(n))
    '''
    # TODO: implementar o algoritmo de ordenação!
    lst.sort()
