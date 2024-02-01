from __future__ import annotations
from dataclasses import dataclass


class No:
    '''
    Um nó no encademaneto.
    '''
    prox: No
    item: str
    ante: No

    def __init__(self, item: str):
        # Quando um nó é criado, os valores prox e ante devem ser inicializados
        # para não permanecerem em um estado inválido.
        self.prox = None  # type: ignore
        self.item = item
        self.ante = None  # type: ignore


class FilaDupla:
    '''
    Uma coleção de strings que segue a política de fila dupla, ou seja, os
    elementos podem ser inseridos e removidos de qualquer extremo (aqui
    chamados de início e fim).

    Exemplos
    >>> f = FilaDupla()
    >>> f.vazia()
    True
    >>> f.insere_inicio('casa')
    >>> f.insere_inicio('minha')
    >>> f.insere_fim('é')
    >>> f.insere_fim('verde')
    >>> f.insere_fim('legal')
    >>> f.insere_fim('né?')
    >>> f.vazia()
    False
    >>> f.remove_inicio()
    'minha'
    >>> f.remove_inicio()
    'casa'
    >>> f.remove_inicio()
    'é'
    >>> f.remove_inicio()
    'verde'
    >>> f.remove_fim()
    'né?'
    >>> f.remove_fim()
    'legal'
    >>> f.remove_inicio()
    Traceback (most recent call last):
    ...
    ValueError: fila vazia
    >>> f.remove_fim()
    Traceback (most recent call last):
    ...
    ValueError: fila vazia
    '''

    sentinela: No

    def __init__(self):
        self.sentinela = No('')
        self.sentinela.prox = self.sentinela
        self.sentinela.ante = self.sentinela

    def insere_inicio(self, item: str):
        '''
        Insere *item* no início da fila.
        '''
        self.__insere(self.sentinela, No(item))

    def remove_inicio(self) -> str:
        '''
        Remove e devolve o item no início da fila.

        Requer que a fila não esteja vazia.
        '''
        if self.vazia():
            raise ValueError('fila vazia')

        return self.__remove(self.sentinela.prox)

    def insere_fim(self, item: str):
        '''
        Insere *item* no fim da fila.
        '''
        self.__insere(self.sentinela.ante, No(item))

    def remove_fim(self) -> str:
        '''
        Remove e devolve o item no fim da fila.

        Requer que a fila não esteja vazia.
        '''
        if self.vazia():
            raise ValueError('fila vazia')

        return self.__remove(self.sentinela.ante)

    def vazia(self) -> bool:
        '''
        Devolve True e a fila está vazia, False caso contrário.
        '''
        return self.sentinela.prox == self.sentinela

    def __insere(self, p: No, novo: No):
        novo.prox = p.prox
        novo.ante = p
        p.prox.ante = novo
        p.prox = novo

    def __remove(self, p: No) -> str:
        item = p.item
        p.ante.prox = p.prox
        p.prox.ante = p.ante
        return p.item
