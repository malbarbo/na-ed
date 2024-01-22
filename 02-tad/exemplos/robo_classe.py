class Robo:
    '''
    Um robo com um nome que está em uma posição da linha do jogo, que deve
    ser um valor entre 1 e 10.
    '''
    nome: str
    pos: int

    def __init__(self, nome: str):
        '''
        Cria um novo robo com o *nome* e que está na posição 1.

        Exemplos
        >>> r = Robo('r2d2')
        >>> r.info()
        'r2d2 (1)'
        '''
        self.nome = nome
        self.pos = 1

    def posicao(self) -> int:
        '''
        Devolve a posição atual do robo *r*.

        Exemplos
        >>> r = Robo('rob')
        >>> r.move(2)
        >>> r.posicao()
        3
        '''
        return self.pos

    def info(self) -> str:
        '''
        Devolve um texto com o nome do robo *r*
        seguido da sua posição entre parêntes.

        Exemplos
        >>> r = Robo('rob')
        >>> r.move(2)
        >>> r.info()
        'rob (3)'
        '''
        return self.nome + ' (' + str(self.pos) + ')'

    def move(self, n: int):
        '''
        Altera a posição de *r* avançando *n* posições (até no máximo a posição 10)
        se *n* for positivo, ou recuando -*n* posições (até no mínimo a posição 1)
        se *n* for negativo. O robo *r* permanece na mesma posição se *n* for 0.

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
        self.pos = max(1, min(10, self.pos + n))
