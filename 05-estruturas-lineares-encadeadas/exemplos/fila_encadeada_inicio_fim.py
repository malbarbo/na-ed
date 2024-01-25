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

    inicio: No | None
    fim: No | None

    def __init__(self):
        '''Cria uma nova fila vazia'''
        self.inicio = None
        self.fim = None

    def enfileira(self, item: str):
        '''
        Adiciona *item* no final da fila.
        '''
        if self.inicio is None:
            self.inicio = No(item, None)
            self.fim = self.inicio
        else:
            self.fim.prox = No(item, None)
            self.fim = self.fim.prox

    def desenfileira(self) -> str:
        '''
        Remove e devolve o primeiro elemento da fila.

        Requer que a fila não esteja vazia.
        '''
        if self.inicio is not None:
            item = self.inicio.item
            self.inicio = self.inicio.prox
            if self.inicio is None:
                self.fim = None
            return item
        else:
            raise ValueError('fila vazia')

    def vazia(self) -> bool:
        '''
        Devolve True se a fila está vazia, False caso contrário.
        '''
        return self.inicio is None
