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

    def __init__(self) -> None:
        '''
        Cria um novo dicionário vazio.
        '''
        raise NotImplementedError

    def num_itens(self) -> int:
        '''
        Devolve a quantidade de chaves no dicionário.
        '''
        raise NotImplementedError

    def associa(self, chave: str, valor: int):
        '''
        Associa a *chave* com o *valor* no dicionário. Se *chave* já está
        associada com um valor, ele é substituído por *valor*.
        '''
        raise NotImplementedError

    def busca(self, chave: str) -> int | None:
        '''
        Devolve o valor associado à *chave* no dicionário ou None se a chave
        não estiver no dicionário.
        '''
        raise NotImplementedError

    def remove(self, chave: str):
        '''
        Remove a *chave* e o valor associado a ela do dicionário. Não faz
        nada se a *chave* não está no dicionário.
        '''
        raise NotImplementedError
