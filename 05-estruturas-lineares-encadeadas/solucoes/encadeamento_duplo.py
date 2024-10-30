from __future__ import annotations
from dataclasses import dataclass


@dataclass
class No:
    ante: No | None
    item: int
    prox: No | None


def lista_nos(lst: list[int]) -> No | None:
    '''
    Devolve um encadeamento com os elementos de *lst*.

    Exemplos
    >>> lista_nos([])
    >>> lista_nos([6, 2, 4])
    No(ante=None, item=6, prox=No(ante=..., item=2, prox=No(ante=..., item=4, prox=None)))
    '''
    # Cria um nó inicial para facilitar
    if lst == []:
        return None
    inicio = No(None, lst[0], None)
    ultimo = inicio
    for i in range(1, len(lst)):
        ultimo.prox = No(ultimo, lst[i], None)
        ultimo = ultimo.prox
    return inicio


def troca_prox(p: No):
    '''
    Troca *p* de lugar com *p.prox*.
    Requer que *p.prox* seja um No.

    Exemplos
    >>> p = lista_nos([7, 4, 6])
    >>> troca_prox(p)
    >>> p.ante
    No(ante=None, item=4, prox=No(ante=..., item=7, prox=No(ante=..., item=6, prox=None)))
    >>> p.item
    7
    >>> p.ante.item
    4
    >>> p.prox.item
    6
    '''
    assert p.prox is not None
    # remove p.prox e chama de q
    q = p.prox
    p.prox = q.prox
    if p.prox is not None:
        p.prox.ante = p
    # insere q
    q.ante = p.ante
    if q.ante is not None:
        q.ante.prox = q
    q.prox = p
    p.ante = q


def troca_ante(p: No):
    '''
    Troca *p* de lugar com *p.ante*.
    Requer que *p.ante* seja um No.

    Exemplos
    >>> p = lista_nos([7, 4, 6]).prox
    >>> troca_ante(p)
    >>> p
    No(ante=None, item=4, prox=No(ante=..., item=7, prox=No(ante=..., item=6, prox=None)))
    >>> p.item
    4
    >>> p.prox.item
    7
    >>> p.prox.prox.item
    6
    '''
    assert p.ante is not None
    troca_prox(p.ante)
