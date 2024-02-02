from __future__ import annotations
from dataclasses import dataclass


@dataclass
class No:
    item: int
    prox: No | None


def lista_nos(lst: list[int]) -> No | None:
    '''
    Devolve um encadeamento com os elementos de *lst*.

    Exemplos
    >>> lista_nos([])
    >>> lista_nos([6, 2, 4])
    No(item=6, prox=No(item=2, prox=No(item=4, prox=None)))
    '''
    p = None
    for i in range(len(lst) - 1, -1, -1):
        p = No(lst[i], p)
    return p


def num_itens(p: No | None) -> int:
    '''
    Determina quanto itens existem no encadeamento
    que começa com *p*.

    Exemplos
    >>> num_itens(None)
    0
    >>> num_itens(No(10, None))
    1
    >>> num_itens(No(20, No(10, None)))
    2
    >>> num_itens(No(4, No(20, No(10, None))))
    3
    '''
    num = 0
    while p is not None:
        num += 1
        p = p.prox
    return num


def soma1(p: No | None):
    '''
    Modifica cada nó do encadeamento que começa em *p* somando
    1 ao item do nó.

    Exemplos
    >>> p = No(10, No(20, No(30, None)))
    >>> soma1(p)
    >>> p
    No(item=11, prox=No(item=21, prox=No(item=31, prox=None)))
    '''
    while p is not None:
        p.item += 1
        p = p.prox


def maximo(p: No) -> int:
    '''
    Encontra o valor máximo entre todos os itens dos
    nós no encadeamento que começa com *p*.

    Exemplos
    >>> maximo(No(7, None))
    7
    >>> maximo(No(10, No(20, No(8, None))))
    20
    '''
    m = p.item
    q = p.prox
    while q is not None:
        m = max(m, q.item)
        q = q.prox
    return m


def copia(p: No | None) -> No | None:
    '''
    Cria e devolve uma cópia do encadeamento que inicia em *p*.

    Exemplos
    >>> p = No(10, No(20, No(30, None)))
    >>> q = copia(p)
    >>> # quanto mudamos p,
    >>> # q não é alterado pois é uma cópia
    >>> p.item = 1
    >>> p.prox.item = 2
    >>> p.prox.prox.item = 3
    >>> p
    No(item=1, prox=No(item=2, prox=No(item=3, prox=None)))
    >>> q
    No(item=10, prox=No(item=20, prox=No(item=30, prox=None)))

    Exemplo para o None
    >>> copia(None)
    '''
    # Cria um primeiro temporário para facilitar o encadeamento
    inicio = No(0, None)
    ultimo = inicio
    while p is not None:
        ultimo.prox = No(p.item, None)
        ultimo = ultimo.prox
        p = p.prox
    # Descarta o primeiro nó
    return inicio.prox



def duplica_nos(p: No | None):
    '''
    Modifica o encadeamento que começa em *p* criando uma
    cópia de cada nó e colocando a cópia após o nó original
    no encadeamento.

    Exemplos
    >>> p = No(1, No(2, None))
    >>> duplica_nos(p)
    >>> p
    No(item=1, prox=No(item=1, prox=No(item=2, prox=No(item=2, prox=None))))
    >>> # A modificação do primeiro
    >>> # não pode alterar o segundo!
    >>> p.item = 20
    >>> p.prox.item
    1
    '''
    while p is not None:
        p.prox = No(p.item, p.prox)
        p = p.prox.prox
