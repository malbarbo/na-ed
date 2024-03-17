def ordena_selecao(lst: list[int]):
    '''
    Ordena os elementos de *lst* em ordem não decrescente.

    Exemplo

    >>> lst = [5, 2, 4, 6, 1, 3]
    >>> ordena_selecao(lst)
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
    ...         ordena_selecao(lst)
    ...         assert lst == list(range(n))
    '''
    # Invariante: o subarranjo lst[:i]
    # contém os i menores elementos
    # do arranjo original lst.
    for i in range(len(lst)):
        # Encontra o índice do menor
        m = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[m]:
                m = j
        # Coloca o menor na posição i
        lst[i], lst[m] = lst[m], lst[i]
