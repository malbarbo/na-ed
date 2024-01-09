---
title: Estruturas de dados lineares - Alocação contígua - Prática
urlcolor: Blue
---

<!-- Pilha -->

@) Modifique a implementação de `Pilha` vista em sala adicionando um método para verificar se a pilha está cheia.

@) Modifique a implementação de `Pilha` (do exercício anterior) para que o construtor receba como parâmetro a quantidade máxima de elementos (capacidade) que a pilha pode armazenar. Adicione também um método que devolve a capacidade da pilha.

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
