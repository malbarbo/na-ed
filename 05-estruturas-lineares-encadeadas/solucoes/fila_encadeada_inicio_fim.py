from __future__ import annotations
from dataclasses import dataclass


@dataclass
class No:
    '''Um nó em um encadeamento'''
    item: str
    prox: No | None


class Fila:
    '''
    Uma coleção de strings que segue a política FIFO: o primeiro a ser inserido
    é o primeiro a ser removido.

    Exemplos
    >>> f = Fila()
    >>> f.vazia()
    True
    >>> f.enfileira('Amanda')
    >>> f.enfileira('Fernando')
    >>> f.enfileira('Márcia')
    >>> f.vazia()
    False
    >>> f.desenfileira()
    'Amanda'
    >>> f.enfileira('Pedro')
    >>> f.enfileira('Alberto')
    >>> while not f.vazia():
    ...     f.desenfileira()
    'Fernando'
    'Márcia'
    'Pedro'
    'Alberto'
    '''

    # Invariantes:
    #   - Se inicio é None, então fim é None
    #   - Se inicio é um No, então fim é o nó no fim do encadeamento que começa
    #     em inicio
    inicio: No | None
    fim: No | None

    def __init__(self) -> None:
        '''Cria uma nova fila vazia'''
        self.inicio = None
        self.fim = None

    def enfileira(self, item: str):
        '''
        Adiciona *item* no final da fila.
        '''
        if self.fim is None:
            assert self.inicio is None
            self.inicio = No(item, None)
            self.fim = self.inicio
        else:
            self.fim.prox = No(item, None)
            self.fim = self.fim.prox

    def desenfileira(self) -> str | None:
        '''
        Remove e devolve o primeiro elemento da fila.
        Devolve None se a fila está vazia.
        '''
        if self.inicio is None:
            return None
        item = self.inicio.item
        self.inicio = self.inicio.prox
        if self.inicio is None:
            self.fim = None
        return item

    def vazia(self) -> bool:
        '''
        Devolve True se a fila está vazia, False caso contrário.
        '''
        return self.inicio is None

    def junta(self, outra):
        '''
        Move todos os elementos de *outra* para esta fila.

        Exemplos
        >>> a = Fila()
        >>> a.enfileira('casa')
        >>> a.enfileira('arroz')
        >>> a.enfileira('pais')
        >>> b = Fila()
        >>> a.enfileira('outra')
        >>> a.enfileira('talvez')
        >>> a.junta(b)
        >>> b.vazia()
        True
        >>> while not a.vazia():
        ...     a.desenfileira()
        'casa'
        'arroz'
        'pais'
        'outra'
        'talvez'
        '''
        self.fim.prox = outra.inicio
        self.fim = outra.fim
        outra.inicio = None
        outra.fim = None
