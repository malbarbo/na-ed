from ed import array

# Modificações
# - construtor recebe a capacidade
# - adicionado método capacidade
# - adicionado método cheia
# - adicionado método __avanca
# - ajustado os exemplos ea implementação para funcionar com essas modificações


class Fila:
    '''
    Uma coleção de strings que segue a política FIFO: o primeiro a ser inserido
    é o primeiro a ser removido.

    Exemplos
    >>> f = Fila(10)
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

    valores: array[str]
    # Indíce onde o próximo elemento será inserido
    fim: int
    # Indíce do primeiro elemento da fila
    inicio: int

    # O valor para o inicio e o fim são incrementados até chegarem em
    # na capacidade da fila, quando voltam a ser 0.
    #
    # A fila está vazia se inicio == fim e está cheia se o próximo valor para
    # fim é igual ao inicio. Dessa forma, nunca podemos preencher todos os
    # elementos de *valores*, pois senão não seria possível distinguir entre fila
    # cheia e fila vazia. Para horar o valor de *cap* do construtor, inicializamos
    # *valores* com *cap* + 1 itens.

    def __init__(self, cap: int):
        '''
        Cria uma nova fila com capacidade para armazenar *cap*
        elementos.
        Requer que cap > 0.
        '''
        if cap <= 0:
            raise ValueError('cap precisa ser maior que 0')
        self.valores = array(cap + 1, '')
        self.inicio = 0
        self.fim = 0

    def enfileira(self, item: str):
        '''
        Adiciona *item* no final da fila.

        Requer que a quantidade de elementos na fila seja menor que
        *self.capacidade()*.

        Exemplos
        >>> f = Fila(10)
        >>> for i in range(10):
        ...     f.enfileira(str(i))
        >>> f.enfileira('a')
        Traceback (most recent call last):
        ...
        ValueError: fila cheia
        >>> f.desenfileira()
        '0'
        >>> f.desenfileira()
        '1'
        '''
        if self.cheia():
            raise ValueError('fila cheia')
        self.valores[self.fim] = item
        self.fim = self.__avanca(self.fim)

    def desenfileira(self) -> str:
        '''
        Remove e devolve o primeiro elemento da fila.

        Requer que a fila não esteja vazia.

        Exemplos
        >>> f = Fila(10)
        >>> f.desenfileira()
        Traceback (most recent call last):
        ...
        ValueError: fila vazia
        >>> f.enfileira('Márcia')
        >>> f.enfileira('João')
        >>> f.enfileira('Pedro')
        >>> f.desenfileira()
        'Márcia'
        '''
        if self.vazia():
            raise ValueError('fila vazia')
        item = self.valores[self.inicio]
        self.inicio = self.__avanca(self.inicio)
        return item

    def vazia(self) -> bool:
        '''
        Devolve True se a fila está vazia, False caso contrário.

        Exemplos
        >>> f = Fila(10)
        >>> f.vazia()
        True
        >>> f.enfileira('Jorge')
        >>> f.vazia()
        False
        '''
        return self.inicio == self.fim

    def cheia(self) -> bool:
        '''
        Devolve True se a fila está vazia, isto é, a quantidade de elementos na
        fila é igual a *self.capacidade()*, False caso contrário.
        '''
        return self.__avanca(self.fim) == self.inicio

    def capacidade(self) -> int:
        '''
        Devolve a capacidade da fila.

        Exemplos
        >>> f = Fila(6)
        >>> f.capacidade()
        6
        >>> f = Fila(31)
        >>> f.capacidade()
        31
        '''
        return len(self.valores) - 1

    def __avanca(self, i: int) -> int:
        # Calcula o índice seguinte de *i* considerando
        # o esquema circular da fila.
        if i == self.capacidade():
            return 0
        else:
            return i + 1
