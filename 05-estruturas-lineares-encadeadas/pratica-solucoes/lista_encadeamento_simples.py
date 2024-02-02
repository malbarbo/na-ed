from __future__ import annotations
from dataclasses import dataclass


@dataclass
class No:
    '''Um nó em um encadeamento'''
    item: int
    prox: No | None


class Lista:
    '''
    Uma sequência de números.

    Exemplos
    >>> lst = Lista()
    >>> lst.str()
    '[]'
    >>> lst.insere(0, 7)
    >>> lst.insere(1, 20)
    >>> lst.insere(2, 5)
    >>> lst.get(0)
    7
    >>> lst.get(2)
    5
    >>> lst.num_itens()
    3
    >>> lst.str()
    '[7, 20, 5]'
    >>> lst.set(0, 10)
    >>> lst.str()
    '[10, 20, 5]'
    >>> lst.insere(1, 8)
    >>> lst.str()
    '[10, 8, 20, 5]'
    >>> lst.remove(2)
    >>> lst.str()
    '[10, 8, 5]'
    >>> lst.insere(lst.num_itens(), 8)
    >>> lst.str()
    '[10, 8, 5, 8]'
    >>> lst.indice(8)
    1
    >>> lst.remove_item(5)
    >>> lst.str()
    '[10, 8, 8]'
    '''

    # Um nó sentinela, que está sempre presente mas não faz parte da lista
    sentinela: No

    def __init__(self) -> None:
        '''
        Cria uma lista vazia.
        '''
        self.sentinela = No(0, None)

    def num_itens(self) -> int:
        '''
        Devolve a quantidade de itens da lista.
        '''
        num = 0
        p = self.sentinela.prox
        while p is not None:
            p = p.prox
            num += 1
        return num

    def get(self, i: int) -> int:
        '''
        Devolve o item que está na posição *i* da lista.

        Requer que 0 <= i < self.num_itens().
        '''
        return self.__get_no(i).item

    def set(self, i: int, item: int):
        '''
        Armazena *item* na posição **i** da lista.

        Requer que 0 <= i < self.num_itens().
        '''
        self.__get_no(i).item = item

    def insere(self, i: int, item: int):
        '''
        Insere *item* na posição *i* da lista. Os itens que estavam inicialmente
        nas posiçõe i, i+1, ..., passam a ficar nas posições i+1, i+2, ...

        Requer que 0 <= i <= self.num_itens().
        '''
        p = self.__get_no_ante(i)
        p.prox = No(item, p.prox)

    def remove(self, i: int):
        '''
        Remove e devolve o item na posição *i* da lista. Os itens que estavam
        inicialmente nas posições i, i+1, ..., passam a ficar nas posições
        i-1, i, ...

        Requer que 0 <= i < self.num_itens().
        '''
        p = self.__get_no_ante(i)
        if p.prox is None:
            raise ValueError('índice inválido')
        p.prox = p.prox.prox

    def remove_item(self, item: int):
        '''
        Remove a primeira ocorrência de *item* da lista. Se i é a posição do
        *item*, então os itens que estavam inicialmente nas posições i, i+1,
        ..., passam a ficar nas posições i-1, i, ...

        Requer que *item* esteja na lista.
        '''
        p = self.sentinela
        while p.prox is not None and p.prox.item != item:
            p = p.prox
        if p.prox is None:
            raise ValueError('item não encontrado')
        p.prox = p.prox.prox

    def indice(self, item: int) -> int:
        '''
        Devolve a posição da primeira ocorrência de *item* na lista.

        Requer que *item* esteja na lista.
        '''
        i = 0
        p = self.sentinela
        while p.prox is not None and p.prox.item != item:
            p = p.prox
            i += 1
        if p.prox is None:
            raise ValueError('item não encontrado')
        return i

    def str(self) -> str:
        '''
        Gera uma representação em string da lista.
        '''
        s = '['
        p = self.sentinela.prox
        if p is not None:
            s += str(p.item)
            p = p.prox
            while p is not None:
                s += ', ' + str(p.item)
                p = p.prox
        return s + ']'

    def __get_no_ante(self, i: int) -> No:
        '''
        Devolve o nó anterior ao nó de índice *i*.
        Requer que 0 <= i <= self.num_itens().
        Se i == 0, devolve a sentinela.
        '''
        if i < 0:
            raise ValueError('índice inválido')
        elif i == 0:
            return self.sentinela
        else:
            return self.__get_no(i - 1)

    def __get_no(self, i: int) -> No:
        '''
        Devolve o nó de índice *i*.
        Requer que 0 <= i < self.num_itens().
        '''
        j = 0
        p = self.sentinela.prox
        while p is not None and j < i:
            p = p.prox
            j += 1
        if p is not None and j == i:
            return p
        else:
            raise ValueError('índice inválido')
