# Avaliação das implementações
#
# - insere_pos3 é a solução mais simples pois é direta. No entanto, requer que
#   o programador enxergue a utilidade do uso das operações de sublista.
#
# - insere_pos2 é a solução mais complicada. O intervalo do laço parece
#   artificial, além disso, em apenas uma iteração o novo elemento é inserido,
#   sugerindo que esta operação deva ser feito em separado, que é como é feito em
#   insere_pos
#
# - insere_post é conceitualmente simples, mas requer que o programador faço o
#   planejamento da solução em três etapas, o que pode não ser claro a primeira
#   vista.

def insere_pos(lst: list[int], i: int, n: int) -> list[int]:
    '''
    Cria uma nova lista inserindo *n* na posicão *i* de *lst*.

    Requer que 0 <= i <= len(lst).
    >>> insere_pos([], 0, 10)
    [10]
    >>> insere_pos([5], 0, 10)
    [10, 5]
    >>> insere_pos([5], 1, 10)
    [5, 10]
    >>> insere_pos([5, 7], 0, 10)
    [10, 5, 7]
    >>> insere_pos([5, 7], 1, 10)
    [5, 10, 7]
    >>> insere_pos([5, 7], 2, 10)
    [5, 7, 10]
    '''
    assert 0 <= i <= len(lst)

    r = []
    # Copia os elementos de 0 até i
    for j in range(0, i):
        r.append(lst[j])

    # Insere o elemento n na posição i
    r.append(n)

    # Copia os lementos de i até len(lst)
    for j in range(i, len(lst)):
        r.append(lst[j])

    return r


def insere_pos2(lst: list[int], i: int, n: int) -> list[int]:
    '''
    Cria uma nova lista inserindo *n* na posicão *i* de *lst*.

    Requer que 0 <= i <= len(lst).
    >>> insere_pos2([], 0, 10)
    [10]
    >>> insere_pos2([5], 0, 10)
    [10, 5]
    >>> insere_pos2([5], 1, 10)
    [5, 10]
    >>> insere_pos2([5, 7], 0, 10)
    [10, 5, 7]
    >>> insere_pos2([5, 7], 1, 10)
    [5, 10, 7]
    >>> insere_pos2([5, 7], 2, 10)
    [5, 7, 10]
    '''
    assert 0 <= i <= len(lst)
    r = []
    for j in range(len(lst) + 1):
        if j == i:
            r.append(n)
        if j < len(lst):
            r.append(lst[j])
    return r


def insere_pos3(lst: list[int], i: int, n: int) -> list[int]:
    '''
    Cria uma nova lista inserindo *n* na posicão *i* de *lst*.

    Requer que 0 <= i <= len(lst).
    >>> insere_pos3([], 0, 10)
    [10]
    >>> insere_pos3([5], 0, 10)
    [10, 5]
    >>> insere_pos3([5], 1, 10)
    [5, 10]
    >>> insere_pos3([5, 7], 0, 10)
    [10, 5, 7]
    >>> insere_pos3([5, 7], 1, 10)
    [5, 10, 7]
    >>> insere_pos3([5, 7], 2, 10)
    [5, 7, 10]
    '''
    assert 0 <= i <= len(lst)
    return lst[:i] + [n] + lst[i:]
