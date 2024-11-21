from __future__ import annotations
from dataclasses import dataclass


def grupos_corretos(expr: str) -> bool:
    '''
    Produz True se os parênteses,
    colchetes e chaves de *expr*
    estão corretos, False caso contrário.

    Exemplos:
    >>> grupos_corretos('([{}])')
    True
    >>> grupos_corretos('[](){}')
    True
    >>> grupos_corretos('({)}')
    False
    >>> grupos_corretos('(2*[3*{5+2]})')
    False
    >>> grupos_corretos('([a]*{b-c}-[10])*({(4-2)/8})')
    True
    '''
    p = Pilha()
    corretos = True
    i = 0
    while i < len(expr) and corretos:
        if expr[i] in '([{':
            p.empilha(expr[i])
        elif expr[i] in ')]}':
            item = p.desempilha()
            if item is None or not par(item, expr[i]):
                corretos = False
        i = i + 1
    return p.vazia() and corretos


def par(a: str, b: str) -> bool:
    return a == '(' and b == ')' or \
        a == '[' and b == ']' or \
        a == '{' and b == '}'


@dataclass
class No:
    '''Um nó em um encadeamento'''
    item: str
    prox: No | None


class Pilha:
    '''
    Uma coleção de strings que segue a política LIFO: o elemento mais
    recentemente inserido é o primeiro a ser removido.

    >>> p = Pilha()
    >>> p.vazia()
    True
    >>> p.empilha('O')
    >>> p.empilha('que')
    >>> p.empilha('escrever?')
    >>> p.vazia()
    False
    >>> p.desempilha()
    'escrever?'
    >>> p.empilha('fazer')
    >>> p.empilha('agora?')
    >>> while not p.vazia():
    ...     p.desempilha()
    'agora?'
    'fazer'
    'que'
    'O'
    '''

    topo: No | None

    def __init__(self) -> None:
        '''
        Cria uma pilha vazia
        '''
        self.topo = None

    def empilha(self, item: str):
        '''
        Adiciona o *item* na pilha.
        '''
        self.topo = No(item, self.topo)

    def desempilha(self) -> str | None:
        '''
        Devolve o elemento mais recentemente adicionado da pilha.
        Se a pilha está vazia, devolve None.
        '''
        if self.topo is None:
            return None
        item = self.topo.item
        self.topo = self.topo.prox
        return item

    def vazia(self) -> bool:
        '''
        Devolve True se a pilha está vazia, False caso contrário.
        '''
        return self.topo is None
