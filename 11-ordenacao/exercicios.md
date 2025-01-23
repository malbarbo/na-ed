---
# vim: set spell spelllang=pt_br sw=4:
title: |
       | Estruturas de dados
       | Ordenação
numbersections: false
urlcolor: Blue
---

## Introdução

@) Descreva o problema de ordenação.

@) O que é uma ordenação in-loco?

@) O que é uma ordenação estável?

@) Qual é a ideia geral de um algoritmo incremental?

@) Qual é a ideia geral de um algoritmo de divisão e conquista?


## Começando

@) Crie um exemplo de arranjo que mostre que a ordenação por seleção não é estável.

@) Explique qual é a relação entre os algoritmos de ordenação por inserção, seleção e heap.

@) O arranjo `[23, 17, 14, 6, 13, 10, 1, 5, 7, 12]` representa um heap máximo?

@) Mostre passo a passo a construção de um heap mínimo a partir do arranjo `[5, 1, 7, 4, 9, 1, 3, 4, 8, 6]`.

@) Crie um exemplo de arranjo que mostre que a ordenação por heap não é estável.

@) Explique qual é a relação entre os algoritmos de ordenação por intercalação e particionamento.

<!--
@) Qual é o resultado do particionado do arranjo `[23, 17, 14, 6, 13, 10, 1, 5, 7, 12]` usando o algoritmo de Lomuto? E usando o algoritmo não in-loco do material?

@) Crie um exemplo de arranjo que mostre que a ordenação por seleção usando o particionamento de Lomuto é instável.

@) A ordenação por baldes pode ser usadas para chaves inteiras? Explique.
-->


## Praticando

@) Faça uma implementação iterativa da função `concerta_heap`.

@) Um outro algoritmo de ordenação é a ordenação por flutuação (do inglês, _bubble-sort_). A ideia do algoritmo é percorrer os elementos da sequência diversas vezes e fazer o maior elemento "flutuar" para o final. Isto pode ser feito da seguinte forma: a cada passagem pelos elementos, cada par de elementos adjacentes e comparado e trocando de lugar se o primeiro for maior que o segundo. O algoritmo para quando uma passagem por todos os elementos não gerar nenhum troca (você consegue ver porque o algoritmo funciona?). Implemente o algoritmo de ordenação por flutuação para arranjos e listas encadeadas. Determine a complexidade de tempo, se ele é in-loco e se é estável.

<!--
@) Partindo do arquivo `ordena_encadeamento.py`, implemente o algoritmo de ordenação por inserção para listas encadeadas. Faça uma versão in-loco e outra que devolve uma nova lista. Qual você achou mais simples?

@) Partindo do arquivo `ordena.py`, implemente uma versão do algoritmo de ordenação por inserção para arranjos em que a parte ordenada fique no final do arranjo.
-->

@) Partindo do arquivo `ordena_encadeamento.py`, implemente o algoritmo de ordenação por seleção para listas encadeadas. Faça uma versão in-loco e outra que devolve uma nova lista. Qual você achou mais simples?

<!--
@) Partindo do arquivo `ordena.py`, implemente uma versão do algoritmo de ordenação por seleção para arranjos em que a parte ordenada fique no final do arranjo.
-->


## Avançando

@) Projete a função `intercala(lst: list[int], ini: int, meio: int, fim: int)`{.python} que intercala os elementos de `lst[ini:meio]`{.python} (que está ordenado) com `lst[meio:fim]`{.python} (que está ordenado) de maneira que `lst[ini:fim]`{.python} fique ordenado. Dica: cria arranjos auxiliares.

@) Projete uma função que implemente o esquema de particionamento de Hoare.
