from __future__ import annotations
from dataclasses import dataclass


@dataclass
class No:
    esq: Arvore
    chave: int
    dir: Arvore


Arvore = No | None


def balanceada(t: Arvore) -> bool:
    r'''
    Devolve True se *t* é balanceada, False caso contrário.
    Uma árvore é balanceada se ela é vazia, ou se a altura
    das suas su árvores diferem em no máximo 1

    Exemplos
          t4  4
            /   \
         /         \
    t2  8           6  t3
      /   \
     4  t1 7
            \
          t0 1

    >>> t0 = No(None, 1, None)
    >>> t1 = No(None, 7, No(None, 1, None))
    >>> t2 = No(No(None, 4, None), 8, t1)
    >>> t3 = No(None, 6, None)
    >>> t4 = No(t2, 4, t3)
    >>> balanceada(None)
    True
    >>> balanceada(t1)
    True
    >>> balanceada(t2)
    True
    >>> balanceada(t4)
    False
    '''
    def altura_balanceada(t: Arvore) -> int | None:
        # Devolve a altura se a árvore é balanceada ou None se ela não é
        # balanceada.
        if t is None:
            return 0
        else:
            hesq = altura_balanceada(t.esq)
            hdir = altura_balanceada(t.dir)
            if hesq is not None and hdir is not None and abs(hesq - hdir) <= 1:
                return max(hesq, hdir) + 1
            else:
                return None
    return altura_balanceada(t) is not None
