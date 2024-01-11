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
    # Indíce do último elemento da fila
    fim: int
    # Indíce do primeiro elemento da fila
    # A fila está vazia se fim < inicio.
    inicio: int

    def __init__(self):
        self.valores = array(MAX_TAM, '')
        self.inicio = 0
        self.fim = -1

    def enfileira(self, item: str):
        if self.fim >= MAX_TAM - 1:
            raise ValueError('fila cheia')
        self.fim += 1
        self.valores[self.fim] = item

    def desenfileira(self) -> str:
        if self.vazia():
            raise ValueError('fila vazia')
        item = self.valores[self.inicio]
        self.inicio += 1
        return item

    def vazia(self) -> bool:
        return self.fim < self.inicio
