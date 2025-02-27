from __future__ import annotations
from dataclasses import dataclass


@dataclass
class No:
    esq: Arvore
    chave: int
    dir: Arvore


Arvore = No | None


def chaves_nivel(t: Arvore, n: int) -> list[int]:
    r'''
    Devolve os nós que estão no nível *n* de *t*.

    Exemplos

          t4  4
            /   \
         /         \
    t2  8           6  t3
      /   \       /
     4  t1 7     5
            \
             1

    >>> t1 = No(None, 7, No(None, 1, None))
    >>> t2 = No(No(None, 4, None), 8, t1)
    >>> t3 = No(No(None, 5, None), 6, None)
    >>> t4 = No(t2, 4, t3)
    >>> chaves_nivel(None, 0)
    []
    >>> chaves_nivel(t4, 0)
    [4]
    >>> chaves_nivel(t4, 1)
    [8, 6]
    >>> chaves_nivel(t4, 2)
    [4, 7, 5]
    >>> chaves_nivel(t4, 3)
    [1]
    '''
    if t is None:
        return []
    elif n == 0:
        return [t.chave]
    else:
        return chaves_nivel(t.esq, n - 1) + chaves_nivel(t.dir, n - 1)
