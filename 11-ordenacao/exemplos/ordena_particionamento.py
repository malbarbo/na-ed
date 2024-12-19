def ordena_particionamento(lst: list[int], ini: int, fim: int):
    '''
    Ordena o subarranjo lst[ini:fim] em ordem não decrescente.

    Requer que 0 <= i <= fim <= len(lst).

    Exemplo

    >>> lst = [5, 2, 4, 6, 1, 3]
    >>> ordena_particionamento(lst, 0, len(lst))
    >>> lst
    [1, 2, 3, 4, 5, 6]

    Testes de propriedade
    A seguir, listas com tamanhos n = 0, 1, ..., 10,
    são geradas com os elementos 0, 1, ..., n. Para
    cada lista todas as suas permutações são usadas
    para testar o algoritmo de ordena_particionamentoção.
    >>> from itertools import permutations
    >>> for n in range(0, 11):
    ...     for p in permutations(range(n)):
    ...         lst = list(p)
    ...         ordena_particionamento(lst, 0, len(lst))
    ...         assert lst == list(range(n))
    '''
    # Se o problema não é trivial
    if ini < fim - 1:
        # Divide em dois subproblemas
        p = particiona(lst, ini, fim)

        # Conquista recursivamente
        ordena_particionamento(lst, ini, p)
        ordena_particionamento(lst, p + 1, fim)


def particiona(lst: list[int], ini: int, fim: int) -> int:
    '''
    Reorganiza os elementos de lst[ini:fim] e devolve um índice p de maneira
    que os elementos de lst[ini:p] são menores ou iguais que lst[p:fim].

    Requer que 0 <= ini <= fim <= len(lst)

    Exemplo
    >>> lst = [2, 8, 7, 1, 3, 5, 6, 4]
    >>> particiona(lst, 0, len(lst))
    3
    >>> lst
    [2, 1, 3, 4, 7, 5, 6, 8]
    '''
    assert 0 <= ini <= fim <= len(lst)
    pivo = lst[fim - 1]
    i = ini - 1
    for j in range(ini, fim - 1):
        if lst[j] <= pivo:
            i += 1
            lst[i], lst[j] = lst[j], lst[i]
    lst[i + 1], lst[fim - 1] = lst[fim - 1], lst[i + 1]
    return i + 1

