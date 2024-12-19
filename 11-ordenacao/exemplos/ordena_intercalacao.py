def ordena_intercalacao(lst: list[int]):
    '''
    Ordena os elementos de *lst* em ordem não decrescente.

    Exemplo

    >>> lst = [5, 2, 4, 6, 1, 3]
    >>> ordena_intercalacao(lst)
    >>> lst
    [1, 2, 3, 4, 5, 6]

    Testes de propriedade
    A seguir, listas com tamanhos n = 0, 1, ..., 10,
    são geradas com os elementos 0, 1, ..., n. Para
    cada lista todas as suas permutações são usadas
    para testar o algoritmo de ordena_intercalacaoção.
    >>> from itertools import permutations
    >>> for n in range(0, 11):
    ...     for p in permutations(range(n)):
    ...         lst = list(p)
    ...         ordena_intercalacao(lst)
    ...         assert lst == list(range(n))
    '''
    if len(lst) > 1:
        m = len(lst) // 2
        a = lst[:m]
        b = lst[m:]
        ordena_intercalacao(a)
        ordena_intercalacao(b)
        intercala(lst, a, b)


def intercala(lst: list[int], a: list[int], b: list[int]):
    '''
    Faz a intercalação em ordem não decrescente dos elementos
    de *a* e *b* e armazena o resultado em *lst*.

    Requer que len(lst) = len(a) + len(b).
    Requer que a e b estejam em ordem não decrescente.

    Exemplos
    >>> lst = [0, 0, 0, 0, 0, 0, 0]
    >>> intercala(lst, [1, 6], [3, 5, 6, 8, 10])
    >>> lst
    [1, 3, 5, 6, 6, 8, 10]
    >>> intercala(lst, [3, 5, 6, 8, 10], [1, 6])
    >>> lst
    [1, 3, 5, 6, 6, 8, 10]
    '''
    assert len(lst) == len(a) + len(b)
    i = 0
    j = 0
    k = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            lst[k] = a[i]
            i += 1
        else:
            lst[k] = b[j]
            j += 1
        k += 1
    # Copia o restante de a
    while i < len(a):
        lst[k] = a[i]
        i += 1
        k += 1
    # Copia o restante de b
    while j < len(b):
        lst[k] = b[j]
        j += 1
        k += 1
