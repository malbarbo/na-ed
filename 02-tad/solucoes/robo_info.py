class Robo:
    '''
    Um robo com um nome que está em uma posição da linha do jogo, que deve
    ser um valor entre 1 e 10.
    '''

    # O nome do robo seguido da sua posição entre parênteses
    # O traço baixo é para evitar conflito com o método info
    _info: str

    def __init__(self, nome: str):
        '''
        Cria um novo robo com o *nome* e que está na posição 1.

        Exemplos
        >>> r = Robo('r2d2')
        >>> r.info()
        'r2d2 (1)'
        '''
        self._info = nome + ' (1)'

    def posicao(self) -> int:
        '''
        Devolve a posição atual do robo *self*.

        Exemplos
        >>> r = Robo('rob')
        >>> r.move(2)
        >>> r.posicao()
        3
        '''
        inicio = self._info.index('(')
        return int(self._info[inicio + 1:-1])

    def info(self) -> str:
        '''
        Devolve um texto com o nome do robo *self* seguido da sua posição entre
        parêntes.

        Exemplos
        >>> r = Robo('rob')
        >>> r.move(2)
        >>> r.info()
        'rob (3)'
        '''
        return self._info

    def move(self, n: int):
        '''
        Altera a posição de *self* avançando *n* posições (até no máximo a
        posição 10) se *n* for positivo, ou recuando -*n* posições (até no
        mínimo a posição 1) se *n* for negativo. O robo *self* permanece na
        mesma posição se *n* for 0.

        Exemplos
        >>> r = Robo('rob')
        >>> # Avança
        >>> r.move(5)
        >>> r.posicao()
        6
        >>> r.move(6)
        >>> r.posicao()
        10
        >>> # Recua
        >>> r.move(-3)
        >>> r.posicao()
        7
        >>> r.move(-8)
        >>> r.posicao()
        1
        >>> # Não move
        >>> r.move(0)
        >>> r.posicao()
        1
        '''
        pos = self.posicao() + n
        if pos < 1:
            pos = 1
        if pos > 10:
            pos = 10
        nome = self._info[:self._info.index(' (')]
        self._info = f'{nome} ({pos})'
