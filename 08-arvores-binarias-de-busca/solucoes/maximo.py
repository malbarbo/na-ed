from __future__ import annotations
from dataclasses import dataclass


@dataclass
class No:
    esq: Arvore
    chave: int
    dir: Arvore


Arvore = No | None


def maximo(t: Arvore) -> int | None:
    r'''
    Devolve o valor máximo entre todos os elementos de *t* or None se *t* é
    None.

    Exemplos
          t4  4
            /   \
         /         \
    t2  8           6  t3
      /   \       /
     4  t1 7     5
            \
          t0 1

    >>> t0 = No(None, 1, None)
    >>> t1 = No(None, 7, No(None, 1, None))
    >>> t2 = No(No(None, 4, None), 8, t1)
    >>> t3 = No(No(None, 5, None), 6, None)
    >>> t4 = No(t2, 4, t3)
    >>> maximo(None) is None
    True
    >>> maximo(t0)
    1
    >>> maximo(t2)
    8
    >>> maximo(t3)
    6
    >>> maximo(t4)
    8
    '''
    def _maximo(a: int | None, b: int | None) -> int | None:
        if a is None:
            return b
        if b is None:
            return a
        else:
            return max(a, b)
    if t is None:
        return None
    else:
        return _maximo(t.chave, _maximo(maximo(t.esq), maximo(t.dir)))
