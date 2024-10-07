from ed import array

# Modificações:
# - construtor recebe a capacidade
# - adicionado método capacidade
# - adicionado método cheia
# - ajustado os exemplos e a implementação para funcionar com essas modificações

# Exercícios (estão aṕos a implementação da Pilha)
# - inverte_pilha
# - remove_vazios


class Pilha:
    '''
    Uma coleção de strings que segue a política LIFO: o elemento mais
    recentemente inserido é o primeiro a ser removido.

    >>> p = Pilha(10)
    >>> p.vazia()
    True
    >>> p.empilha('O')
    >>> p.empilha('que')
    >>> p.empilha('escrever?')
    >>> p.vazia()
    False
    >>> p.desempilha()
    'escrever?'
    >>> p.empilha('fazer')
    >>> p.empilha('agora?')
    >>> while not p.vazia():
    ...     p.desempilha()
    'agora?'
    'fazer'
    'que'
    'O'
    '''

    valores: array[str]
    # O índice do elemento que está no topo da pilha,
    # -1 se a pilha está vazia.
    topo: int

    def __init__(self, cap: int):
        '''
        Cria uma nova pilha com capacidade para armazenar *cap*
        elementos.
        Requer que cap > 0.
        '''
        if cap <= 0:
            raise ValueError('cap precisa ser maior que 0')
        self.valores = array(cap, '')
        self.topo = -1

    def empilha(self, item: str):
        '''
        Adiciona o *item* na pilha.

        Requer que a quantidade de elementos na pilha seja menor que
        *self.capacidade()*.

        Exemplos
        >>> p = Pilha(10)
        >>> for i in range(10):
        ...     p.empilha(str(i))
        >>> p.empilha('a')
        Traceback (most recent call last):
        ...
        ValueError: pilha cheia
        >>> p.desempilha() == str(9)
        True
        '''
        if self.cheia():
            raise ValueError('pilha cheia')
        self.topo = self.topo + 1
        self.valores[self.topo] = item

    def desempilha(self) -> str:
        '''
        Devolve o elemento mais recentemente adicionado da pilha.

        Requer que a pilha não esteja vazia.

        Exemplos
        >>> p = Pilha(10)
        >>> p.desempilha()
        Traceback (most recent call last):
        ...
        ValueError: pilha vazia
        >>> p.empilha('casa')
        >>> p.empilha('na')
        >>> p.empilha('árvore')
        >>> p.desempilha()
        'árvore'
        '''
        if self.vazia():
            raise ValueError('pilha vazia')
        item = self.valores[self.topo]
        self.topo = self.topo - 1
        return item

    def capacidade(self) -> int:
        '''
        Devolve a capacidade da pilha.

        Exemplos
        >>> p = Pilha(8)
        >>> p.capacidade()
        8
        >>> p = Pilha(17)
        >>> p.capacidade()
        17
        '''
        return len(self.valores)

    def vazia(self) -> bool:
        '''
        Devolve True se a pilha está vazia, False caso contrário.

        Exemplos
        >>> p = Pilha(10)
        >>> p.vazia()
        True
        >>> p.empilha('lar')
        >>> p.vazia()
        False
        '''
        return self.topo == -1

    def cheia(self) -> bool:
        '''
        Devolve True se a pilha está checia, False caso contrário.
        >>> p = Pilha(2)
        >>> p.cheia()
        False
        >>> p.empilha('a')
        >>> p.cheia()
        False
        >>> p.empilha('b')
        >>> p.cheia()
        True
        '''
        return self.topo == self.capacidade() - 1



def inverte_pilha(p: Pilha):
    '''
    Inverte a ordem dos elemento de *p*.

    Exemplos
    >>> p = Pilha(10)
    >>> p.empilha('um')
    >>> p.empilha('carro')
    >>> p.empilha('mouse')
    >>> inverte_pilha(p)
    >>> p.desempilha()
    'um'
    >>> p.desempilha()
    'carro'
    >>> p.desempilha()
    'mouse'
    '''
    a = Pilha(p.capacidade())
    b = Pilha(p.capacidade())
    move_todos(p, a)
    move_todos(a, b)
    move_todos(b, p)


def remove_vazios(p: Pilha):
    '''
    Temove todos os elementos vazios de *p*.

    Exemplos
    >>> p = Pilha(10)
    >>> p.empilha('um')
    >>> p.empilha('')
    >>> p.empilha('carro')
    >>> p.empilha('')
    >>> p.empilha('')
    >>> remove_vazios(p)
    >>> p.desempilha()
    'carro'
    >>> p.desempilha()
    'um'
    '''
    a = Pilha(p.capacidade())
    while not p.vazia():
        item = p.desempilha()
        if item != '':
            a.empilha(item)
    move_todos(a, p)


def move_todos(a: Pilha, b: Pilha):
    '''
    Desempilha todos os elementos de *a* e empilha em *b*.

    Exemplos
    >>> a = Pilha(10)
    >>> a.empilha('a')
    >>> a.empilha('b')
    >>> a.empilha('c')
    >>> b = Pilha(10)
    >>> move_todos(a, b)
    >>> a.vazia()
    True
    >>> b.desempilha()
    'a'
    >>> b.desempilha()
    'b'
    >>> b.desempilha()
    'c'
    >>> b.vazia()
    True
    '''
    while not a.vazia():
        b.empilha(a.desempilha())
