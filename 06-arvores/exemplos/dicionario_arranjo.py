from dataclasses import dataclass

@dataclass
class Item:
    chave: str
    valor: int

class Dicionario:
    '''
    Uma coleção de chaves únicas associadas com valores.

    Exemplos
    >>> d = Dicionario()
    >>> d.num_itens()
    0
    >>> d.associa('Jorge', 25)
    >>> d.associa('Bia', 40)
    >>> d.num_itens()
    2
    >>> d.get('Jorge')
    25
    >>> d.get('Bia')
    40
    >>> d.get('Andre') is None
    True
    >>> d.associa('Bia', 50)
    >>> d.get('Bia')
    50
    >>> d.remove('Jorge')
    >>> d.get('Jorge') is None
    True
    >>> d.remove('Ana')
    >>> d.num_itens()
    1
    '''

    itens: list[Item]

    def __init__(self) -> None:
        '''
        Cria um novo dicionário vazio.
        '''
        self.itens = []

    def num_itens(self) -> int:
        '''
        Devolve a quantidade de chaves no dicionário.
        '''
        return len(self.itens)

    def associa(self, chave: str, valor: int):
        '''
        Associa a *chave* com o *valor* no dicionário. Se *chave* já está
        associada com um valor, ele é sustituído por *valor*.
        '''
        i = self.__busca(chave)
        if i is not None:
            self.itens[i].valor = valor
        else:
            self.itens.append(Item(chave, valor))

    def get(self, chave: str) -> int | None:
        '''
        Devolve o valor associado com *chave* no dicionário ou None se a chave
        não está no dicionário.
        '''
        i = self.__busca(chave)
        if i is not None:
            return self.itens[i].valor
        else:
            return None

    def remove(self, chave: str):
        '''
        Remove a *chave* e o valor associado com ela do dicionário. Não faz
        nada se a *chave* não está no dicionário.
        '''
        i = self.__busca(chave)
        if i is not None:
            self.itens[i], self.itens[-1] = self.itens[-1], self.itens[i]
            self.itens.pop()

    def __busca(self, chave: str) -> int | None:
        for i in range(len(self.itens)):
            if self.itens[i].chave == chave:
                return i
        return None
