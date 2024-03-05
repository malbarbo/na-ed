---
# vim: set spell spelllang=pt_br:
title: Tabelas de dispersão
linkcolor: Black
urlcolor: Blue
---

## Introdução

Vimos que algumas vezes informações sobre características da entrada nos permitem desenvolver algoritmos e estrutura de dados mais eficientes. \pause Por exemplo: \pause

- Se um arranjo está ordenado, então podemos fazer uma busca binária ao invés de uma busca linear; \pause

- Se as chaves para inserção em uma ABB são uniformemente distribuídas, então a altura da árvore será pequena e as operações serão eficientes.


## Introdução

Além disso, quando a entrada não tem aquelas características, ainda podemos tomar algumas providências: \pause

- Modificar a entrada, como por exemplo, ordenar os valores para fazer a busca binária; \pause

- Fazer o rebalanceamento em ABB, se as chaves não são uniformemente distribuídas, para manter a altura da árvore pequena.


## Desafio

Vimos que podemos implementar as operações de busca, inserção e remoção do TAD Dicionario usando árvores AVL com tempo $O(\lg n)$. \pause Será que podemos fazer melhor se soubermos algo sobre as entradas (chaves)? \pause

Na definição do TAD as chaves eram strings, e se as chaves fossem inteiros? \pause

E se as chaves estivem em um intervalo específico, com entre 0 e 10.000? \pause

Como tirar proveito desse conhecimento sobre as chaves para fazer uma implementação eficiente?


## Endereçamento direto

Podemos criar um arranjo com uma posição para cada possível chave da entrada, armazenamos na posição o valor associada com a chave, se houver um, ou `None`{.python} caso contrário. \pause

Essa estratégia é chamada de **endereçamento direto**. \pause De forma geral, para chaves no intervalo de $0$ a $M - 1$, alocamos um arranjo com $M$ posições.


## Endereçamento direto

<div class="columns">
<div class="column" width="48%">
\small

Implemente um dicionário que associa número naturais a strings usando endereçamento direto.

\pause

\scriptsize

```python
# As restrições (assert) sobre as
# chaves foram omitidas.
class Dicionario:
    valores: list[str | None]

    def __init__(self, m: int) -> None:
        assert 0 <= m
        self.valores = [None] * m

    def get(self, chave: int) -> str | None:
        return self.valores[chave]

    def associa(self, chave: int, valor: str):
        self.valores[chave] = valor

    def remove(self, chave: int):
        self.valores[chave] = None
```

\pause

</div>
<div class="column" width="48%">
Qual é a complexidade de tempo das operações de dicionário usando endereçamento direto? \pause $O(1)$.
</div>
</div>


## Endereçamento direto

Quais as desvantagens/limitações dessa estratégia? \pause

- Se a quantidade de chaves é muito menor que $M$, então existe um desperdício muito grande de memória. \pause Além disso, a quantidade de memória disponível pode não ser suficiente. \pause

- As chaves precisam ser maiores que $0$. \pause

- As chaves são restritas a inteiros. \pause

Vamos isolar e tentar lidar com cada uma dessas questões.


## Intervalos quaisquer

<div class="columns">
<div class="column" width="48%">

O que podemos fazer se as chaves puderem ser menores que 0, isto é, puderem estar em um intervalo de $[A, B)$ qualquer? \pause

Podemos _mapear_ cada chave para um valor distinto no intervalo  $[0, B - A)$:

$A \rightarrow 0, (A + 1) \rightarrow 1, \dots, (B - 1) \rightarrow (B - A - 1)$.

\pause

Dessa forma podemos usar o resultado do mapeamento da chave como índice em um arranjo de tamanho $B - A$. \pause

Projete uma função que faça o mapeamento de uma chave usando esse esquema.

\pause

</div>
<div class="column" width="48%">
\scriptsize

```python
def mapeia(chave: int, A: int, B: int) -> int:
    '''
    Mapeia uma chave no intervalo de
    *A* a *B* para um índice de um arranjo
    com *(B - A)* elementos.
    Requer que A <= chave < B.

    Exemplos
    >>> mapeia(-5, -5, 20)
    0
    >>> mapeia(19, -5, 20)
    24
    >>> mapeia(6, -5, 20)
    11
    '''
```

