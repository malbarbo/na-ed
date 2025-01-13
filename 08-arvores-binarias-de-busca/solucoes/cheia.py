from __future__ import annotations
from dataclasses import dataclass


@dataclass
class No:
    esq: Arvore
    chave: int
    dir: Arvore


Arvore = No | None


def cheia(t: Arvore) -> bool:
    r'''
    Devolve True se *t* é uma árvore cheia, isto é, todos os nós tem grau 0 ou
    2. Devolve False caso contrário.

    Exemplos
          t4  4
            /   \
         /        \
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
    >>> cheia(None)
    True
    >>> cheia(t4)
    False
    >>> cheia(t2)
    False
    >>> cheia(t1)
    False
    >>> t1.esq = No(None, 5, None)
    >>> cheia(t1)
    True
    >>> cheia(t3)
    False
    >>> t3.dir = No(None, 5, None)
    >>> cheia(t3)
    True
    >>> cheia(t2)
    True
    >>> cheia(t4)
    True
    '''
    if t is None:
        return True
    else:
        grau = int(t.esq is None) + int(t.dir is None)
        return grau != 1 and cheia(t.esq) and cheia(t.dir)
