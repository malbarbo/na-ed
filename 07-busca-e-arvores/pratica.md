---
title: Busca e árvores - Prática
urlcolor: Blue
---

<!-- Busca binária -->

@) Considere um arranjo com os valores 3, 6, 8, 9, 20, 21, 22, 23, 30, 40, 45, 46, 50, 60 e diga quais são os índices dos valores que são comparados com a chave em uma busca binária para cada uma das chaves: 6, 30, 41, 50, 70.

@) Implemente a busca binária de forma que a chave seja comparada por igualdade com o elemento "do meio" apenas uma vez. Dica: Faça a repetição até que `inicio == fim` e faça a comparação após a repetição.

@) Crie um experimento para verificar qual das duas implementação de busca binária é mais eficiente: a vista em sala ou a do exercício anterior.

@) Implemente o TAD Dicionario usando arranjo ordenado e busca binária.

<!-- Árvores binária -->

@) Desenhe uma árvore binária como os elementos 3, 6, 8, 20, 21, 22, 23, 30, 40, 46, 50, 60 de maneira que qualquer busca binária em um arranjo com esses elementos ou na árvore se comporte da mesma forma (como o exemplo do material).

@) Projete uma função que determine a quantidade de elementos de uma árvore binária.

@) Projete uma função que determine quantos nós em uma árvore binária tem grau 2.

@) Uma árvore binária cheia é aquela em que todos os seus nós tem grau 0 ou 2. Projete uma função que determine se uma árvore binária é cheia.

@) Projete uma função que determine a altura de uma árvore binária.

@) Projete uma função que altere os elementos negativos de uma árvore binária para seus valores absolutos.

@) Projete uma função que devolva o valor máximo em uma árvore binária ou `None`{.python} se a árvore estiver vazia.

@) Uma árvore binária balanceada é aquela em que a altura das subárvores a direita e a esquerda diferem em no máximo 1 e as duas subárvores também são balanceadas. Projete uma função que verifique se uma árvore binária é balanceada.

@) (Desafio) Projete uma função que exiba uma árvore na horizontal, como no exemplo a seguir. Note que o nó 8 não filho a esquerda e que o nó 9 não tem filho a direita. Dica: Faça uma função recursiva auxiliar (`linhas`) que devolva uma lista de strings, onde cada string representa uma linha a ser exibida, para exibir a linhas faça `print('\n'.join(linhas(t)))`{.python}.

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

<!-- Árvores binárias de busca -->

@) Projete uma função que determine se uma árvore binária é uma árvore binária de busca (ABB).

@) Projete uma função que encontre a amplitude dos valores de uma ABB não vazia. A amplitude de valores é a diferença entre o valor máximo e mínimo. A sua função deve ter tempo de execução $O(h)$, onde $h$ é a altura da árvore. Dica: faça duas funções auxiliares, uma para encontrar o mínimo e outra para encontrar o máximo.

@) (Desafio) Projete uma função que receba como parâmetro uma ABB e um valor $n$, contido na ABB, e determine o sucessor de $n$ na ABB, isto é, o menor valor maior que $n$. A função deve devolver `None`{.python} se não existe sucessor de $n$.

@) Projete uma função que crie uma ABB balanceada a partir de um arranjo de valores distintos em ordem crescente. Dica: use o processo do material que "transformou" um arranjo em uma ABB.

@) Projete uma função que crie um arranjo ordenado em ordem crescente a partir dos valores de uma ABB.

@) Projete uma função que crie um arranjo ordenado em ordem decrescente a partir dos valores de uma ABB.

@) (Desafio) Projete uma função que crie um arranjo com os valores de uma ABB em ordem de nível da direita para esquerda.

@) Projete uma versão iterativa da operação de inserção em ABB.

@) Projete uma versão iterativa da operação de remoção em ABB.
