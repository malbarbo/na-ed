---
# vim: set spell spelllang=pt_br:
title: Ordenação
linkcolor: Black
urlcolor: Blue
---

## Introdução

Junto com o problema de busca, o problema de ordenação é um dos mais estudados da Computação. \pause

O problema de ordenação consiste em, dado uma sequência de $n$ números $\langle a_1, a_2, \ldots, a_n \rangle$, determinar uma permutação (reordenação) $\langle a_1', a_2', \ldots, a_n' \rangle$ da sequência de entrada tal que, $a_1' \leq a_2' \leq \dots \leq a_n'$.


## Introdução

Para avaliarmos os algoritmos de ordenação, além da complexidade de tempo, consideramos o uso extra de memória e se a ordenação é estável. \pause

Um algoritmo é **in-loco** se a quantidade de memória que ele precisa para executar é $O(1)$, ou seja, não depende do tamanho da entrada. \pause

Um algoritmo de ordenação é **estável** se a ordem relativamente dos elementos com a mesma chave é preservado.


## Introdução

Veremos agora o projeto de diversos algoritmos de ordenação. \pause Eles são baseados nas seguintes técnicas de projeto: \pause

- Incremental \pause

- Divisão e conquista \pause

- _Ad hoc_ (específicos, sem técnica geral)


## Projeto de algoritmos incremental

A ideia de um algoritmo incremental é: \pause

- Iniciar com a solução para um problema trivial; \pause

- Estender a solução iterativamente para um problema maior até obter a solução do problema que queremos resolver; \pause


Como projetar um algoritmo incremental para somar os elementos de um arranjo? \pause

- Começamos com a soma do arranjo vazio que é 0; \pause

- Estendemos a soma adicionando um elemento do arranjo por vez até que todos os elementos tenham sido somados.


## Ordenação incremental

Como projetar um algoritmo incremental para ordenar os elementos de um arranjo? \pause

- Iniciamos com um subarranjo vazio já ordenado; \pause

- Estendemos o subarranjo já ordenado selecionando um elemento por vez até que todos os elementos tenham sido selecionados.

![](imagens/ordenado-resto.pdf){width=6cm} \pause

Temos que tomar duas decisões para tornar o processo concreto: \pause

- Como selecionar o próximo elemento? \pause

- Como estender o subarranjo ordenado?


## Ordenação por inserção

![](imagens/ordenado-resto.pdf){width=6cm}

Como selecionar o próximo elemento? \pause

- Pegamos o primeiro elemento do restante. \pause
- Qual é o custo? \pause $O(1)$ \pause

Como estender o subarranjo ordenado? \pause

- Inserindo o elemento selecionado na parte ordenada. \pause
- Qual é o custo? \pause $O(j)$ \pause

Este algoritmo é conhecido como **ordenação por inserção** (_insertion sort_).


## Ordenação por inserção

<div class="columns">
<div class="column" width="25%">
\includegraphics[trim=140pt 380pt 2000pt 50pt,clip]{imagens/Fig-2-2.pdf} \pause
</div>
<div class="column" width="25%">
\includegraphics[trim=1140pt 380pt 1000pt 50pt,clip]{imagens/Fig-2-2.pdf} \pause
</div>
<div class="column" width="25%">
\includegraphics[trim=2140pt 380pt 0pt 50pt,clip]{imagens/Fig-2-2.pdf} \pause
</div>
</div>

<div class="columns">
<div class="column" width="25%">
\includegraphics[trim=140pt 0pt 2000pt 450pt,clip]{imagens/Fig-2-2.pdf} \pause
</div>
<div class="column" width="25%">
\includegraphics[trim=1140pt 0pt 1000pt 450pt,clip]{imagens/Fig-2-2.pdf} \pause
</div>
<div class="column" width="25%">
\includegraphics[trim=2140pt 0pt 0pt 450pt,clip]{imagens/Fig-2-2.pdf}
</div>
</div>


## Ordenação por inserção

