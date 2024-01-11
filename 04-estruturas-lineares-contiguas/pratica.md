---
title: Estruturas de dados lineares - Alocação contígua - Prática
urlcolor: Blue
---

<!-- Pilha -->

@) Modifique a implementação de `Pilha` vista em sala adicionando um método para verificar se a pilha está cheia.

@) Modifique a implementação de `Pilha` (do exercício anterior) para que o construtor receba como parâmetro a quantidade máxima de elementos que a pilha pode armazenar. Adicione um método que devolve a capacidade da pilha e ajuste os exemplos para funcionarem com essas modificações.

@) Projete uma função que receba como parâmetro uma pilha e modifique a pilha invertendo a ordem dos seus elementos. Faça a implementação usando uma pilha auxiliar. Qual a complexidade de tempo da função?

    ```python
    >>> p = Pilha()
    >>> p.empilha('um')
    >>> p.empilha('carro')
    >>> p.empilha('mouse')
    >>> inverte_pilha(p)
    >>> p.desempilha()
    'um'
    >>> p.desempilha()
    'carro'
    >>> p.desempilha()
    'mouse'
    ```

@) Projete uma função que receba como parâmetro uma pilha e remova todos os elementos da pilha que sejam vazios. Note que ordem relativa dos elementos que permanecem na pilha não de ser altera.

    ```python
    >>> p = Pilha()
    >>> p.empilha('um')
    >>> p.empilha('')
    >>> p.empilha('carro')
    >>> p.empilha('')
    >>> p.empilha('')
    >>> remove_vazios(p)
    >>> p.desempilha()
    'carro'
    >>> p.desempilha()
    'um'
    ```

@) Projete uma função que exiba os elementos de uma pilha na ordem em que eles foram adicionados. Use uma pilha auxiliar para fazer a implementação. Note que a pilha deve permanecer como ela foi passada para a função.

    ```python
    >>> p = Pilha()
    >>> p.empilha('um')
    >>> p.empilha('carro')
    >>> p.empilha('mouse')
    >>> exibe_pilha(p)
    um
    carro
    mouse
    >>> p.desempilha()
    'mouse'
    >>> p.desempilha()
    'carro'
    >>> p.desempilha()
    'um'
    ```

@) Projete uma função que receba como parâmetro duas pilhas e troque os elementos de uma pilha com os elementos da outra pilha.

@) (Desafio) Faça uma implementação alternativa do TAD Pilha que use uma única string para armazenar todos os elementos da pilha.

<!-- Fila -->

@) Modifique a implementação de `Fila` do aquivo `fila_fim.py` adicionando um método para verificar se a fila está cheia. Use o novo método para simplificar a implementação de `enfileira`.

@) Modifique a implementação de `Fila` do aquivo `fila_inicio_fim.py` adicionando um método para verificar se a fila está cheia. Use o novo método para simplificar a implementação de `enfileira`.

@) Modifique a implementação de `Fila` dos arquivos `fila_fim.py`, `fila_inicio_fim.py` e `fila_circular.py` para que o construtor receba como parâmetro a quantidade máxima de elementos que a fila pode armazenar. Adicione um método que devolve a capacidade da fila e ajuste os exemplos para funcionarem com essas modificações.

@) A implementação de `Fila` do arquivo `fila_circular.py` usa a ideia de "índice circular", quando o índice chega no final no arranjo, ele volta para o início. Essa ideia é usada nos métodos `enfileira`, `desenfileira` e `cheia`. Crie um método auxiliar para calcular o próximo índice a partir de um índice qualquer e use esse método para simplificar a implementação dos métodos `enfileira`, `desenfileira` e `cheia`.

@) Implemente a função chamada `tempo_fila` do arquivo abaixo:

    ```python
    from fila_inicio_fim import Fila
    # from fila_fim import Fila

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
    ```

    Execute o arquivo com o comando `python arquivo.py` e veja na saída os tempos de execução da função `tempo_fila` para $n = 1000, 2000, 4000$.

    Troque a implementação de fila usada no arquivo comentando a linha `from fila_inicio_fim import Fila` e descomentando a linha `from fila_fim import Fila`.

    Execute novamente o arquivo e observe os tempos de execução.

    Os tempos de execução foram diferentes? Explique.

@) Implemente uma fila usando duas pilhas.

@) Implemente uma pilha usando duas filas.

@) (Desafio) Faça uma implementação alternativa do TAD Fila que use uma única string para armazenar todos os elementos da fila.
