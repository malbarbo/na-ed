# Versão que "diminui a lista" criando uma nova lista com slice.
def concatena(lst: list[str]) -> str:
    '''
    Concatena todos os elementos de *lst*.

    Exemplos
    >>> concatena([])
    ''
    >>> concatena(['cc'])
    'cc'
    >>> concatena(['cc', ' é ', 'ciência da computação'])
    'cc é ciência da computação'
    '''
    if lst == []:
        s = ''
    else:
        s = lst[0] + concatena(lst[1:])
    return s


# Versão que "diminui a lista" usando um argumento extra
def concatena2(lst: list[str], n: int) -> str:
    '''
    Concatena os primeiros *n* elementos de *lst*.

    Requer que 0 <= n < len(lst)

    Exemplos
    >>> concatena2([], 0)
    ''
    >>> concatena2(['cc'], 1)
    'cc'
    >>> concatena2(['cc', ' é ', 'ciência da computação'], 3)
    'cc é ciência da computação'
    '''
    if n == 0:
        s = ''
    else:
        s = concatena2(lst, n - 1) + lst[n - 1]
    return s