<div class="columns">
<div class="column" width="53%">
Projete uma função que implemente o algoritmo de ordenação por inserção. \pause

\scriptsize

```python
def ordena_insercao(lst: list[int]):
    '''
    Ordena *lst* em ordem não decrescente usando
    o algoritmo de ordenação por inserção.
    Exemplos
    >>> lst = [5, 2, 4, 6, 1, 3]
    >>> ordena_insercao(lst)
    >>> lst
    [1, 2, 3, 4, 5, 6]
    '''
```

\pause

```python
    for i in range(1, len(lst)):
        j = i
        while j > 0 and lst[j - 1] > lst[j]:
            lst[j - 1], lst[j] = lst[j], lst[j - 1]
            j -= 1
```

</div>
<div class="column" width="43%">
\pause
Qual é a complexidade de tempo da ordenação por inserção? \pause

Qual é o melhor caso? \pause `lst` está em ordem não decrescente, o corpo do `while`{.python} não é executado nenhuma vez. \pause A complexidade de tempo é $O(n)$. \pause

Qual é o pior caso? \pause `lst` está em ordem não crescente, \pause na iteração `i` o corpo do `while`{.python} é executado `i` vezes. \pause A complexidade de tempo é $\displaystyle \sum_{i=1}^{n - 1} i = O(n^2)$. \pause

A implementação é in-loco? \pause Sim. \pause

A ordenação é estável? \pause Sim.

</div>
</div>


## Melhoria

Podemos melhor o tempo? \pause

Temos dois custos, o de seleção, que é $O(1)$, e o de inserção, que é $O(j)$. \pause Podemos melhor o tempo da inserção? \pause

Considerando que o subarranjo `lst[:j]` está ordenado, poderíamos usar uma busca binária para encontrar a posição de inserção em $O(\lg j)$. \pause No entanto, a inserção continuaria sendo $O(j)$, pois os elementos precisar ser deslocados. \pause

Podemos fazer uma "inserção" sem fazer o deslocamento dos elementos? \pause Sim!


## Ordenação por seleção

![](imagens/ordenado-resto.pdf){width=6cm}

Como selecionar o próximo elemento? \pause

- Pegamos o menor elemento do restante. \pause
- Qual é o custo? \pause $O(n - j)$ \pause

Como estender o subarranjo ordenado? \pause

- Trocando de posição o menor elemento com o primeiro do restante. \pause
- Qual é o custo? \pause $O(1)$ \pause

Este algoritmo é conhecido como **ordenação por seleção** (_selection sort_).


## Ordenação por seleção

<div class="columns">
<div class="column" width="53%">
Projete uma função que implemente o algoritmo de ordenação por seleção. \pause

\scriptsize

```python
def ordena_selecao(lst: list[int]):
    '''
    Ordena *lst* em ordem não decrescente usando
    o algoritmo de ordenação por inserção.
    Exemplos
    >>> lst = [5, 2, 4, 6, 1, 3]
    >>> ordena_insercao(lst)
    >>> lst
    [1, 2, 3, 4, 5, 6]
    '''
```

\pause

```python
    for i in range(len(lst)):
        m = i # índice do menor em lst[i:]
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[m]:
                m = j
        lst[i], lst[m] = lst[m], lst[i]
```

</div>
<div class="column" width="43%">
\pause
Qual é a complexidade de tempo da ordenação por seleção? \pause

Cada iteração `i` o corpo do segundo `for`{.python} é executado `n - i - 1` vezes. \pause A complexidade de tempo é $\displaystyle \sum_{i=0}^{n - 1} n - i - 1 = O(n^2)$. \pause

A implementação é in-loco? \pause Sim. \pause

A ordenação é estável? \pause Sim. \pause

A ordenação por seleção é mais eficiente do que a ordenação por inserção? \pause Não...

</div>
</div>


## Melhoria

Quando projetamos o algoritmo de ordenação por seleção nós movemos o custo de inserção para a seleção e
vice e versa… \pause Parece que não ganhamos nada! \pause

