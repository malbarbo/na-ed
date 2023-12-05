from arranjod_um import *

def primos(lim: int) -> ArranjoD:
    '''
    Encontra todos os números primos menores que *lim*.

    Exemplos:
    >>> lst = primos(12)
    >>> lst[0]
    2
    >>> lst[1]
    3
    >>> lst[2]
    5
    >>> lst[3]
    7
    >>> lst[4]
    11
    '''
    primos = arranjod_vazio()
    n = 2
    while n < lim:
        eh_primo = True
        i = 0
        while eh_primo and i < arranjod_len(primos):
            if n % arranjod_pos(primos, i) == 0:
                eh_primo = False
            i = i + 1

        if eh_primo:
            arranjod_acrescenta(primos, n)

        n = n + 1
    return primos
