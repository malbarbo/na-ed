class Contador:
    '''
    Representa a quantidade de pendências que precisam ser resolvidas. Essa
    quantidade pode aumentar ou diminuir em uma unidade por vez e nunca pode
    ficar menor que zero.
    '''

    # Já que não podemos usa um inteiro e operações aritméticas, usamos o
    # tamanho de uma lista para representar o valor do contador.
    lst: list[int]

    def __init__(self) -> None:
        '''
        Cria um contador iniciado em 0.

        Exemplos
        >>> c = Contador()
        >>> c.valor()
        0
        '''
        self.lst = []

    def valor(self) -> int:
        '''
        Devolve o valor atual do contador.

        Exemplos
        >>> c = Contador()
        >>> for i in range(10):
        ...    c.inc()
        >>> for i in range(3):
        ...    c.dec()
        >>> c.valor()
        7
        '''
        return len(self.lst)

    def inc(self) -> None:
        '''
        Aumenta o valor do contador em 1.

        Exemplos
        >>> c = Contador()
        >>> c.inc()
        >>> c.valor()
        1
        >>> c.inc()
        >>> c.valor()
        2
        '''
        self.lst.append(0)

    def dec(self) -> None:
        '''
        Diminuir o valor do contador em 1. Se o contador está em 0, não faz
        nada.

        Exemplos
        >>> c = Contador()
        >>> c.inc()
        >>> c.inc()
        >>> c.inc()
        >>> c.valor()
        3
        >>> c.dec()
        >>> c.valor()
        2
        >>> c.dec()
        >>> c.dec()
        >>> c.dec()
        >>> c.dec()
        >>> c.valor()
        0
        '''
        if len(self.lst) > 0:
            self.lst.pop()
