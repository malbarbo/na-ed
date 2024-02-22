from __future__ import annotations
from dataclasses import dataclass


@dataclass
class No:
    esq: Arvore
    val: int
    dir: Arvore


Arvore = No | None


def busca(t: Arvore, val: int) -> bool:
    r'''
    Devolve True se *val* está em *t*, False caso contrário.

    Requer que *t* seja uma árvore binária de busca.

    Exemplos
                t
              4
            /   \
         /         \
        1  esq      7 dir
      /   \       /
    -3     2     5
            \
             3

    >>> esq = No(No(None, -3, None), 1, No(None, 2, No(None, 3, None)))
    >>> dir = No(No(None, 5, None), 7, None)
    >>> t = No(esq, 4, dir)
    >>> busca(None, 10)
    False
    >>> busca(t, 0)
    False
    >>> busca(t, 1)
    True
    >>> busca(t, 2)
    True
    >>> busca(t, 3)
    True
    >>> busca(t, 4)
    True
    >>> busca(t, 5)
    True
    >>> busca(t, 6)
    False
    >>> busca(t, 7)
    True
    '''
    if t is None:
        return False
    elif val == t.val:
        return True
    elif val < t.val:
        return busca(t.esq, val)
    else:  # val > t.val
        return busca(t.dir, val)


def busca_iter(t: Arvore, val: int) -> bool:
    r'''
    Devolve True se *val* está em *t*, False caso contrário.

    Requer que *t* seja uma árvore binária de busca.

    Exemplos
                t
              4
            /   \
         /         \
        1  esq      7 dir
      /   \       /
    -3     2     5
            \
             3

    >>> esq = No(No(None, -3, None), 1, No(None, 2, No(None, 3, None)))
    >>> dir = No(No(None, 5, None), 7, None)
    >>> t = No(esq, 4, dir)
    >>> busca_iter(None, 10)
    False
    >>> busca_iter(t, 0)
    False
    >>> busca_iter(t, 1)
    True
    >>> busca_iter(t, 2)
    True
    >>> busca_iter(t, 3)
    True
    >>> busca_iter(t, 4)
    True
    >>> busca_iter(t, 5)
    True
    >>> busca_iter(t, 6)
    False
    >>> busca_iter(t, 7)
    True
    '''
    r = t
    while r is not None:
        if val == r.val:
            return True
        elif val < r.val:
            r = r.esq
        else:  # val > r.val
            r = r.dir
    return False
