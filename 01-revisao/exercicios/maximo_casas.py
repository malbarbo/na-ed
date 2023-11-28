from dataclasses import dataclass
from enum import Enum, auto

# Análise
#
# Um personagem de um jogo está em um tabuleiro com 10 linhas e 10 colunas
# (enumeradas de 1 a 10) e está virado para das direções: norte, sul, leste ou oeste.
#
# Para o norte aumenta o número da linha (sul diminui)
#
# Para o leste aumenta o número da coluna (oeste diminui).
#
# Determinar quantas casas no máximo um personagem pode avançar a partir da sua posição e direção.
#
# O personagem não pode sair do tabuleiro.


class Direcao(Enum):
    '''
    A direção em que o personagem está virado.

    Para o norte o número da linha aumenta, para o sul diminui.

    Para o leste o número da coluna aumenta, para o sul diminui.

    ^
    |     N
    |     |
    | O -   - L
    |     |
    |     S
    --------------->
    '''
    NORTE = auto()
    LESTE = auto()
    SUL = auto()
    OESTE = auto()


@dataclass
class Personagem:
    '''
    A posição e direção que um personagem se encontra no tabuleiro.
    '''
    # A linha, deve estar entre 1 e 10
    lin: int
    # A coluna, deve estar entre 1 e 10
    col: int
    dir: Direcao


def maximo_casas(p: Personagem) -> int:
    '''
    Determina o número máximo de casas que o personagem *p* pode avançar
    considerando a sua posição atual e a direção que ele está virado.

    Exemplos
    >>> maximo_casas(Personagem(lin=4, col=2, dir=Direcao.NORTE))
    6
    >>> maximo_casas(Personagem(lin=10, col=2, dir=Direcao.NORTE))
    0
    >>> maximo_casas(Personagem(lin=4, col=2, dir=Direcao.SUL))
    3
    >>> maximo_casas(Personagem(lin=1, col=2, dir=Direcao.SUL))
    0
    >>> maximo_casas(Personagem(lin=4, col=2, dir=Direcao.LESTE))
    8
    >>> maximo_casas(Personagem(lin=4, col=10, dir=Direcao.LESTE))
    0
    >>> maximo_casas(Personagem(lin=4, col=2, dir=Direcao.OESTE))
    1
    >>> maximo_casas(Personagem(lin=4, col=1, dir=Direcao.OESTE))
    0
    '''
    if p.dir == Direcao.NORTE:
        casas = 10 - p.lin
    elif p.dir == Direcao.SUL:
        casas = p.lin - 1
    elif p.dir == Direcao.LESTE:
        casas = 10 - p.col
    elif p.dir == Direcao.OESTE:
        casas = p.col - 1
    return casas
