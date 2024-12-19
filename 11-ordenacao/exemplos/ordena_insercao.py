def ordena_insercao(lst: list[int]):
    '''
    Ordena os elementos de *lst* em ordem não decrescente.

    Exemplo

    >>> lst = [5, 2, 4, 6, 1, 3]
    >>> ordena_insercao(lst)
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
    ...         ordena_insercao(lst)
    ...         assert lst == list(range(n))
    '''
    # Invariante: o subarranjo lst[:i] contém os
    # elementos inicialmente em lst[:i] em ordem
    # não decrescente.
    for i in range(1, len(lst)):
        j = i
        while j > 0 and lst[j - 1] > lst[j]:
            lst[j - 1], lst[j] = lst[j], lst[j - 1]
            j -= 1
