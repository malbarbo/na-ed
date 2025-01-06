---
# vim: set spell spelllang=pt_br sw=4:
title: |
       | Estruturas de dados
       | Árvores AVL
numbersections: false
urlcolor: Blue
---

## Introdução

@) O que é uma árvore balanceada?

@) O que é uma árvore auto balanceada?

@) O que é uma árvore AVL?

@) O que é uma rotação?

@) Mostre o que acontece em uma rotação simples (esquerda e direita) e em uma rotação dupla (esquerda-direita e direita-esquerda).

@) Por que rotações duplas são necessárias em alguns casos.


## Começando

@) Desenhe a sequência de árvores AVL geradas pela inserção dos elementos 6, 1, 3, 7, 8, 12, 9, 5, 4, 2, 16.

@) Partindo do resultado do exercício anterior, desenhe a sequência de árvores AVL geras pela remoção dos elementos 12, 1, 3, 6, 7, 8, 5, 9, 4, 2.


# Praticando

@) Baixe o arquivo `avl.py` e faça a implementação das funções `rotaciona_dir` e `balanceia_dir`. Depois modifique a função `remove` adicionando as chamadas para fazer o rebalanceamento.

@) Projete uma função que conte o número de nós em uma AVL cujos valores pertencem a um intervalo da intervalo $[a, b]$.

@) Implemente o TAD Dicionario usando árvores AVL. Note que você terá que alterar o arquivo `avl.py` para armazenar o valor associado com a chave no nó.


# Avançando

@) Modifique uma árvore AVL para que cada nó armazene a contagem de nós na sua subárvore. Use essa informação para encontrar o $k$-ésimo menor elemento eficientemente.

@) O Alberto é um estudante de Computação e quando estava estudando árvore AVL teve a ideia de criar um novo tipo de árvore balanceada: limitar a diferença entre a quantidade de nós a esquerda e a direita da raiz em 1 nó. Discuta os méritos da ideia do Aberto e as diferenças na implementação em relação a árvore AVL.
