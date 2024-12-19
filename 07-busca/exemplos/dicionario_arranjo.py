from dataclasses import dataclass


@dataclass
class Item:
    chave: str
    valor: int


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

    Em seguida, para cada número da lista uma busca é executada para verificar
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

    itens: list[Item]

    def __init__(self) -> None:
        '''
        Cria um novo dicionário vazio.
        '''
        self.itens = []

    def num_itens(self) -> int:
        '''
        Devolve a quantidade de chaves no dicionário.
        '''
        return len(self.itens)

    def associa(self, chave: str, valor: int):
        '''
        Associa a *chave* com o *valor* no dicionário. Se *chave* já está
        associada com um valor, ele é sustituído por *valor*.
        '''
        i = self.__busca(chave)
        if i is not None:
            self.itens[i].valor = valor
        else:
            self.itens.append(Item(chave, valor))

    def busca(self, chave: str) -> int | None:
        '''
        Devolve o valor associado com *chave* no dicionário ou None se a chave
        não está no dicionário.
        '''
        i = self.__busca(chave)
        if i is not None:
            return self.itens[i].valor
        else:
            return None

    def remove(self, chave: str):
        '''
        Remove a *chave* e o valor associado com ela do dicionário. Não faz
        nada se a *chave* não está no dicionário.
        '''
        i = self.__busca(chave)
        if i is not None:
            self.itens[i], self.itens[-1] = self.itens[-1], self.itens[i]
            self.itens.pop()

    def __busca(self, chave: str) -> int | None:
        for i in range(len(self.itens)):
            if self.itens[i].chave == chave:
                return i
        return None
