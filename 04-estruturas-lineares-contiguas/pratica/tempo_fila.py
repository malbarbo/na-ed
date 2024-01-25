from fila_arranjo_inicio_fim import Fila
# from fila_arranjo_fim import Fila

def tempo_fila(n: int):
    # Criar uma fila com capacidade para n elementos
    # Inserir n elementos na fila
    # Esvaziar a fila
    return

if __name__ == '__main__':
    from timeit import timeit
    for n in [1000, 2000, 4000]:
        tempo = timeit(f'tempo_fila({n})',
                       setup='from __main__ import tempo_fila',
                       number=10)
        print(n, tempo)
