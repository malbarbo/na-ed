from __future__ import annotations
from dataclasses import dataclass


@dataclass
class No:
    esq: Arvore
    chave: int
    dir: Arvore


Arvore = No | None


def exibe(t: Arvore) -> None:
    r'''
    Exibe um desenho de *t* na horizontal.

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
    >>> exibe(None)
    <BLANKLINE>
    >>> exibe(t0)
    1
    >>> exibe(t1)
    7
    ├── 
    └── 1
    >>> exibe(t2)
    8
    ├── 4
    └── 7
        ├── 
        └── 1
    >>> exibe(t4)
    4
    ├── 8
    │   ├── 4
    │   └── 7
    │       ├── 
    │       └── 1
    └── 6
        ├── 5
        └── 
    '''
    print('\n'.join(linhas(t)))


def linhas(t: Arvore) -> list[str]:
    if t is None:
        return ['']
    elif t.esq is None and t.dir is None:
        return [str(t.chave)]
    else:
        esq = linhas(t.esq)
        esq[0] = '├── ' + esq[0]
        for i in range(1, len(esq)):
            esq[i] = '│   ' + esq[i]

        dir = linhas(t.dir)
        dir[0] = '└── ' + dir[0]
        for i in range(1, len(dir)):
            dir[i] = '    ' + dir[i]

        return [str(t.chave)] + esq + dir
