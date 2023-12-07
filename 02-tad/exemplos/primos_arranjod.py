from arranjod_um import *

def primos(lim: int) -> ArranjoD:
    '''
    Encontra todos os números primos menores que *lim*.

    Exemplos:
    >>> a = primos(12)
    >>> arranjod_get(a, 0)
    2
    >>> arranjod_get(a, 1)
    3
    >>> arranjod_get(a, 2)
    5
    >>> arranjod_get(a, 3)
    7
    >>> arranjod_get(a, 4)
    11
    '''
    primos = arranjod_vazio()
    n = 2
    while n < lim:
        eh_primo = True
        i = 0
        while eh_primo and i < arranjod_len(primos):
            if n % arranjod_get(primos, i) == 0:
                eh_primo = False
            i = i + 1

        if eh_primo:
            arranjod_acrescenta(primos, n)

        n = n + 1
    return primos
