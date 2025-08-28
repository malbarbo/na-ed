---
# vim: set spell spelllang=pt_br sw=4:
title: |
       | Estruturas de dados
       | Busca
numbersections: false
urlcolor: Blue
# TODO: adicionar soluções para exercícios de busca binária
---


## Introdução

@) Quais são as operações básicas do TAD Dicionário?

@) Como funciona a busca binária?

@) O que acontece se uma busca binária for executada em um arranjo não ordenado?

@) Por que o tempo de execução da busca binária é $O(lg(n))$?


## Começando

@) Implemente o TAD Dicionário usando encadeamento simples.

@) Considere um arranjo com os valores 3, 6, 8, 9, 20, 21, 22, 23, 30, 40, 45, 46, 50, 60 e diga quais são os índices dos valores que são comparados com a chave em uma busca binária para cada uma das chaves: 6, 30, 41, 50, 70.

@) Modifique a implementação da busca binária para funcionar com arranjos em ordem não crescente.

@) Implemente o TAD Dicionário usando arranjo ordenado e busca binária.


## Praticando

@) Implemente a busca binária usando recursividade.

@) Considerando um arranjo ordenado de inteiros onde podem existir valores repetidos, implemente uma busca binária que encontre a primeira ocorrência de um dado número inteiro no arranjo.


## Avançando

@) Use a ideia da busca binária para implementar um algoritmo que encontre a raiz quadrada inteira, se existir, de um número inteiro positivo.

@) Uma invariante de laço é uma propriedade que sempre é verdadeira antes de cada iteração do laço de repetição. A seguir estão alguns exemplos de invariantes

    ```python
    def soma(lst: list[int]) -> int:
        pares = 0
        # Invariante
        # pares é a quantidade de valores pares na sublista lst[:i]
        for i in range(len(lst)):
            if lst[i] % 2 == 0:
                pares = pares + 1
        return pares
    ```

    ```python
    def cotem(lst: list[int], v: int) -> Bool:
        # Invariante
        # v não está na sublista lst[:i]
        for i in range(len(lst)):
            if lst[i] == v:
                return True
        return False
    ```

    Enuncie uma invariante para a função de busca binária vista em sala.


## Desafios

@) Implemente a busca binária de forma que haja apenas uma comparação (dentro do laço) entre a chave e o valor do meio do arranjo.
