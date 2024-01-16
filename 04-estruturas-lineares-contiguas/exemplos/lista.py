class Lista:
    '''
    Uma sequência de números.

    Exemplos
    >>> lst = Lista()
    >>> lst.str()
    '[]'
    >>> lst.insere(0, 7)
    >>> lst.insere(1, 20)
    >>> lst.insere(2, 5)
    >>> lst.get(0)
    7
    >>> lst.get(2)
    5
    >>> lst.num_itens()
    3
    >>> lst.str()
    '[7, 20, 5]'
    >>> lst.set(0, 10)
    >>> lst.str()
    '[10, 20, 5]'
    >>> lst.insere(1, 8)
    >>> lst.str()
    '[10, 8, 20, 5]'
    >>> lst.remove(2)
    >>> lst.str()
    '[10, 8, 5]'
    >>> lst.insere(lst.num_itens(), 8)
    >>> lst.str()
    '[10, 8, 5, 8]'
    >>> lst.indice(8)
    1
    >>> lst.remove_item(5)
    >>> lst.str()
    '[10, 8, 8]'
    '''

    def num_itens(self) -> int:
        '''
        Devolve a quantidade de itens da lista.
        '''

    def get(self, i: int) -> str:
        '''
        Devolve o item que está na posição *i* da lista.

        Requer que 0 <= i < self.num_itens().
        '''

    def set(self, i: int, item: str):
        '''
        Armazena *item* na posição **i** da lista.

        Requer que 0 <= i < self.num_itens().
        '''

    def insere(self, i: int, item: str):
        '''
        Insere *item* na posição *i* da lista. Os itens que estavam iniciamente
        nas posiçõe i, i+1, ..., passam a ficar nas posições i+1, i+2, ...

        Requer que 0 <= i <= self.num_itens().
        '''

    def remove(self, i: int):
        '''
        Remove e devolve o item na posição *i* da lista. Os itens que estavam
        inicialmente nas posições i, i+1, ..., passam a ficar nas posições
        i-1, i, ...

        Requer que 0 <= i < self.num_itens().
        '''

    def remove_item(self, item: str) ->:
        '''
        Remove a primeira ocorrência de *item* da lista. Se i é a posição do
        *item*, então os itens que estavam inicialmente nas posições i, i+1,
        ..., passam a ficar nas posições i-1, i, ...

        Requer que o item esteja na lista.
        '''

    def indice(self, item: str) -> int:
        '''
        Devolve a posição da primeira ocorrência de *item* na lista.

        Requer que *item* esteja presente na lista.
        '''

    def str(self) -> str:
        '''
        Gera uma representação em string da lista.
        '''
