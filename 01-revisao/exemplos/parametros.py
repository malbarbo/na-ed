# Carrege o arquivo com o comando python -i parametros.py
# e teste os exemplos.
#
# Tente prever a saída antes de executar!

from dataclasses import dataclass


def soma1(x: int):
    '''
    >>> a = 10
    >>> soma1(a)
    >>> a # doctest: +SKIP
    ?
    '''
    x = x + 1


def soma1_primeiro1(lst: list[int]):
    '''
    >>> x = [6, 1, 10]
    >>> soma1_primeiro1(x)
    >>> x # doctest: +SKIP
    ?
    '''
    lst[0] = lst[0] + 1


def soma1_primeiro2(lst: list[int]):
    '''
    >>> x = [6, 1, 10]
    >>> soma1_primeiro2(x)
    >>> x # doctest: +SKIP
    ?
    '''
    x = lst[0]
    x = x + 1


def zera1(lst: list[int]):
    '''
    >>> x = [6, 1, 10]
    >>> zera1(x)
    >>> x # doctest: +SKIP
    ?
    '''
    lst1 = []
    for i in range(len(lst)):
        lst1.append(0)
    lst = lst1


def zera2(lst: list[int]):
    '''
    >>> x = [6, 1, 10]
    >>> zera2(x)
    >>> x # doctest: +SKIP
    ?
    '''
    for i in range(len(lst)):
        lst[i] = 0


@dataclass
class Ponto:
    x: int
    y: int


def ponto_desloca_y(p: Ponto, dy: int):
    '''
    >>> q = Ponto(7, 2)
    >>> ponto_desloca_y(q, 4)
    >>> q # doctest: +SKIP
    ?
    '''
    p = Ponto(p.x, p.y + dy)


def ponto_desloca_y2(p: Ponto, dy: int):
    '''
    >>> q = Ponto(7, 2)
    >>> ponto_desloca_y2(q, 4)
    >>> q # doctest: +SKIP
    ?
    '''
    p.y = p.y + dy
