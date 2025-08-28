from __future__ import annotations
from dataclasses import dataclass


@dataclass
class No:
    primeiro: int
    resto: Lista


Lista = No | None


def soma(lst: Lista) -> int:
    '''
    Soma os elementos de *lst*.

    Exemplos
    >>> soma(None)
    0
    >>> soma(No(3, None))
    3
    >>> soma(No(4, No(3, None)))
    7
    >>> soma(No(10, No(4, No(3, None))))
    17
    '''
    if lst is None:
        return 0
    else:
        return lst.primeiro + soma(lst.resto)


def num_itens(lst: Lista) -> int:
    '''
    Devolve a quantidade de itens em *lst*.

    Exemplos
    >>> num_itens(None)
    0
    >>> num_itens(No(3, None))
    1
    >>> num_itens(No(4, No(3, None)))
    2
    >>> num_itens(No(10, No(4, No(3, None))))
    3
    '''
    if lst is None:
        return 0
    else:
        return 1 + num_itens(lst.resto)


def todos_pares(lst: Lista) -> bool:
    '''
    Devolve True se todos os elementos de *lst* são pares, False caso
    contrário.

    Exemplos
    >>> todos_pares(None)
    True
    >>> todos_pares(No(32, None))
    True
    >>> todos_pares(No(4, No(32, None)))
    True
    >>> todos_pares(No(8, No(4, No(32, None))))
    True
    >>> todos_pares(No(7, No(4, No(32, None))))
    False
    '''
    if lst is None:
        return True
    else:
        return lst.primeiro % 2 == 0 and todos_pares(lst.resto)


def contem(lst: Lista, v: int) -> bool:
    '''
    Devolve True se *v* está em *lst*, False caso contrário.

    Exemplos
    >>> contem(None, 3)
    False
    >>> contem(No(8, No(4, No(32, None))), 8)
    True
    >>> contem(No(8, No(4, No(32, None))), 4)
    True
    >>> contem(No(8, No(4, No(32, None))), 40)
    False
    '''
    if lst is None:
        return False
    else:
        return v == lst.primeiro or contem(lst.resto, v)


def copia(lst: Lista) -> Lista:
    '''
    Cria e devolve uma cópia de *lst*.

    Exemplos
    >>> lsta = No(10, No(20, No(30, None)))
    >>> lstb = copia(lsta)
    >>> # quando mudamos lsta,
    >>> # lstb não é alterada pois é uma cópia
    >>> lsta.primeiro = 1
    >>> lsta.resto.primeiro = 2
    >>> lsta.resto.resto.primeiro = 3
    >>> lsta
    No(primeiro=1, resto=No(primeiro=2, resto=No(primeiro=3, resto=None)))
    >>> lstb
    No(primeiro=10, resto=No(primeiro=20, resto=No(primeiro=30, resto=None)))

    Exemplo para o None
    >>> copia(None)
    '''
    if lst is None:
        return None
    else:
        return No(lst.primeiro, copia(lst.resto))


def soma1(lst: Lista) -> None:
    '''
    Modifica *lst* somando 1 a cada elemento de *lst*.

    Exemplos
    >>> p = No(10, No(20, No(30, None)))
    >>> soma1(p)
    >>> p
    No(primeiro=11, resto=No(primeiro=21, resto=No(primeiro=31, resto=None)))
    '''
    if lst is not None:
        lst.primeiro += 1
        soma1(lst.resto)


def duplica(lst: Lista) -> None:
    '''
    Modifica *lst*, inserindo uma cópia de cada nó após o nó original.

    Exemplos
    >>> lst = No(1, No(2, None))
    >>> duplica(lst)
    >>> lst
    No(primeiro=1, resto=No(primeiro=1, resto=No(primeiro=2, resto=No(primeiro=2, resto=None))))
    >>> # A modificação do primeiro nó
    >>> # não pode alterar o nó copiado!
    >>> lst.primeiro = 20
    >>> lst.resto.primeiro
    1
    '''
    if lst is not None:
        duplica(lst.resto)
        lst.resto = No(lst.primeiro, lst.resto)
