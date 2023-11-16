---
# vim: set spell spelllang=pt_br:
title: Motivação
---


# Problema

\small

Um sítio de conteúdo pretende fazer uma serie de postagens com as palavras e expressões mais comuns em diversos idiomas, incluindo também listas especializadas para determinadas áreas (como engenharia, culinária, etc).

Para criar as listas foi levantado diversos corpus (coleções de textos) para cada possível postagem. Também foi contratado especialistas em cada idioma / área. Para ajudar os especialistas existe a necessidade de processar os textos e gerar uma lista preliminar das palavras mais frequentes.

Uma equipe já pré-processou os corpus e gerou um arquivo texto contendo uma palavra/expressão por linha. Cada arquivo tem entre 1000 e 1000000 de palavras. Essa equipe também já criou uma função para ler o arquivo e devolver uma lista com cada palavra/expressão de um arquivo.

Agora é preciso um programa que analise uma lista e gere uma tabela com as palavras/expressões com o número de vezes (frequência) que cada uma aparece na lista (com as que mais aparecem primeiro).


# Dinâmica

Forme equipes de até 5 pessoas. \pause

Proponha um algoritmo para resolver esse problema. \pause

Apresente o algoritmo usando um exemplo.


# Estratégias

Abordagem incremental direta:

\pause

- Temos uma lista de palavras e frequência (em ordem de maior frequência) e temos uma palavra. Precisamos atualizar a lista considerando a palavra: \pause

    - Se a palavra está na lista, aumentamos a frequência em 1 e "movemos" a palavra para manter a lista em ordem. \pause
    - Senão adicionamos na lista a palavra com a frequência 1.


# Estratégias

Abordagem usado um plano: \pause

- Calculamos a frequência de cada palavra e criamos uma lista \pause

- Ordenamos a lista \pause


Como calcular a frequência de cada palavra? \pause

- Usando o método incremental \pause

- Ordenando a lista e contando as palavras iguais consecutivas \pause


Como ordenar a lista por frequência? \pause

- Usando a ordenação por seleção. Encontramos a palavra com maior frequência e colocamos na posição 0 da lista, repetimos o processo para as posições 1, 2, ... até a última posição da lista.


# Perguntas

Como avaliar quais desses algoritmos é mais viável? \pause

Como avaliar se _algum_ desses algoritmos é viável? \pause

Se os algoritmos funcionam corretamente, porque algum pode não ser viável? \pause

Vamos ver as implementações e como elas funcionam para dados reais.


# Conclusões

Conclusões

- Mesmo que um algoritmo funcione corretamente, ele pode ser inviável devido ao seu tempo de execução. \pause

- Precisamos de uma forma para determinar o tempo de execução de um algoritmo sem precisar implementá-lo. \pause

- As estruturas de dados são essenciais para algoritmos eficientes. \pause

- Os tipos abstratos de dados nos ajudam na decomposição do problema. \pause

- Algoritmos de ordenação eficientes são importantes para a computação.
