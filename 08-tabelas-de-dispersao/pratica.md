---
title: Tabelas de dispersão - Prática
urlcolor: Blue
---

@) Implemente a função de dispersão baseada em multiplicação: $h(k) = \left \lfloor m \times (k \times A \mod 1) \right \rfloor$. Use $A = 1.618033$. Não esqueça de colocar valores negativos nos exemplos.

@) Considerando uma tabela com $m = 9$ e a função de dispersão $h(k) = k \mod m$, mostre como fica uma tabela de dispersão após a inserção das chaves 5, 28, 19, 15, 20, 33, 12, 17 e da remoção das chaves 15, 5 e 12.

    a) Use uma tabela com encadeamento
    b) Use uma tabela com endereçamento aberto e sondagem linear

@) Faça o mesmo que o exercício anterior, mas use a função de dispersão do exercício 1.

@) Projete uma função de dispersão que mapeia uma string para um inteiro. A função deve multiplicar o _code point_ armazenado em cada posição da string pelo valor da posição mais 1 e somar os resultados.

@) Implemente as funções de inserção e remoção em dicionário usando tabela de dispersão com endereçamento aberto e sondagem linear. Não precisa tratar o caso em que não há espaço na tabela.
