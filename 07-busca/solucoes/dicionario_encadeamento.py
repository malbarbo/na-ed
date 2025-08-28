from __future__ import annotations
from dataclasses import dataclass


@dataclass
class No:
    chave: str
    valor: int
    prox: No | None


class Dicionario:
    '''
    Uma coleção de associações chave-valor, onde cada chave é única.

    Exemplos

    >>> d = Dicionario()
    >>> d.num_itens()
    0
    >>> d.associa('Jorge', 25)
    >>> d.associa('Bia', 40)
    >>> d.num_itens()
    2
    >>> d.busca('Jorge')
    25
    >>> d.busca('Bia')
    40
    >>> d.busca('Andre') is None
    True
    >>> d.associa('Bia', 50)
    >>> d.busca('Bia')
    50
    >>> d.remove('Jorge')
    >>> d.busca('Jorge') is None
    True
    >>> d.remove('Ana')
    >>> d.num_itens()
    1

    Testes

    O teste a seguir cria uma lista com uma permutação dos números de 0 a 99 e
    cria um dicionário adicionando cada número (string) como chave associada
    com o próprio número.

    Em seguida, para cada número da lista uma busca é realizada para verificar
    se a associação está correta. Depois a associação é removida e todas as
    outras associações são verificadas.

    >>> import random
    >>> lst = list(range(100))
    >>> random.shuffle(lst)
    >>> d = Dicionario()
    >>> # Faz associação
    >>> for valor in lst:
    ...     d.associa(str(valor), valor)
    >>> for i in range(len(lst)):
    ...     # Associação original
    ...     assert d.busca(str(i)) == i
    ...     # Modifica a associação e verifica
    ...     d.associa(str(i), 2 * i)
    ...     assert d.busca(str(i)) == 2 * i
    ...     # Remove a associação e verifica
    ...     d.remove(str(i))
    ...     assert d.busca(str(i)) is None
    ...     # As associações que não foram removidas permanecem as mesmas?
    ...     for j in range(i + 1, len(lst)):
    ...         assert d.busca(str(j)) == j
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
        associada com um valor, ele é substituído por *valor*.
        '''
        p = self.__busca(chave)
        if p is not None:
            p.valor = valor
        else:
            self.sentinela.prox = No(chave, valor, self.sentinela.prox)

    def busca(self, chave: str) -> int | None:
        '''
        Devolve o valor associado à *chave* no dicionário ou None se a chave
        não estiver no dicionário.
        '''
        p = self.__busca(chave)
        if p is not None:
            return p.valor
        else:
            return None

    def remove(self, chave: str):
        '''
        Remove a *chave* e o valor associado a ela do dicionário. Não faz
        nada se a *chave* não está no dicionário.
        '''
        # Procura o nó anterior ao nó que contém a chave
        p = self.sentinela
        while p.prox is not None and p.prox.chave != chave:
            p = p.prox
        # Se encontrou, remove o próximo
        if p.prox is not None:
            p.prox = p.prox.prox

    def __busca(self, chave: str) -> No | None:
        '''
        Se a *chave* está no dicionário, devolve o nó p tal que p.chave == chave;
        senão, devolve None.
        '''
        p = self.sentinela.prox
        while p is not None and p.chave != chave:
            p = p.prox
        return p
