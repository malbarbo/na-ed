from __future__ import annotations
from dataclasses import dataclass


@dataclass
class No:
    esq: Arvore
    val: int
    dir: Arvore

    def __repr__(self) -> str:
        '''
        Devolve uma representação dos nós usando um percurso pré-ordem. Nós
        vazios não aparecen na saída. A representação de um nó que não é vazio
        é composto por abre parênteses, a representação do nó a esquerda, o
        valor do nó entre espaços, seguido da representação do nó a direita,
        seguido de fecha parênteses.

        Exemplos
        >>> No(No(None, 6, None), 5, None)
        (( 6 ) 5 )
        >>> No(None, 2, No(None, 6, None))
        ( 2 ( 6 ))
        '''
        if self.esq is None:
            esq = ''
        else:
            esq = repr(self.esq)
        if self.dir is None:
            dir = ''
        else:
            dir = repr(self.dir)
        return f'({esq} {self.val} {dir})'


Arvore = No | None


def busca(t: Arvore, val: int) -> bool:
    r'''
    Devolve True se *val* está em *t*, False caso contrário.

    Requer que *t* seja uma ABB.

    Exemplos
               t
             4
           /   \
         /       \
        1  esq    7 dir
      /   \       /
    -3     2     5
            \
             3

    >>> esq = No(No(None, -3, None), 1, No(None, 2, No(None, 3, None)))
    >>> dir = No(No(None, 5, None), 7, None)
    >>> t = No(esq, 4, dir)
    >>> busca(None, 10)
    False
    >>> busca(t, 0)
    False
    >>> busca(t, 1)
    True
    >>> busca(t, 2)
    True
    >>> busca(t, 3)
    True
    >>> busca(t, 4)
    True
    >>> busca(t, 5)
    True
    >>> busca(t, 6)
    False
    >>> busca(t, 7)
    True
    '''
    if t is None:
        return False
    elif val == t.val:
        return True
    elif val < t.val:
        return busca(t.esq, val)
    else:  # val > t.val
        return busca(t.dir, val)


def busca_iter(t: Arvore, val: int) -> bool:
    r'''
    Devolve True se *val* está em *t*, False caso contrário.

    Requer que *t* seja uma ABB.

    Exemplos
               t
             4
           /   \
         /       \
        1  esq    7 dir
      /   \       /
    -3     2     5
            \
             3

    >>> esq = No(No(None, -3, None), 1, No(None, 2, No(None, 3, None)))
    >>> dir = No(No(None, 5, None), 7, None)
    >>> t = No(esq, 4, dir)
    >>> busca_iter(None, 10)
    False
    >>> busca_iter(t, 0)
    False
    >>> busca_iter(t, 1)
    True
    >>> busca_iter(t, 2)
    True
    >>> busca_iter(t, 3)
    True
    >>> busca_iter(t, 4)
    True
    >>> busca_iter(t, 5)
    True
    >>> busca_iter(t, 6)
    False
    >>> busca_iter(t, 7)
    True
    '''
    r = t
    while r is not None:
        if val == r.val:
            return True
        elif val < r.val:
            r = r.esq
        else:  # val > r.val
            r = r.dir
    return False


def insere(t: Arvore, val: int) -> No:
    '''
    Devolve a raiz da ABB que é o resultado da inserção de *val* em *t*.
    Se *val* já está em *t*, devolve *t*.

    Requer que *t* seja uma ABB.

    Exemplos
    >>> r = insere(None, 7)
    >>> r
    ( 7 )
    >>> r = insere(r, 7)
    >>> r
    ( 7 )
    >>> r = insere(r, 3)
    >>> r
    (( 3 ) 7 )
    >>> r = insere(r, 12)
    >>> r
    (( 3 ) 7 ( 12 ))
    >>> r = insere(r, 4)
    >>> r
    (( 3 ( 4 )) 7 ( 12 ))
    >>> r = insere(r, 10)
    >>> r
    (( 3 ( 4 )) 7 (( 10 ) 12 ))
    '''
    if t is None:
        return No(None, val, None)
    elif val < t.val:
        t.esq = insere(t.esq, val)
    elif val > t.val:
        t.dir = insere(t.dir, val)
    else:  # val == t.val
        pass
    return t


def remove(t: Arvore, val: int) -> Arvore:
    r'''
    Devolve a raiz da ABB que é o resultado da remoção de *val* em *t*.
    Se *val* não está em *t*, devolve *t*.
    Se *t* só tem um nó e *val* está nesse nó, devolve None.

    Requer que *t* seja uma ABB.

    Exemplos

         5
       /   \
     /       \
    1         10
     \       /
      3     6
     / \     \
    2   4     8

    >>> r = None
    >>> for val in [5, 1, 3, 10, 6, 4, 8, 2]:
    ...     r = insere(r, val)
    >>> # Remoção de folha
    >>> r = remove(r, 4)
    >>> r
    (( 1 (( 2 ) 3 )) 5 (( 6 ( 8 )) 10 ))
    >>> # Remoção de nó interno sem filho a esquerda
    >>> r = remove(r, 1)
    >>> r
    ((( 2 ) 3 ) 5 (( 6 ( 8 )) 10 ))
    >>> # Remoção de nó interno sem filho a direita
    >>> r = remove(r, 10)
    >>> r
    ((( 2 ) 3 ) 5 ( 6 ( 8 )))
    >>> # Remoção de nó interno com dois filhos
    >>> r = remove(r, 5)
    >>> r
    (( 2 ) 3 ( 6 ( 8 )))
    '''
    if t is None:
        return None
    elif val < t.val:
        t.esq = remove(t.esq, val)
        return t
    elif val > t.val:
        t.dir = remove(t.dir, val)
        return t
    else:  # val == t.val
        if t.esq is None:
            # Se t.dir é None
            #     t     ->  None
            #
            # Se t.dir não é None
            #     t          D
            #    / \    ->  / \
            #   E   D      DE DD
            #      / \
            #     DE DD
            return t.dir
        elif t.dir is None:
            #     t          E
            #    /      ->  / \
            #   E          EE ED
            #  / \
            # EE ED
            return t.esq
        else:
            # Tem os dois filhos
            #     t           t (val=max)
            #    / \    ->   / \
            #   E   D       E   D
            #  com         sem
            #  max         max
            m = maximo(t.esq)
            t.val = m
            t.esq = remove(t.esq, m)
            return t


def maximo(t: No) -> int:
    '''
    Encontra o valor máximo em *t*.

    Requer que *t* seja uma ABB.

    Exemplos
    >>> r = None
    >>> for val in [5, 1, 2, 7, 6, 3, 8, 4]:
    ...     r = insere(r, val)
    >>> maximo(r)
    8
    '''
    while t.dir is not None:
        t = t.dir
    return t.val
