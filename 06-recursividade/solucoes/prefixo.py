from __future__ import annotations
from dataclasses import dataclass


@dataclass
class No:
    primeiro: int
    resto: Lista


Lista = No | None


def prefixo(lsta: Lista, lstb: Lista) -> bool:
    '''
    Devolve True se *lsta* é prefixo de *lstb*, isto é, *lstb* começa com
    *lsta*. Devolve False caso contrário.

    Exemplos
    >>> prefixo(None, None)
    True
    >>> prefixo(None, No(10, No(20, None)))
    True
    >>> prefixo(No(10, None), None)
    False
    >>> prefixo(No(10, No(20, None)), No(10, No(20, No(30, No(40, None)))))
    True
    >>> prefixo(No(10, No(2, None)), No(10, No(20, No(30, No(40, None)))))
    False
    '''
    # None é prefixo de qualquer lista
    if lsta is None:
        return True
    # Se lsta não é None, então não pode ser prefixo de None
    if lstb is None:
        return False
    # Senão, primeiros iguais e resto prefixo
    return lsta.primeiro == lstb.primeiro and prefixo(lsta.resto, lstb.resto)
