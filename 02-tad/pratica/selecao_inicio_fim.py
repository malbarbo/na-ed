from dataclasses import dataclass


@dataclass
class Selecao:
    '''
    Um intervalo de células selecionadas de uma linha de uma panilha.
    '''

    def __init__(self, col: int):
        '''
        Cria uma nova seleção de células que inclui apenas a célula da coluna *col*
        de uma linha qualquer.

        Requer que col >= 1.

        Exemplos
        >>> s = Selecao(10)
        >>> s.inicio()
        10
        >>> s.fim()
        10
        '''
        return


    def inicio(self) -> int:
        '''
        Devolve o início da seleção *s*.

        Exemplos
        >>> s = Selecao(4)
        >>> s.inicio()
        4
        >>> s.move_esquerda()
        >>> s.inicio()
        3
        '''
        return 0


    def fim(self) -> int:
        '''
        Devolve o fim da seleção *s*.

        Exemplos
        >>> s = Selecao(4)
        >>> s.fim()
        4
        >>> s.move_direita()
        >>> s.fim()
        5
        '''
        return 0


    def move_direita(self):
        '''
        Altera a selação *s* movendo o início ou fim da seleção para a direita da
        seguinte forma:
        - Se o fim de *s* está a direita da célula onde a seleção começou, ou a
          seleção só tem uma célula, então o fim é movido uma célula para a
          direita.
        - Se o início de *s* está a esquerda célula onde a seleção começou, então,
          o início é movido uma célula para a direta (até o mínimo de 1).

        Exemplos
        >>> # Mudança do fim
        >>> s = Selecao(2)
        >>> s.move_direita()
        >>> s.inicio()
        2
        >>> s.fim()
        3
        >>> s.move_direita()
        >>> s.inicio()
        2
        >>> s.fim()
        4
        >>> # Mudança do início
        >>> s = Selecao(4)
        >>> s.move_esquerda()
        >>> s.move_esquerda()
        >>> s.move_esquerda()
        >>> s.inicio()
        1
        >>> s.fim()
        4
        >>> s.move_direita()
        >>> s.inicio()
        2
        >>> s.fim()
        4
        '''
        return


    def move_esquerda(self):
        '''
        Altera a selação *s* movendo o início ou fim da seleção para a esquerda da
        seguinte forma:
        - Se o inicio de *s* está a esquerda da célula onde a seleção começou, ou a
          seleção só tem uma célula, então o início é movido uma célula para a
          esquerda (até o mínimo de 1).
        - Se o fim de *s* está a direita célula onde a seleção começou, então, o
          fim é movido uma célula para a esquerda.

        Exemplos
        >>> # Mudança do início
        >>> s = Selecao(6)
        >>> s.move_esquerda()
        >>> s.inicio()
        5
        >>> s.fim()
        6
        >>> s.move_esquerda()
        >>> s.inicio()
        4
        >>> s.fim()
        6
        >>> # Mudança do fim
        >>> s = Selecao(4)
        >>> s.move_direita()
        >>> s.move_direita()
        >>> s.move_direita()
        >>> s.inicio()
        4
        >>> s.fim()
        7
        >>> s.move_esquerda()
        >>> s.inicio()
        4
        >>> s.fim()
        6
        '''
        return
