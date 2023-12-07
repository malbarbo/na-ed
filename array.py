class array:
    '''
    Um arranjo de tamanho fixo implementado com uma lista.
    '''

    def __init__(self, n: int):
        '''
        Cria um novo arranjo com *n* elementos 0.
        '''
        self.valores = [0] * n

    def __len__(self) -> int:
        return len(self.valores)

    def __getitem__(self, i: int) -> int:
        return self.valores[i]

    def __setitem__(self, i: int, value: int):
        self.valores[i] = value

    def __repr__(self) -> str:
        return 'array(' + repr(self.valores) + ')'

    def __str__(self) -> str:
        return 'array(' + str(self.valores) + ')'
