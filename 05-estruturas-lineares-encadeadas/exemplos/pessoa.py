from dataclasses import dataclass


@dataclass
class Pessoa:
    nome: str
    idade: int | None


def faz_aniversario(p: Pessoa):
    '''
    Aumenta a idade da pessoa *p* em 1 ano
    se a idade for diferente de None.

    Exemplos
    >>> p1 = Pessoa('Joao', 21)
    >>> faz_aniversario(p1)
    >>> p1
    Pessoa(nome='Joao', idade=22)
    >>> p2 = Pessoa('Maria', None)
    >>> faz_aniversario(p2)
    >>> p2
    Pessoa(nome='Maria', idade=None)
    '''
    if p.idade is not None:
        p.idade += 1
