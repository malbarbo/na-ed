from ed import array

MAX_TAM = 100

class Fila:
    '''
    Uma coleção de strings que segue a política FIFO: o primeiro a ser inserido
    é o primeiro a ser removido.

    Exemplos
    >>> f = Fila()
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
    # Indíce do último elemento da fila, -1 se a fila está vazia
    fim: int

    def __init__(self):
        self.valores = array(MAX_TAM, '')
        self.fim = -1

    def enfileira(self, item: str):
        if self.fim >= MAX_TAM - 1:
            raise ValueError('fila cheia')
        self.fim += 1
        self.valores[self.fim] = item

    def desenfileira(self) -> str:
        if self.vazia():
            raise ValueError('fila vazia')
        item = self.valores[0]
        for i in range(1, self.fim + 1):
            self.valores[i - 1] = self.valores[i]
        self.fim -= 1
        return item

    def vazia(self) -> bool:
        return self.fim == -1
