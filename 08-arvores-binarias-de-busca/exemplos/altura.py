from __future__ import annotations
from dataclasses import dataclass


@dataclass
class No:
    esq: Arvore
    chave: int
    dir: Arvore


Arvore = No | None


def altura(t: Arvore) -> int:
    r'''
    Devolve a altura da árvore *t*, isto é, o comprimeiro do caminho mais longo
    da raíz até um no folha. Devolve -1 se *t* é None.

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
    >>> altura(None)
    -1
    >>> altura(t1)
    1
    >>> altura(t4)
    3
    '''
    if t is None:
        return -1
    else:
        return 1 + max(altura(t.esq), altura(t.dir))
