def inicializa_heap(A: list[int]):
    r'''
    Organiza os elementos de *A* para formarem um heap máximo.

    Exemplo

              4                      16
            /    \      -->        /    \
          1       3              14     10
        /   \   /   \          /   \   /   \
       2    16 9    10        8     7 9     3
      / \   /                / \   /
    14   8 7                2   4 1

    >>> A = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    >>> inicializa_heap(A)
    >>> A
    [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
    >>>
    '''
    for i in range(len(A) // 2, -1, -1):
        concerta_heap(A, len(A), i)


def concerta_heap(A: list[int], n: int, i: int):
    r'''
    Concer um heap... TODO: determine a descrição!

    Requer que i <= n < len(A).
    Requer que as árvores com raizes esq(i) e dir(i) sejam heaps máximos (se
    existirem).

    Exemplo

             16                     16
           /    \      -->        /    \
         4       10            14       10
       /   \   /   \          /   \   /   \
     14     7 9     3        8     7 9     3
     / \   /                / \   /
    2   8 1                2   4 1

    >>> A = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
    >>> concerta_heap(A, 10, 1)
    >>> A
    [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
    '''
    assert i < n <= len(A)
    fesq = esq(i)
    fdir = dir(i)
    imax = i
    if fesq < n and A[fesq] > A[imax]:
        imax = fesq
    if fdir < n and A[fdir] > A[imax]:
        imax = fdir
    if imax != i:
        A[i], A[imax] = A[imax], A[i]
        concerta_heap(A, n, imax)


def esq(i: int):
    '''
    Devolve o índice do filho a esquerda do nó na posição *i*.
    Exemplos
    >>> esq(0)
    1
    >>> esq(1)
    3
    '''
    return 2 * i + 1


def dir(i: int):
    '''
    Devolve o índice do filho a direita do nó na posição *i*.
    Exemplos
    >>> dir(0)
    2
    >>> dir(1)
    4
    '''
    return 2 * i + 2
