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
        if i < len(self.itens) and self.itens[i].chave == chave:
            self.itens[i].valor = valor
        else:
            self.itens.insert(i, Item(chave, valor))

    def get(self, chave: str) -> int | None:
        '''
        Devolve o valor associado com *chave* no dicionário ou None se a chave
        não está no dicionário.
        '''
        i = self.__busca(chave)
        if i < len(self.itens) and self.itens[i].chave == chave:
            return self.itens[i].valor
        else:
            return None

    def remove(self, chave: str):
        '''
        Remove a *chave* e o valor associado com ela do dicionário. Não faz
        nada se a *chave* não está no dicionário.
        '''
        i = self.__busca(chave)
        if i < len(self.itens) and self.itens[i].chave == chave:
            del self.itens[i]

    def __busca(self, chave: str) -> int:
        '''
        Se *chave* está presente em *itens*, devolve o índice i tal que
        *itens[i] == chave*. Senão devolve o índice i tal que a inserção de
        *chave* na posição *i* de *itens* mantém *itens* em ordem não
        decrescente.

        Requer que *itens* esteja em ordem não decrescente.
        '''
        ini = 0
        fim = len(self.itens) - 1
        while ini <= fim:
            m = (ini + fim) // 2
            if chave == self.itens[m].chave:
                return m
            elif chave < self.itens[m].chave:
                fim = m - 1
            else:  # chave > self.itens[m].chave
                ini = m + 1
        return ini
