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

    Testes

    O teste a seguir cria uma lista com uma permutação dos números de 0 a 99 e
    cria um dicionário adicionando cada número (string) como chave associada
    com o próprio número.

    Em seguida, para cada número da lista o get é executado para verificar se a
    associação está correta. Depois a associação é removida e todas as outras
    associações são verificadas.

    >>> import random
    >>> lst = list(range(100))
    >>> random.shuffle(lst)
    >>> d = Dicionario()
    >>> # Faz associação
    >>> for valor in lst:
    ...     d.associa(str(valor), valor)
    >>> for i in range(len(lst)):
    ...     # Associação original
    ...     assert d.get(str(i)) == i
    ...     # Modifica a associação e verifica
    ...     d.associa(str(i), 2 * i)
    ...     assert d.get(str(i)) == 2 * i
    ...     # Remove a associação e verifica
    ...     d.remove(str(i))
    ...     assert d.get(str(i)) is None
    ...     # As associações que não foram removidas permanecem as mesmas?
    ...     for j in range(i + 1, len(lst)):
    ...         assert d.get(str(j)) == j
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
        p = self.__busca(chave)
        if p is not None:
            p.valor = valor
        else:
            self.sentinela.prox = No(chave, valor, self.sentinela.prox)

    def get(self, chave: str) -> int | None:
        '''
        Devolve o valor associado com *chave* no dicionário ou None se a chave
        não está no dicionário.
        '''
        p = self.__busca(chave)
        if p is not None:
            return p.valor
        else:
            return None

    def remove(self, chave: str):
        '''
        Remove a *chave* e o valor associado com ela do dicionário. Não faz
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
        Se *chave* está no dicionário devolve o nó p tal que p.chave == chave,
        senão devolve None.
        '''
        p = self.sentinela.prox
        while p is not None and p.chave != chave:
            p = p.prox
        return p