Mas isso não é verdade, agora podemos abordar o problema por outro ângulo! \pause

### Antes

Tentamos diminuir o tempo para inserir em um arranjo ordenado (parece muito rígido). \pause

### Agora

Vamos tentar diminuir o tempo para selecionar o valor mínimo de um arranjo (parece mais flexível).


## Heap

Um **heap** (binário) é um arranjo que pode ser visto como uma árvore binária quase completa:

![](imagens/Fig-6-1.pdf){width=10cm}

Cada nó da árvore corresponde ao elemento do arranjo que armazena o valor do nó.

A árvore está preenchida em todos os níveis, exceto talvez no nível mais baixo, que é preenchido a partir da esquerda.

Note que nesse exemplo o arranjo é indexado a partir de 1!


## Heap

Como o heap pode ser visto como árvore, ele também tem uma altura, que é $O(\lg n)$. \pause

É essa característica que permite que as operações em um heap sejam eficientes.


## Heap

Para arranjos indexados a partir de 0, a raiz do heap está na posição 0. \pause Além disso, para cada nó no índice $i$, os índices do pai e dos filhos a direita e a esquerda podem ser caculado da seguinte forma: \pause

$\proc{pai}(i) = \lfloor (i - 1) / 2 \rfloor$ \pause

$\proc{esq}(i) = 2 i + 1$ \pause

$\proc{dir}(i) = 2 i + 2$

<!--
\pause

Um arranjo $A$ que representa um heap tem dois atributos

- $\attrib{A}{length}$, que é o tamanho do arranjo; e
- $\attrib{A}{heap-size}$, que é o número de elementos do heap ($0 \le \attrib{A}{heap-size} \le \attrib{A}{length}$)

-->

## Propriedade do heap

Em um **heap máximo** armazenado em um arranjo $A$, para cada nó $i$ diferente da raiz
$$A[\proc{pai}(i)] \ge A[i]$$

\pause

Em um **heap mínimo** armazenado em um arranjo $A$, para cada nó $i$ diferente da raiz
$$A[\proc{pai}(i)] \le A[i]$$

\pause

Em um heap máximo, onde está o maior elemento? \pause Na raiz. \pause

Em um heap mínimo, onde está o menor elemento? \pause Na raiz.


## Heap e ordenação

Como utilizar um heap máximo em um processo de ordenação incremental? \pause

![](imagens/heap-ordenado.pdf){width=6cm}

- Mantemos a porção ordenada no final do arranjo;
- E o heap na porção inicial.


## Heap e ordenação

![](imagens/heap-ordenado.pdf){width=6cm}

Como selecionar o próximo elemento? \pause

- Pegamos o maior elemento do heap. \pause
- Qual é o custo? \pause $O(\log(heap-size))$ -- veremos isso a seguir. \pause

Como estender o subarranjo ordenado? \pause

- Trocando de posição o maior elemento com o último do restante. \pause
- Qual é o custo? \pause $O(1)$. \pause

Este algoritmo é conhecido como **ordenação por heap** (_heap sort_).


## Exemplo da ordenação por heap

\includegraphics[trim=0cm 90cm 84.65cm 0cm, clip, width=8cm]{imagens/Fig-6-4.pdf}

\large

```
       | 16 | 14 | 10 |  8 |  7 |  9 |  3 |  2 |  4 |  1 |
       \_____________________ heap ______________________/
```


## Exemplo da ordenação por heap

\includegraphics[trim=42.34cm 90cm 42.31cm 0cm, clip, width=8cm]{imagens/Fig-6-4.pdf}

\large

```
       | 14 |  8 | 10 |  4 |  7 |  9 |  3 |  2 |  1 | 16 |
       \__________________ heap ____________________/
```


## Exemplo da ordenação por heap

\includegraphics[trim=84.68cm 90cm 0cm 0cm, clip, width=8cm]{imagens/Fig-6-4.pdf}

