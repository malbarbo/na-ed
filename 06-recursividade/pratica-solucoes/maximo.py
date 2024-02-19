from __future__ import annotations
from dataclasses import dataclass


@dataclass
class No:
    primeiro: int
    resto: Lista


Lista = No | None


def maximo(lst: Lista) -> int | None:
    '''
    Devolve o valor máximo de *lst* ou None se *lst* é None.

    Exemplos
    >>> maximo(None) is None
    True
    >>> maximo(No(2, None))
    2
    >>> maximo(No(4, No(1, No(7, No(2, None)))))
    7
    '''
    if lst is None:
        return None
    elif (m := maximo(lst.resto)) is None:
        return lst.primeiro
    else:
        return max(lst.primeiro, m)
