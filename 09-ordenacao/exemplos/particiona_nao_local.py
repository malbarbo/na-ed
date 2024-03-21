def particiona(lst: list[int], ini: int, fim: int) -> int:
    '''
    >>> lst = [2, 8, 7, 1, 3, 5, 6, 4]
    >>> particiona(lst, 0, len(lst))
    3
    >>> lst
    [2, 1, 3, 4, 8, 7, 5, 6]
    '''
    assert ini < fim
    pivo = lst[fim - 1]
    menores = []
    maiores_iguais = []
    for i in range(ini, fim - 1):
        if lst[i] < pivo:
            menores.append(lst[i])
        else:
            maiores_iguais.append(lst[i])
    # Copia os menores do que o pivo para lst
    for i in range(len(menores)):
        lst[i] = menores[i]
    # Copia o pivo para lst
    p = len(menores)
    lst[p] = pivo
    # Copias os maiores ou iguais ao pivo para lst
    for j in range(len(maiores_iguais)):
        lst[p + j + 1] = maiores_iguais[j]
    # Retorna o índice do pivo
    return p