\large

```
       | 10 |  8 |  9 |  4 |  7 |  1 |  3 |  2 | 14 | 16 |
       \________________ heap _________________/
```


## Exemplo da ordenação por heap

\includegraphics[trim=0cm 60.9cm 84.65cm 29.1cm, clip, width=8cm]{imagens/Fig-6-4.pdf}

\large

```
       |  9 |  8 |  3 |  4 |  7 |  1 |  2 | 10 | 14 | 16 |
       \______________ heap ______________/
```


## Exemplo da ordenação por heap

\includegraphics[trim=42.34cm 60.9cm 42.31cm 29.1cm, clip, width=8cm]{imagens/Fig-6-4.pdf}

\large

```
       |  8 |  7 |  3 |  4 |  2 |  1 |  9 | 10 | 14 | 16 |
       \___________ heap ____________/
```


## Exemplo da ordenação por heap

\includegraphics[trim=84.68cm 60.9cm 0cm 29.1cm, clip, width=8cm]{imagens/Fig-6-4.pdf}

\large

```
       |  7 |  4 |  3 |  1 |  2 |  8 |  9 | 10 | 14 | 16 |
       \_________ heap _________/
```


## Exemplo da ordenação por heap

\includegraphics[trim=0cm 31.8cm 84.65cm 58.2cm, clip, width=8cm]{imagens/Fig-6-4.pdf}

\large

```
       |  4 |  2 |  3 |  1 |  7 |  8 |  9 | 10 | 14 | 16 |
       \______ heap _______/
```


## Exemplo da ordenação por heap

\includegraphics[trim=42.34cm 31.8cm 42.31cm 58.2cm, clip, width=8cm]{imagens/Fig-6-4.pdf}

\large

```
       |  3 |  2 |  1 |  4 |  7 |  8 |  9 | 10 | 14 | 16 |
       \____ heap ____/
```


## Exemplo da ordenação por heap

\includegraphics[trim=84.68cm 31.8cm 0cm 58.2cm, clip, width=8cm]{imagens/Fig-6-4.pdf}

\large

```
       |  2 |  1 |  3 |  4 |  7 |  8 |  9 | 10 | 14 | 16 |
       \_ heap __/
```


## Exemplo da ordenação por heap

\includegraphics[trim=0cm 2.7cm 84.65cm 87.3cm, clip, width=8cm]{imagens/Fig-6-4.pdf}
\large

```
       |  1 |  2 |  3 |  4 |  7 |  8 |  9 | 10 | 14 | 16 |
       \heap/
```


## Operações com heap

Que operações precisamos para implementar a ordenação por heap? \pause

- Inicialização do heap \pause
- Remoção do máximo \pause

Para implementar essas funções, vamos precisar de uma operação auxiliar, que "concerta" um heap.


## Concertando um heap

<div class="columns">
<div class="column" width="48%">
\includegraphics[trim=0cm 42.2cm 55.55cm 0cm, clip]{imagens/Fig-6-2.pdf}
</div>
<div class="column" width="48%">
Seja $A$ um arranjo que armazena um heap máximo.

Considerando que o elemento da posição $i$ foi alterado, como podemos verificar se a propriedade do heap se mantém, e caso contrário, como podemos "concertar" o heap? \pause

Verificamos se $A[i]$ é menor que algum dos dois filhos, \pause se sim, trocamos $A[i]$ de lugar com o maior filho,
</div>
</div>


## Concertando um heap

<div class="columns">
<div class="column" width="48%">
\includegraphics[trim=55.55cm 42.2cm 0cm 0cm, clip]{imagens/Fig-6-2.pdf}
</div>
<div class="column" width="48%">

Seja $A$ um arranjo que armazena um heap máximo.

Considerando que o elemento da posição $i$ foi alterado, como podemos verificar se a propriedade do heap se mantém, e caso contrário, como podemos "concertar" o heap?

