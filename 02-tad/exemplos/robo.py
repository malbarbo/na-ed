from dataclasses import dataclass


@dataclass
class Robo:
    '''
    Um robo que está em uma posição da linha do
    jogo, que deve ser um valor entre 1 e 10.
    '''
    ...


def robo_cria() -> Robo:
    '''
    Cria um novo robo na posição 1.

    Exemplos
    >>> r = robo_cria()
    >>> robo_posicao(r)
    1
    '''
    ...


def robo_posicao(r: Robo) -> int:
    '''
    Devolve a posição atual do robo *r*.

    Exemplos
    >>> r = robo_cria()
    >>> robo_move(r, 2)
    >>> robo_posicao(r)
    3
    '''
    ...


def robo_move(r: Robo, ):
    '''
    Altera a posição de *r* avançando *n* posições (até no máximo a posição 10)
    se *n* for positivo, ou recuando -*n* posições (até no mínimo a posição 1)
    se *n* for negativo. O robo *r* permanece na mesma posição se *n* for 0.

    Exemplos
    >>> r = robo_cria()
    >>> # Avança
    >>> robo_move(r, 5)
    >>> robo_posicao(r)
    6
    >>> robo_move(r, 6)
    >>> robo_posicao(r)
    10
    >>> # Recua
    >>> robo_move(r, -3)
    >>> robo_posicao(r)
    7
    >>> robo_move(r, -8)
    >>> robo_posicao(r)
    1
    >>> # Não move
    >>> robo_move(r, 0)
    >>> robo_posicao(r)
    1
    '''
    ...
