from typing import TypeVar, Iterator, Generic

T = TypeVar('T')

class array(Generic[T]):
    '''
    Um arranjo de tamanho fixo implementado com uma lista.

    Exemplos
    >>> a = array(5, 0)
    >>> a
    array([0, 0, 0, 0, 0])
    >>> len(a)
    5
    >>> a[0] = 10
    >>> a[3] = 20
    >>> a
    array([10, 0, 0, 20, 0])
    >>> a[0]
    10
    >>> a[5]
    Traceback (most recent call last):
    ...
    IndexError: list index out of range

    Exemplo com string
    >>> a = array(3, 'oi')
    >>> a
    array(['oi', 'oi', 'oi'])
    >>> a[1] = ' de novo '
    >>> s = ''
    >>> for v in a:
    ...    s = s + v
    >>> s
    'oi de novo oi'
    '''

    def __init__(self, n: int, val: T):
        '''
        Cria um novo arranjo com *n* cópias de *val*.

        Note que todas as cópias de *val* referenciam o mesmo objeto, o pode
        não ser o comportamento desejado.

        Para criar cópias distintas de *val*, use copy.deepcopy após a criação
        do arranjo.

        Exemplo
        >>> from dataclasses import dataclass
        >>> @dataclass
        ... class Ponto:
        ...     x: int
        ...     y: int
        >>> p = Ponto(3, 4)
        >>> pontos = array(2, p)
        >>> pontos
        array([Ponto(x=3, y=4), Ponto(x=3, y=4)])
        >>> # pontos[0] e pontos[1] referenciam o mesmo objeto
        >>> pontos[0].x = 10
        >>> pontos
        array([Ponto(x=10, y=4), Ponto(x=10, y=4)])

        >>> # Para criar cópias distintas de p
        >>> # podemos usar copy.deepcopy após criar
        >>> from copy import deepcopy
        >>> p = Ponto(3, 4)
        >>> pontos = array(2, Ponto(0, 0))
        >>> for i in range(len(pontos)):
        ...     pontos[i] = deepcopy(p)
        >>> pontos
        array([Ponto(x=3, y=4), Ponto(x=3, y=4)])
        >>> pontos[0].x = 10
        >>> pontos
        array([Ponto(x=10, y=4), Ponto(x=3, y=4)])
        '''
        self.valores = [val] * n

    def __len__(self) -> int:
        return len(self.valores)

    def __getitem__(self, i: int) -> T:
        return self.valores[i]

    def __setitem__(self, i: int, value: T):
        self.valores[i] = value

    def __iter__(self) -> Iterator[T]:
        return iter(self.valores)

    def __repr__(self) -> str:
        return 'array(' + repr(self.valores) + ')'

    def __str__(self) -> str:
        return 'array(' + str(self.valores) + ')'