Verificamos se $A[i]$ é menor que algum dos dois filhos, se sim, trocamos $A[i]$ de lugar com o maior filho, \pause depois executamos o processo recursivamente para o filho que foi trocado.
</div>
</div>


## Concertando um heap

<div class="columns">
<div class="column" width="48%">
\includegraphics[trim=0cm 2.5cm 55.55cm 39.7cm, clip]{imagens/Fig-6-2.pdf}
</div>
<div class="column" width="48%">
Seja $A$ um arranjo que armazena um heap máximo.

Considerando que o elemento da posição $i$ foi alterado, como podemos verificar se a propriedade do heap se mantém, e caso contrário, como podemos "concertar" o heap?

Verificamos se $A[i]$ é menor que algum dos dois filhos, se sim, trocamos $A[i]$ de lugar com o maior filho, depois executamos o processo recursivamente para o filho que foi trocado.
</div>
</div>


## Concertando um heap

<div class="columns">
<div class="column" width="48%">
Projete uma função que receba com parâmetro um arranjo $A$, a quantidade de elementos $n$ de $A$ que estão sendo usados e um índice $i$, onde os elementos `esq(i)` e `dir(i)` são raízes de heap máximo, e "concerte" o arranjo, se necessário, para que a árvore com raiz $i$ seja um heap máximo. \pause

</div>
<div class="column" width="48%">

\scriptsize

```python
def concerta_heap(A: list[int], n: int, i: int):
    assert i < n <= len(A)
    # Encontra o índice do maior entre
    # A[i], A[esq(i)] e A[dir(i)]
    fesq = esq(i)
    fdir = dir(i)
    imax = i
    if fesq < n and A[fesq] > A[imax]:
        imax = fesq
    if fdir < n and A[fdir] > A[imax]:
        imax = fdir
    # Se o maior não é A[i], ajusta e repete
    # o processo.
    if imax != i:
        A[i], A[imax] = A[imax], A[i]
        concerta_heap(A, n, imax)
```

\pause

\normalsize

Qual é a complexidade de tempo? \pause $O(\lg n)$.

</div>
</div>


## Construindo um heap

Como construir um heap? \pause Vamos começar com o que está certo e ir "consertando" até que todo o heap fique certo. \pause

\includegraphics[trim=0cm 81.7cm 55.55cm 7cm, clip, width=6cm]{imagens/Fig-6-3.pdf}

Dado um arranjo qualquer, que vamos transformar em um heap, quais elementos sabemos que são raízes de heap válidos? \pause As folhas.


## Construindo um heap

\includegraphics[trim=0cm 81.7cm 55.55cm 7cm, clip, width=6cm]{imagens/Fig-6-3.pdf}


## Construindo um heap

\includegraphics[trim=55.55cm 81.7cm 0cm 7cm, clip, width=6cm]{imagens/Fig-6-3.pdf}


## Construindo um heap

\includegraphics[trim=0cm 42cm 55.55cm 46.7cm, clip, width=6cm]{imagens/Fig-6-3.pdf}


## Construindo um heap

\includegraphics[trim=55.55cm 42cm 0cm 46.7cm, clip, width=6cm]{imagens/Fig-6-3.pdf}


## Construindo um heap

\includegraphics[trim=0cm 2.3cm 55.55cm 86.4cm, clip, width=6cm]{imagens/Fig-6-3.pdf}


## Construindo um heap

\includegraphics[trim=55.55cm 2.3cm 0cm 86.4cm, clip, width=6cm]{imagens/Fig-6-3.pdf}


## Construindo um heap

<div class="columns">
<div class="column" width="48%">
Projete uma função que receba com parâmetro um arranjo $A$, e rearranje os elementos de $A$ para formar um heap máximo.

\pause
</div>
<div class="column" width="48%">

\scriptsize

```python
def inicializa_heap(A: list[int]):
    for i in range(len(A) // 2 - 1, -1, -1):
        concerta_heap(A, len(A), i)
```

</div>
</div>

\vspace{0.5cm}

\pause

