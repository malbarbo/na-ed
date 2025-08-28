---
# vim: set spell spelllang=pt_br sw=4:
title: |
       | Estruturas de dados
       | Recursividade
numbersections: false
urlcolor: Blue
---

## Introdução

@) O que é uma função recursiva?

@) Qual é a relação entre decomposição de um problema e recursividade?

@) Qual é a relação entre tipos com autorreferência e funções recursivas?

@) O que é recursão estrutural?


## Começando

<!-- lista, algum -->
@) Projete uma função recursiva que determine se algum dos elementos de uma lista encadeada é ímpar.

<!-- list, máximo -->
@) Projete uma função recursiva que encontre o valor máximo de uma lista encadeada. Se a lista for vazia, a função deve devolver `None`{.python}.

<!-- natural, repetição -->
@) Projete uma função recursiva que receba como entrada uma string e um número natural $n$ e devolva a string repetida $n$ vezes. Por exemplo, para a string `'casa'`{.python} e $n = 3$, a função deve produzir `'casacasacasa'`{.python}. Não use o operador de repetição de string (`*`{.python})!

<!-- arranjo, frequência -->
@) Projete uma função recursiva que conte quantas vezes um número aparece em um arranjo.


## Praticando


<!-- lista - modificação -->
@) Projete uma função recursiva que receba como entrada uma lista encadeada de strings e um número natural $n$, e modifique as strings da lista para que todas fiquem com tamanho $n$. Se uma string tem tamanho maior que $n$, os caracteres do final devem ser descartados. Se uma string tem tamanho menor que $n$, espaços em branco devem ser adicionados ao final da string.

<!-- natural, repetição -->
@) Projete uma função recursiva que receba como entrada um número $a$ (diferente de 0) e um número natural $n$ e
calcule o valor $a^n$.

<!-- lista, filter -->
@) Projete uma função recursiva que receba como entrada uma lista encadeada e crie uma nova lista encadeada com os elementos positivos da lista de entrada.

<!-- arranjo -->
@) Projete uma função recursiva que encontre o tamanho máximo entre todas as strings de um arranjo de strings.


## Avançando

<!-- natural, par, impar -->
@) Recursão indireta é quando duas ou mais funções chamam uma a outra. Defina duas funções `impar` e `par`, uma em termos da outra, isto é, a função `impar` deve chamar a função `par` e a função `par` deve chamar a função `impar` (a recursão para no caso base).

<!-- arranjo, verificação ordenação -->
@) Projete uma função recursiva que verifique se um arranjo de números está em ordem não decrescente. Dica: use dois casos base.

<!-- lista - filter in loco-->
@) Projete uma função recursiva que receba como entrada uma lista encadeada de números e remova todas as ocorrências do valor 0.

<!-- natural, cria lista -->
@) Projete uma função recursiva que receba como entrada dois números naturais, $n$ e $x$, onde $x \le n$ e devolva um arranjo com os divisores de $n$ que são menores ou iguais a $x$. Por exemplo, para $n = 16$ e $x = 7$, a função deve produzir `[1, 2, 4]`{.python}.


## Desafios

@) Dados duas listas encadeadas `lsta` e `lstb`, projete uma função recursiva que verifique se `lsta` é prefixo de `lstb`, isto é, se `lstb` começa com `lsta`.

@) Projete uma função recursiva que altere um arranjo de números, ordenando os seus elementos em ordem não decrescente.
