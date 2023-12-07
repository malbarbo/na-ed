from array import array
from dataclasses import dataclass


@dataclass
class ArranjoD:
    '''
    Um aranjo dinâmico implementado com um arranjo de tamanho fixo. O arranjo
    *valores* sempre tem exatamente os elementos do arranjo dinâmico.

    Quando um elemento é adicionado, um novo arranjo de tamanho fixo com uma
    posição a mais que *valores* é criado. Os elementos de *valores* são
    copiados para o novo arranjo e o novo elemento é colocado na última
    posição.
    '''
    valores: array


def arranjod_vazio() -> ArranjoD:
    '''
    Cria um arranjo com zero elementos

    >>> a = arranjod_vazio()
    >>> arranjod_len(a)
    0
    '''
    return ArranjoD(array(0))


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
    return len(a.valores)


def arranjod_get(a: ArranjoD, i: int) -> int:
    '''
    Devolve o elementos que está na posição *i* de *a*.

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
    return a.valores[i]


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
    n = arranjod_len(a)
    novo = array(n + 1)
    for i in range(n):
        novo[i] = a.valores[i]
    novo[n] = item
    a.valores = novo