Qual é a complexidade de tempo? \pause

- Limite simples: a função é `concerta_heap` tem tempo $O(\lg n)$ e é chamada $n / 2$, portanto, $O(n \lg n)$ \pause

- Limite estrito: $O(n)$


## Implementação ordenação por heap

<div class="columns">
<div class="column" width="48%">
Projete uma função que implemente a ordenação por heap.

\pause
</div>
<div class="column" width="48%">

\scriptsize

```python
def ordena_heap(lst: list[int]):
    inicializa_heap(lst)
    for n in range(len(lst) - 1, 0, -1):
        # Troca o maior do heap com
        # o elemento da última posição do heap
        lst[0], lst[n] = lst[n], lst[0]
        # Concerta a raiz do heap
        concerta_heap(lst, n, 0)
```

</div>
</div>

\vspace{0.5cm}

\pause

Qual é a complexidade de tempo? \pause $O(n \lg n)$. \pause

A implementação é in-loco? \pause Sim. \pause

A implementação é estável? \pause Não.


## Projeto de algoritmos de divisão e conquista

A ideia de um algoritmo divisão e conquista é: \pause

- Resolver o problema diretamente se ele for trivial, senão **dividir** o problema em dois ou mais subproblemas do mesmo tipo; \pause

- **Conquistar** os subproblemas resolvendo-os recursivamente; \pause

- **Combinar** as soluções dos subproblemas para obter a solução do problema original \pause


Como projetar um algoritmo de divisão e conquista para somar os elementos de um arranjo? \pause

- Se o arranjo for vazio, a soma é 0. Senão dividir o arranjo na metade e calcular a soma de cada metade recursivamente; \pause

- Obter a soma do arranjo somando o resultado de cada metade;


## Ordenação incremental

Como projetar um algoritmo de divisão e conquista para ordenar os elementos de um arranjo? \pause

- Se o arranjo tiver mais que um elemento, separamos os elementos em dois subarranjos; \pause

- Ordenamos cada subarranjo recursivamente; \pause

- Combinamos os dois subarranjos para obter a ordenação do arranjo inicial. \pause


Temos que tomar duas decisões para tornar o processo concreto: \pause

- Como separar os elementos em dois subarranjos? \pause

- Como combinar os dois subarranjos ordenados?


## Ordenação por intercalação

Como separar os elementos em dois subarranjos? \pause

- Dividindo o arranjo ao meio; \pause

- Qual é o custo? \pause $O(1)$ \pause

Como combinar os dois subarranjos ordenados? \pause

- Fazendo a intercalação em ordem dos elementos dos subarranjos; \pause

- Qual é o custo? \pause $O(n)$ \pause

Este algoritmo é conhecido como **ordenação por intercalação** (_merge sort_).


## Ordenação por intercalação

![](imagens/mergesort.pdf){width=7cm}


## Ordenação por intercalação

<div class="columns">
<div class="column" width="43%">
Projete uma função que implemente o algoritmo de ordenação por intercalação.

\pause

\scriptsize

```python
def ordena_intercalacao(lst: list[int]):
    # Se o problema não é trivial
    if len(lst) > 1:
```

\pause

```python
        # Divide em dois subproblemas
        m = len(lst) // 2
        a = lst[:m]
        b = lst[m:]
```

\pause

```python
        # Conquista recursivamente
        ordena_intercalacao(a)
        ordena_intercalacao(b)
```

\pause

```python
        # Combina as soluções
        intercala(lst, a, b)
```

\pause

</div>
<div class="column" width="52%">

Projete uma função que implemente a intercalação.

\pause

\scriptsize

```python
def intercala(lst: list[int], a: list[int], b: list[int]):
    '''
    Faz a intercalação em ordem não decrescente dos
    elementos de *a* e *b* em *lst*.

    Requer que len(lst) = len(a) + len(b).
    Requer que a e b estekam em ordem não decrescente.

    Exemplos
    >>> lst = [0, 0, 0, 0, 0, 0, 0]
    >>> intercala(lst, [1, 6], [3, 5, 6, 8, 10])
    >>> lst
    [1, 3, 5, 6, 6, 8, 10]
    >>> intercala(lst, [3, 5, 6, 8, 10], [1, 6])
    >>> lst
    [1, 3, 5, 6, 6, 8, 10]
    '''
```