\pause

```python
    assert A <= chave < B
    return chave - A
```

</div>
</div>



## Quantidade de chaves menor que o tamanho do intervalo

O que fazer quando a quantidade de chaves armazenadas $n$ é muito menor que a quantidade de chaves possíveis $M$? \pause

Usar um arranjo de tamanho $m = O(n)$ e _mapear_ as chaves para índices no intervalo de $[0, m - 1)$ (índice válido para o arranjo). \pause

Como mapear 10 valores no intervalo de $[0, 1000]$ para valores no intervalo $[0, 20]$? ($n = 10$, $m  = 20$, $M = 1000$).


## Quantidade de chaves menor que o tamanho do intervalo

Algumas opções (sendo `k` uma chave e $m$ o tamanho do arranjo): \pause

- Por divisão: `k % m`{.python} \pause

- Por multiplicação: `floor(m * (k * A % 1))`{.python}, onde $A > 1$ é um valor real -- note que `k * A % 1`{.python} é um valor menor que `1`{.python}.


## Quantidade de chaves menor que o tamanho do intervalo

Mapeie as chaves 734, 141, 8, 230, 554, 650 usando o esquema de divisão com $m = 20$. \pause

$734 \rightarrow 14$, \pause $141 \rightarrow 1$ \pause, $8 \rightarrow 8$, \pause $230 \rightarrow 10$, \pause $554 \rightarrow 14$, \pause $650 \rightarrow 10$. \pause

Considerando que queremos usar o resultado do mapeamento de uma chave como índice em um arranjo (onde o valor associado com a chave será armazenado), qual o problema que temos? \pause Colisões! \pause

Uma **colisão** ocorre quando duas chaves são mapeadas para a mesma posição do arranjo.


## Colisões

Podemos evitar as colisões? \pause Sem conhecer as chaves, não. \pause

Podemos lidar com as colisões? \pause Sim, de algumas maneiras que vamos ver depois. \pause

Considerando o mapeamento por divisão, qual a característica das chaves para que as colisões sejam mais raras? \pause Elas devem estar uniformemente distribuídas. \pause

E para que as colisões sejam frequentes? \pause Que tenham o mesmo resto quando divididas por `m`. \pause

É possível projetar funções de mapeamento que tornem as colisões raras, independente da distribuição da entrada? \pause Sim! Mas é um assunto avançado, que não vamos discutir nessa disciplina.


## Chaves que não são inteiros

O que fazer quando as chaves não são inteiros? \pause

_Mapear_ as chaves para valores inteiros: \pause

- Diretamente para uma posição; ou \pause

- Para um inteiro que depois é mapeado para uma posição. \pause

Como mapear uma string para um inteiro? \pause Cada caractere da string é internamente representado por um número (_code point_), esse número pode ser obtido com a função `ord`{.python}. \pause

Então, podemos, por exemplo, mapear uma string para o _code point_ do seu primeiro caractere, ou para zero se a string é vazia. \pause

Qual o problema dessa forma de mapeamento? \pause Gera muitas colisões!


## Funções de dispersão

Vimos diferentes situações e diferentes formas de lidar com elas, mas elas tinha algo em comum, o que? \pause

- O mapeamento da chave para inteiro.

\pause

Vamos combinar duas funções de mapeamento: \pause

- A primeira mapeará uma chave qualquer para um número inteiro, garantindo uma distribuição uniforme do resultado. \pause Chamaremos essa função de **função de dispersão**, ou em inglês, função _hash_. \pause

- A segunda mapeará o resultado da primeira para uma posição do arranjo.


## Referências

Capítulo 11 - Seção Estratégias de hashing - Fundamentos de Python: Estruturas de dados. Kenneth A. Lambert. (Disponível na Minha Biblioteca na UEM).

Capítulo 11 - Tabelas de Dispersão - Algoritmos: Teoria e Prática, 3a. edição, Cormen, T. at all.

Capítulo 5 - Hash Tables - [Open Data Structures](https://opendatastructures.org/ods-python.pdf).
