def intercala(lst: list[int], ini: int, meio: int, fim: int):
    '''
    Faz a intercalação em ordem não decrescente dos elementos de lst[ini:meio]
    e lst[meio:fim] de maneira que lst[ini:fim] fique em ordem não decrescente.

    Requer que lst[ini:meio] e lst[meio:fim] estejam em ordem não decrescente.
    Requer que 0 <= ini <= meio <= fim <= len(lst)

    Exemplos
    >>> lst = [1, 6, 3, 5, 6, 8, 10]
    >>> intercala(lst, 0, 2, len(lst))
    >>> lst
    [1, 3, 5, 6, 6, 8, 10]
    >>> lst = [3, 5, 6, 8, 10, 1, 6]
    >>> intercala(lst, 0, 5, len(lst))
    >>> lst
    [1, 3, 5, 6, 6, 8, 10]
    '''
    assert 0 <= ini <= meio <= fim <= len(lst)
    a = lst[ini:meio]
    b = lst[meio:fim]
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
