from __future__ import annotations
from dataclasses import dataclass


@dataclass
class No:
    valor: int
    prox: Lista


Lista = No | None


def ordena(lst: Lista) -> Lista:
    '''
    Ordena os elementos de *lst* em ordem não decrescente.

    Exemplo

    >>> arranjo(ordena(lista([5, 2, 4, 6, 1, 3])))
    [1, 2, 3, 4, 5, 6]

    Testes de propriedade
    A seguir, listas com tamanhos n = 0, 1, ..., 10,
    são geradas com os elementos 0, 1, ..., n. Para
    cada lista todas as suas permutações são usadas
    para testar o algoritmo de ordenação.
    >>> from itertools import permutations
    >>> for n in range(0, 11):
    ...     for p in permutations(range(n)):
    ...         lst = lista(list(p))
    ...         lst = ordena(lst)
    ...         assert lst == lista(list(range(n)))
    '''
    # TODO: implementar o algoritmo de ordenação!
    a = arranjo(lst)
    a.sort()
    return lista(a)


def lista(a: list[int]) -> Lista:
    '''
    Cria uma Lista com os elementos de *lst*.

    Exemplo
    >>> arranjo(lista([5, 1, 4]))
    [5, 1, 4]
    '''
    # cria um sentinela
    inicio = No(0, None)
    p = inicio
    for x in a:
        p.prox = No(x, None)
        p = p.prox
    # descarta o sentinela
    return inicio.prox


def arranjo(lst: Lista) -> list[int]:
    '''
    Cria um arranjo com os elementos de *lst*.
    '''
    a = []
    while lst is not None:
        a.append(lst.valor)
        lst = lst.prox
    return a
