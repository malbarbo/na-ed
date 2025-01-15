---
# vim: set spell spelllang=pt_br sw=4:
title: |
       | Estruturas de dados
       | Tabelas de dispersão
numbersections: false
urlcolor: Blue
---

## Introdução

@) O que é endereçamento direto?

@) O que é colisão?

@) O que uma função de dispersão? Qual é a principal característica de uma boa função de dispersão?

@) O que são tabelas de dispersão?


## Começando

@) Considerando uma tabela com $m = 9$ e a função de dispersão $h(k) = k \mod m$, mostre como fica uma tabela de dispersão após a inserção das chaves 5, 28, 19, 15, 20, 33, 12, 17 e da remoção das chaves 15, 5 e 12.

    a) Use uma tabela com encadeamento
    b) Use uma tabela com endereçamento aberto e sondagem linear

@) Quais os cuidados devem ser tomados na implementação da remoção usando endereçamento aberto.

@) Explique o conceito de fator de carga e porque ele é importante.


## Praticando

@) Implemente a função de dispersão baseada em multiplicação: $h(k) = \left \lfloor m \times (k \times A \mod 1) \right \rfloor$. Use $A = 1.618033$. Não esqueça de colocar valores negativos nos exemplos. Faça o primeiro exercício da seção anterior usando essa função de dispersão.

@) Projete uma função de dispersão que mapeia uma string para um inteiro. A função deve multiplicar o _code point_ armazenado em cada posição da string pelo valor da posição mais 1 e somar os resultados.

@) Implemente as funções de inserção e remoção em dicionário usando tabela de dispersão com endereçamento aberto e sondagem linear. Não é necessário tratar o redimensionamento da tabela.


## Avançando

@) Modifique a implementação do exercício anterior e adicione o redimensionamento da tabela quando o fator de carga ficar muito pequeno ou muito grande.
