from dataclasses import dataclass


@dataclass
class Robo:
    '''
    Um robo com um nome que está em uma posição da linha do jogo, que deve
    ser um valor entre 1 e 10.
    '''
    ...


def robo_cria(nome: str) -> Robo:
    '''
    Cria um novo robo com o *nome* e que está na posição 1.

    Exemplos
    >>> r = robo_cria('r2d2')
    >>> robo_info(r)
    'r2d2 (1)'
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


def robo_info(r: Robo) -> str:
    '''
    Devolve um texto com o nome do robo *r*
    seguido da sua posição entre parêntes.

    Exemplos
    >>> r = robo_cria('rob')
    >>> robo_move(r, 2)
    >>> robo_posicao(r)
    'rob (3)'
    '''


def robo_move(r: Robo, n: int):
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
