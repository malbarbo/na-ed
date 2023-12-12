from dataclasses import dataclass

@dataclass
class ArranjoD:
    # TODO: definir!
    pass


def arranjod_vazio() -> ArranjoD:
    '''
    Cria um novo arranho com zero elementos.

    >>> a = arranjod_vazio()
    >>> arranjod_len(a)
    0
    '''
    # TODO: implementar
    return ArranjoD()


def arranjod_len(a: ArranjoD) -> int:
    '''
    Devolve a quantidade de elementos de *a*.

    Exemplos
    >>> a = arranjod_vazio()
    >>> arranjod_acrescenta(a, 2)
    >>> arranjod_len(a)
    1
    >>> arranjod_acrescenta(a, 4)
    >>> arranjod_acrescenta(a, 1)
    >>> arranjod_len(a)
    3
    '''
    # TODO: implementar
    return 0


def arranjod_get(a: ArranjoD, i: int) -> int:
    '''
    Devolve o elemento da posição *i* de *a*.

    Exemplos
    >>> a = arranjod_vazio()
    >>> arranjod_acrescenta(a, 4)
    >>> arranjod_acrescenta(a, 3)
    >>> arranjod_acrescenta(a, 7)
    >>> arranjod_acrescenta(a, -1)
    >>> arranjod_get(a, 0)
    4
    >>> arranjod_get(a, 1)
    3
    >>> arranjod_get(a, 2)
    7
    >>> arranjod_get(a, 3)
    -1
    '''
    # TODO: implementar
    return 0


def arranjod_acrescenta(a: ArranjoD, item: int):
    '''
    Acrescenta *item* no final *a*.

    Exemplos
    >>> a = arranjod_vazio()
    >>> for i in range(1, 1001):
    ...     arranjod_acrescenta(a, i)
    >>> arranjod_get(a, 0)
    1
    >>> arranjod_get(a, 300)
    301
    >>> arranjod_get(a, 999)
    1000
    '''
    # TODO: implementar
    pass
