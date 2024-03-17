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

Para avaliarmos os algoritmos de ordenação usamos normalmente, além da complexidade de tempo, o uso extra de memória e se a ordenação é estável. \pause

Um algoritmo é **in-loco** se a quantidade de memória que ele precisa para executar é $O(1)$, ou seja, não depende do tamanho da entrada. \pause

Um algoritmo de ordenação é **estável** se a ordem relativamente dos elementos com a mesma chave é preservado.


## Introdução

Veremos agora o projeto de diversos algoritmos de ordenação e também vamos discutir suas características. \pause

Os algoritmos que veremos são baseados nas seguintes técnicas de projeto: \pause

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

Como selecionar o próximo elemento? \pause Pegamos o primeiro elemento do restante. \pause

Como estender o subarranjo ordenado? \pause Inserindo o elemento selecionado na parte ordenada. \pause

Este algoritmo é conhecido como **ordenação por inserção**. \pause

Considerado que o tamanho da parte ordenada é $j$ e o tamanho do restante é $n - j$, qual é o tempo para selecionar um elemento? \pause $O(1)$. \pause E para inserir o elemento selecionado na parte ordenada? \pause $O(j)$.


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
    for i in range(1, len(lst)):
        j = i
        while j > 0 and lst[j - 1] > lst[j]:
            lst[j - 1], lst[j] = lst[j], lst[j - 1]
            j -= 1
```

</div>
<div class="column" width="43%">
\pause
Qual a complexidade de tempo da ordenação por inserção? \pause

Qual é o melhor caso? \pause `lst` está em ordem não decrescente, o corpo do `while`{.python} não é executado nenhuma vez. \pause A complexidade de tempo é $O(n)$. \pause

Qual é o pior caso? \pause `lst` está em ordem não crescente, \pause na iteração `i` o corpo do `while`{.python} é executado `i` vezes. \pause A complexidade de tempo é $\displaystyle \sum_{i=1}^{n - 1} i = O(n^2)$. \pause

A implementação é in-loco? \pause Sim. \pause

A ordenação é estável? \pause Sim.

</div>
</div>
