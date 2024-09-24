class BancoHoras:
    '''
    Representa a quantidade de horas extras que um funcionário fez
    e que ainda não foram "volgadas".
    '''

    # Total de minutos
    minutos: int

    def __init__(self) -> None:
        '''
        Cria um novo banco de horas com zero horas.

        Exemplos
        >>> b = BancoHoras()
        >>> b.consulta()
        '00:00'
        '''
        self.minutos = 0

    def deposita(self, horas: int, minutos: int):
        '''
        Deposita a quantidade *horas* e *minutos* no banco de horas.

        Requer que horas >= 0 e 0 <= minutos < 60.

        Exemplos
        >>> b = BancoHoras()
        >>> b.deposita(0, 30)
        >>> b.deposita(2, 0)
        >>> b.deposita(3, 40)
        >>> b.consulta()
        '06:10'
        '''
        assert horas >= 0
        assert 0 <= minutos < 60
        self.minutos += horas * 60 + minutos

    def saque(self, horas: int, minutos: int) -> bool:
        '''
        Tenta sacar a quantidade *horas* e *minutos* do banco de horas.
        Se o saque for feito, devolve True.
        Se o saque não for feito (o saldo é insuficente), devolve False.

        Requer que horas >= 0 e 0 <= minutos < 60.
        Exemplos
        >>> b = BancoHoras()
        >>> b.deposita(5, 30)
        >>> b.saque(1, 40)
        True
        >>> b.consulta()
        '03:50'
        >>> b.saque(3, 51)
        False
        '''
        assert horas >= 0
        assert 0 <= minutos < 60
        minutos = horas * 60 + minutos
        if self.minutos > minutos:
            self.minutos -= minutos
            return True
        else:
            return False

    def consulta(self) -> str:
        '''
        Devolve uma string no formato HH:MM representado
        a quantidade de horas e minutos no banco de horas.

        Exemplos
        >>> b = BancoHoras()
        >>> b.deposita(2, 45)
        >>> b.consulta()
        '02:45'
        >>> b = BancoHoras()
        >>> b.deposita(12, 5)
        >>> b.consulta()
        '12:05'
        '''
        def istr(n: int) -> str:
            if n < 10:
                return '0' + str(n)
            else:
                return str(n)
        hh = self.minutos // 60
        mm = self.minutos % 60
        return istr(hh) + ':' + istr(mm)
        # Diretamente usando strings formatadas
        # return f'{hh:02}:{mm:02}'