</div>
</div>


## Ordenação por intercalação

<div class="columns">
<div class="column" width="43%">
Projete uma função que implemente o algoritmo de ordenação por intercalação.

\scriptsize

```python
def ordena_intercalacao(lst: list[int]):
    # Se o problema não é trivial
    if len(lst) > 1:
```

```python
        # Divide em dois subproblemas
        m = len(lst) // 2
        a = lst[:m]
        b = lst[m:]
```

```python
        # Conquista recursivamente
        ordena_intercalacao(a)
        ordena_intercalacao(b)
```

```python
        # Combina as soluções
        intercala(lst, a, b)
```

</div>
<div class="column" width="52%">

\scriptsize

```python
def intercala(lst: list[int], a: list[int], b: list[int]):
    assert len(lst) == len(a) + len(b)
    i, j, k = 0, 0, 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            lst[k] = a[i]
            i += 1
        else:
            lst[k] = b[j]
            j += 1
        k += 1
    while i < len(a): # Copia o restante de a
        lst[k] = a[i]
        i += 1
        k += 1
    while j < len(b): # Copia o restante de b
        lst[k] = b[j]
        j += 1
        k += 1
```

</div>
</div>


## Ordenação por intercalação

<div class="columns">
<div class="column" width="43%">
Projete uma função que implemente o algoritmo de ordenação por intercalação.

\scriptsize

```python
def ordena_intercalacao(lst: list[int]):
    # Se o problema não é trivial
    if len(lst) > 1:
```

```python
        # Divide em dois subproblemas
        m = len(lst) // 2
        a = lst[:m]
        b = lst[m:]
```

```python
        # Conquista recursivamente
        ordena_intercalacao(a)
        ordena_intercalacao(b)
```

```python
        # Combina as soluções
        intercala(lst, a, b)
```

</div>
<div class="column" width="52%">

Qual é a complexidade de tempo de `intercala`? \pause $O(n)$. \pause

A implementação da ordenação por intercalação é in-loco? \pause Não. \pause

É estável? Sim. \pause

Qual é a complexidade de tempo de `ordena_intercalacao`? \pause

$$T(n) =
    \begin{cases}
      c               & \text{se $n \le 1$} \\
      2T(n/2) + cn    & \text{caso contrário}
    \end{cases}$$

\pause

$T(n) = O(n \lg n)$

</div>
</div>


## Ordenação por intercalação

<div class="columns">
<div class="column" width="40%">
Podemos fazer melhor? \pause Vamos tentar! \pause

Mas antes, vamos ver a forma mais comum de implementar a ordenação por intercalação, que é utilizando índices para informar o intervalo de ordenação / intercalação.

\pause

Note que nessa versão a cópia dos subarranjos geralmente é feita na função `intercala`.

\pause

</div>
<div class="column" width="55%">
\scriptsize

```python
def ordena_intercalacao(lst: list[int], ini: int, fim: int):
    '''
    Ordena o subarranjo lst[ini:fim] em ordem não
    decrescente.
    Requer que 0 <= i <= fim <= len(lst).
    '''
```

\pause

```python
    # Se o problema não é trivial
    if ini < fim - 1:
```

\pause

```python
        # Divide em dois subproblemas
        meio = (ini + fim) // 2
```

\pause

```python
        # Conquista recursivamente
        ordena_intercalacao(lst, ini, meio)
        ordena_intercalacao(lst, meio, fim)
```

\pause

```python
        # Combina as soluções
        intercala(lst, ini, meio, fim)
```

\pause

</div>
</div>

Projete essa versão de `intercala`.


## Divisão e conquista

