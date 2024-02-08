from __future__ import annotations
from dataclasses import dataclass


@dataclass
class No:
    chave: str
    valor: int
    prox: No | None


class Dicionario:
    '''
    Uma coleção de chaves únicas associadas com valores.

    Exemplos
    >>> d = Dicionario()
    >>> d.num_itens()
    0
    >>> d.associa('Jorge', 25)
    >>> d.associa('Bia', 40)
    >>> d.num_itens()
    2
    >>> d.get('Jorge')
    25
    >>> d.get('Bia')
    40
    >>> d.get('Andre') is None
    True
    >>> d.associa('Bia', 50)
    >>> d.get('Bia')
    50
    >>> d.remove('Jorge')
    >>> d.get('Jorge') is None
    True
    >>> d.remove('Ana')
    >>> d.num_itens()
    1
    '''

    sentinela: No

    def __init__(self) -> None:
        '''
        Cria um novo dicionário vazio.
        '''
        self.sentinela = No('', 0, None)

    def num_itens(self) -> int:
        '''
        Devolve a quantidade de chaves no dicionário.
        '''
        num = 0
        p = self.sentinela.prox
        while p is not None:
            p = p.prox
            num += 1
        return num

    def associa(self, chave: str, valor: int):
        '''
        Associa a *chave* com o *valor* no dicionário. Se *chave* já está
        associada com um valor, ele é sustituído por *valor*.
        '''
        p = self.__get_no(chave)
        if p is not None:
            p.valor = valor
        else:
            self.sentinela.prox = No(chave, valor, self.sentinela.prox)

    def get(self, chave: str) -> int | None:
        '''
        Devolve o valor associado com *chave* no dicionário ou None se a chave
        não está no dicionário.
        '''
        p = self.__get_no(chave)
        if p is not None:
            return p.valor
        else:
            return None

    def remove(self, chave: str):
        '''
        Remove a *chave* e o valor associado com ela do dicionário. Não faz
        nada se a *chave* não está no dicionário.
        '''
        p = self.sentinela
        while p.prox is not None and p.prox.chave != chave:
            p = p.prox
        if p.prox is not None:
            p.prox = p.prox.prox

    def __get_no(self, chave: str) -> No | None:
        p = self.sentinela.prox
        while p is not None and p.chave != chave:
            p = p.prox
        return p
