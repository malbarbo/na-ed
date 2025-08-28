from __future__ import annotations
from dataclasses import dataclass


@dataclass
class No:
    primeiro: int
    resto: Lista


Lista = No | None


def prefixo(lsta: Lista, lstb: Lista) -> bool:
    '''
    Devolve True se *lsta* é prefixo de *lstb* (ou seja, se *lstb* começa
    com *lsta*), e False caso contrário.

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
    # A lista vazia é prefixo de qualquer lista
    if lsta is None:
        return True
    # Se lsta não é None, então não pode ser prefixo de uma lista vazia
    if lstb is None:
        return False
    # Senão, os primeiros elementos devem ser iguais e o resto de lsta deve ser prefixo do resto de lstb
    return lsta.primeiro == lstb.primeiro and prefixo(lsta.resto, lstb.resto)