No projeto de um algoritmo de divisão e conquista temos que tomar duas decisõe: \pause

- Como separar os elementos em dois subarranjos? \pause

- Como combinar os dois subarranjos ordenados? \pause

Na ordenação por intercalação, a etapa de divisão é constante e a de combinação linear. Então, se queremos mudar o tempo de execução, precisamos pensar em como melhorar a combinação.


## Divisão e conquista

Como combinar dois arranjos ordenados sem precisar passar por todos os elementos? \pause Parece que não tem com... \pause

Se não podemos melhorar, será que podemos eliminar a etapa de combinação? \pause

Supondo que o arranjo de entrada `lst[0:n]`{.python} seja dividido em `lst[0:p]`{.python} e `lst[p:n]`{.python}, o que é necessário para que após a ordenação de `lst[0:p]`{.python} e `lst[p:n]`{.python} o arranjo `lst[0:n]`{.python} fique ordenado sem precisarmos fazer mais nada? \pause

Os elementos de `lst[0:p]`{.python} devem ser menores ou iguais aos elementos de `lst[p:n]`{.python}!


## Particionamento

<div class="columns">
<div class="column" width="40%">

Então, o que precisamos fazer? \pause

Projetar uma função que particione um arranjo em duas partes, um com os "menores" e outra com os "maiores". \pause Para isso vamos precisar de um "pivô" para determinar em que parte cada elemento deve ficar. \pause

\includegraphics[trim=8cm 79cm 0cm 3cm, clip, width=4cm]{imagens/Fig-7-1.pdf}

\vspace{-0.5cm}

\pause \center $\downarrow$

\includegraphics[trim=8cm 0cm 0cm 82cm, clip, width=4cm]{imagens/Fig-7-1.pdf}

</div>
<div class="column" width="55%">
Especifique a função para fazer o particionamento de um subarranjo. A função deve devolver o índice que separa as duas partes.

\scriptsize

```python
def particiona(lst: list[int], ini: int, fim: int) -> int:
    '''
    Reorganiza os elementos de lst[ini:fim] e devolve um
    índice p de maneira que os elementos de lst[ini:p]
    são menores que lst[p:fim].

    Exemplos
    >>> lst = [2, 8, 7, 1, 3, 5, 6, 4]
    >>> particiona(lst, 0, len(lst))
    3
    >>> lst
    [2, 1, 3, 4, 8, 7, 5, 6]
    '''
```
</div>
</div>


## Ordenação por partição

O algoritmo de ordenação de divisão e conquista baseado na função de particionamento é chamado de **ordenação por particionamento** ou **quick sort**.

\pause

Implemente a ordenação por particionamento.


## Ordenação por partição

<div class="columns">
<div class="column" width="48%">

\scriptsize

```python
def ordena_particionamento(lst: list[int], ini: int, fim: int):
    '''
    Ordena o subarranjo lst[ini:fim] em ordem não
    decrescente.

    Requer que 0 <= i <= fim <= len(lst).
    '''
```

\pause

```python
    # Se o problema não é trivial
    if ini < fim - 1:
```

\pause

```python
        # Divide em dois subproblemas
        p = particiona(lst, ini, fim)
```

\pause

```python
        # Conquista recursivamente
        ordena_particionamento(lst, ini, p)
        ordena_particionamento(lst, p, fim)
```

\pause

```python
        # As soluções já estão combinadas!
```

\pause

</div>
<div class="column" width="48%">

\scriptsize

```python







def ordena_intercalacao(lst: list[int], ini: int, fim: int):
```

```python
    # Se o problema não é trivial
    if ini < fim - 1:
```

```python
        # Divide em dois subproblemas
        meio = (ini + fim) // 2
```

```python
        # Conquista recursivamente
        ordena_intercalacao(lst, ini, meio)
        ordena_intercalacao(lst, meio, fim)
```

```python
        # Combina as soluções
        intercala(lst, ini, meio, fim)
```
</div>
</div>
