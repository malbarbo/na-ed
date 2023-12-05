from dataclasses import dataclass

@dataclass
class ArranjoD:
    # TODO: definir!
    pass


def arranjod_vazio() -> ArranjoD:
    '''
    Cria uma nova lista vazia.

    >>> lst = arranjod_vazio()
    >>> arranjod_len(lst)
    0
    '''
    return ArranjoD()


def arranjod_len(a: ArranjoD) -> int:
    '''
    Devolve a quantidade de elementos de *lst*.

    Exemplos
    >>> lst = arranjod_vazio()
    >>> arranjod_acrescenta(lst, 2)
    >>> arranjod_len(lst)
    1
    >>> arranjod_acrescenta(lst, 4)
    >>> arranjod_acrescenta(lst, 1)
    >>> arranjod_len(lst)
    3
    '''
    # TODO: implementar
    return 0


def arranjod_pos(a: ArranjoD, i: int) -> int:
    '''
    Devolve o elementos que está na posição *i* de *lst*.

    Exemplos
    >>> lst = arranjod_vazio()
    >>> arranjod_acrescenta(lst, 4)
    >>> arranjod_acrescenta(lst, 3)
    >>> arranjod_acrescenta(lst, 7)
    >>> arranjod_acrescenta(lst, -1)
    >>> arranjod_pos(lst, 0)
    4
    >>> arranjod_pos(lst, 1)
    3
    >>> arranjod_pos(lst, 2)
    7
    >>> arranjod_pos(lst, 3)
    -1
    '''
    # TODO: implementar
    return 0


def arranjod_acrescenta(a: ArranjoD, item: int):
    '''
    Acrescenta *item* no final *lst*.

    Exemplos
    >>> lst = arranjod_vazio()
    >>> for i in range(1, 1001):
    ...     arranjod_acrescenta(lst, i)
    >>> arranjod_pos(lst, 0)
    1
    >>> arranjod_pos(lst, 300)
    301
    >>> arranjod_pos(lst, 999)
    1000
    '''
    # TODO: implementar
    pass
