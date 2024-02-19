from __future__ import annotations
from dataclasses import dataclass


@dataclass
class No:
    esq: Arvore
    val: int
    dir: Arvore


Arvore = No | None


def num_folhas(t: Arvore) -> int:
    '''
    Determina a quantidade de folhas em *t*.
    Uma folha é um nó sem nehum filho.

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
    >>> num_folhas(t1)
    1
    >>> num_folhas(t2)
    2
    >>> num_folhas(t3)
    1
    >>> num_folhas(t4)
    3
    >>> num_folhas(None)
    0
    '''
    if t is None:
        return 0
    elif t.esq is None and t.dir is None:
        return 1
    else:
        return num_folhas(t.esq) + num_folhas(t.dir)
