def busca_binaria(valores: list[int], chave: int) -> int:
    '''
    Se *chave* está presente em *valores*, devolve o índice i tal que
    *valores[i] == chave*. Senão devolve o índice i tal que a inserção de
    *chave* na posição *i* de *valores* mantém *valores* em ordem não
    decrescente.

    Requer que *valores* esteja em ordem não decrescente.

    Exemplos

    >>> busca_binaria([], 10)
    0
    >>> busca_binaria([7], 4)
    0
    >>> busca_binaria([7], 8)
    1
    >>> busca_binaria([7], 7)
    0
    >>> busca_binaria([6, 8, 10, 12, 20], 7)
    1
    >>> busca_binaria([6, 8, 10, 12, 20], 10)
    2
    >>> busca_binaria([6, 8, 10, 12, 20], 11)
    3
    >>> busca_binaria([6, 8, 10, 12, 20], 12)
    3
    >>> busca_binaria([6, 8, 10, 12, 20], 17)
    4
    >>> busca_binaria([6, 8, 10, 12, 20], 20)
    4
    >>> busca_binaria([6, 8, 10, 12, 20], 21)
    5


    Testes de propriedade

    O teste a seguir cria uma lista 0, 2, ..., 98 e realiza uma busca binária
    para 0, 1, 2, ..., 99.

    >>> lst = list(range(0, 100, 2))
    >>> for i in range(100):
    ...     assert busca_binaria(lst, i) == (i + 1) // 2
    '''

    ini = 0
    fim = len(valores) - 1
    while ini <= fim:
        m = (ini + fim) // 2
        if chave == valores[m]:
            return m
        elif chave < valores[m]:
            fim = m - 1
        else: # chave > valores[m]
            ini = m + 1
    return ini
