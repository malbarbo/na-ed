---
# vim: set spell spelllang=pt_br sw=4:
title: |
       | Estruturas de dados
       | Árvores binárias de busca
numbersections: false
urlcolor: Blue
---

## Introdução

@) O que é uma árvore binária?

@) Qual é o modelo de função para funções que processam árvores binárias?

@) O que é a altura de uma árvore binária?

@) Qual é a altura máxima de uma árvore binária com $n$ nós? Qual é a características das árvores binárias com altura máxima?

@) Qual é a altura mínima de uma árvore binária com $n$ nós? Qual é a características de árvores binárias com altura mínima?

@) O que é uma árvore binária de busca?

@) Quais são os algoritmos de busca, inserção e remoção para ABBs? Qual é a complexidade de tempo dos algoritmos?


## Começando

@) Desenhe uma árvore binária como os elementos 3, 6, 8, 20, 21, 22, 23, 30, 40, 46, 50, 60 de maneira que qualquer busca binária em um arranjo com esses elementos ou na árvore se comporte da mesma forma (como o exemplo do material).

@) Projete uma função que determine a quantidade de elementos de uma árvore binária.

@) Projete uma função que determine quantos nós em uma árvore binária tem grau 2.

@) Uma árvore binária cheia é aquela em que todos os seus nós tem grau 0 ou 2. Projete uma função que determine se uma árvore binária é cheia.

@) Projete uma função que devolva o valor máximo em uma árvore binária ou `None`{.python} se a árvore estiver vazia.

@) Desenhe a sequência de ABBs geradas pela inserção dos elementos 6, 1, 3, 7, 8, 12, 9, 5, 4, 2, 16.

@) Partindo do resultado do exercício anterior, desenhe a sequência de ABBs geradas pela remoção dos elementos 12, 1, 3, 6, 7, 8, 5, 9, 4, 2.


## Praticando

@) Projete uma função que altere os elementos negativos de uma árvore binária para seus valores absolutos.

@) Projete uma função que determine se uma árvore binária é uma ABB.

@) Uma árvore binária balanceada é aquela em que a altura das subárvores a direita e a esquerda diferem em no máximo 1 e as suas subárvores também são balanceadas. Projete uma função que verifique se uma árvore binária é balanceada.

@) Projete uma função que receba como parâmetro uma ABB e um valor $n$, contido na ABB, e determine o sucessor de $n$ na ABB, isto é, o menor valor maior que $n$. A função deve devolver `None`{.python} se não existe sucessor de $n$.

@) Projete uma função que encontre a amplitude dos valores de uma ABB não vazia. A amplitude de valores é a diferença entre o valor máximo e mínimo. A sua função deve ter tempo de execução $O(h)$, onde $h$ é a altura da árvore.


## Avançando

@) Projete uma função que crie um arranjo ordenado em ordem crescente a partir dos valores de uma ABB. Não ordene o arranjo!

@) Projete uma função que crie um arranjo ordenado em ordem decrescente a partir dos valores de uma ABB. Não ordene o arranjo!

@) Projete uma função que crie uma ABB a partir de um arranjo ordenado de valores. A árvore deve ser criada de maneira que uma busca binária na árvore tenha o mesmo comportamento que uma busca binária no arranjo. Não use a função de inserção em ABB!

@) Projete uma versão iterativa da operação de inserção em ABB.

@) Projete uma versão iterativa da operação de remoção em ABB.


## Desafios

@) Projete uma função que crie um arranjo com os valores de uma ABB em ordem de nível da direita para esquerda.

@) Projete uma função que exiba uma árvore na horizontal, como no exemplo a seguir. Note que o nó 8 não filho a esquerda e que o nó 9 não tem filho a direita. Dica: Faça uma função recursiva auxiliar (`linhas`) que devolva uma lista de strings, onde cada string representa uma linha a ser exibida, para exibir as linhas faça `print('\n'.join(linhas(t)))`{.python}.

    ```
    10
    ├── 6
    │   ├── 3
    │   └── 5
    └── 8
        ├──
        └── 9
            ├── 4
            └──
    ```

