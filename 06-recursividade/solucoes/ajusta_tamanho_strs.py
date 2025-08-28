from __future__ import annotations
from dataclasses import dataclass


@dataclass
class No:
    primeiro: str
    resto: Lista


Lista = No | None


def ajusta_tamanho_str(s: str, n: int) -> str:
    '''
    Devolve uma string baseada em *s* com *n* caracteres.
    Se *n < len(s)*, devolve uma string com os primeiros *n* caracteres de *s*
    Se *n > len(s)*, devolve a string *s* seguida de espaços em branco.
    Se *n == len(s)*, devolve *s*.

    Requer que n >= 0.

    Exemplos
    >>> ajusta_tamanho_str('casas', 3)
    'cas'
    >>> ajusta_tamanho_str('casas', 9)
    'casas    '
    >>> ajusta_tamanho_str('casas', 9)
    'casas    '
    '''
    # Essa função não precisa ser recursiva, mas vale o treino! Mesmo sendo ineficiente...
    assert n >= 0
    if n == len(s):
        return s
    elif n < len(s):
        return ajusta_tamanho_str(s[:-1], n)
    else:  # n > len(s)
        return ajusta_tamanho_str(s + ' ', n)


def ajusta_tamanho_strs(lst: Lista, n: int):
    '''
    Modifica cada elemento de *lst* com a função *ajusta_tamanho_str*.

    Exemplos
    >>> lst = No('casa', No('outra palavra', No('a', None)))
    >>> ajusta_tamanho_strs(lst, 4)
    >>> lst
    No(primeiro='casa', resto=No(primeiro='outr', resto=No(primeiro='a   ', resto=None)))
    '''
    if lst is not None:
        lst.primeiro = ajusta_tamanho_str(lst.primeiro, n)
        ajusta_tamanho_strs(lst.resto, n)
